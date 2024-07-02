"""
Script for generating heart rate anomalies occuring at random intervals.
Combined /sine + /clustered to generate streaming data with anomalies.
Please generate your own token to use this script.
"""
import requests
import concurrent.futures
from queue import Queue
import threading

token = "YOUR_TOKEN_HERE"

def consume_stream_sine(url, amplitude, frequency, phase, sample_rate, interval, queue):
    try:
        url = f"{url}?amplitude={amplitude}&frequency={frequency}&phase={phase}&sample_rate={sample_rate}&interval={interval}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, stream=True)
        print(f"Connected to {url}")       
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    print(f"Sine: {decoded_line}")
                    queue.put(float(decoded_line))
        else:
            print(f"Failed to connect, status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def consume_stream_anomaly(url, minimum_interval, maximum_interval, data_interval, queue):
    try:
        url = f"{url}?minimum_interval={minimum_interval}&maximum_interval={maximum_interval}&data_interval={data_interval}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, stream=True)
        print(f"Connected to {url}")       
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    print(f"Anomaly: {decoded_line}")
                    queue.put(float(decoded_line))
        else:
            print(f"Failed to connect, status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def combine_streams(queue1, queue2):
    value1 = queue1.get()
    value2 = queue2.get()
    combined_value = value1 + value2
    print(f"Combined: {combined_value}")

if __name__ == "__main__":
    stream_url_sine = 'http://datagen.pythonanywhere.com/sine'
    stream_url_anomaly = 'http://datagen.pythonanywhere.com/anomalies/clustered'
    amplitude = 10
    frequency = 2
    phase = 0 
    sample_rate = 25
    interval = 0.1 # Common for both sine and anomaly    
    minimum_interval = 80
    maximum_interval = 150
    print ("Starting the Streaming Data Generator")
    queue1 = Queue()
    queue2 = Queue()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(consume_stream_sine, stream_url_sine, amplitude, frequency, phase, sample_rate, interval, queue1)
        executor.submit(consume_stream_anomaly, stream_url_anomaly, minimum_interval, maximum_interval, interval, queue2)
        combine_thread = threading.Thread(target=combine_streams, args=(queue1, queue2), daemon=True)
        combine_thread.start()
        combine_thread.join()
