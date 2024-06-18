from locust import HttpUser, task, between, events
import json
import time

response_times = []

class DataGenUser(HttpUser):
    host = "http://datagen.pythonanywhere.com"
    wait_time = between(1, 2)
    
    @task
    def get_sine(self):
        global response_times
        amplitude = 10
        frequency = 2
        phase = 0
        sample_rate = 100
        interval = 2

        url_path = "/sine"
        query_params = f"?amplitude={amplitude}&frequency={frequency}&phase={phase}&sample_rate={sample_rate}&interval={interval}"
        full_url = self.host + url_path + query_params

        with self.client.get(full_url, stream=True) as response:
            start_time = time.time()
            for line in response.iter_lines():
                if line:
                    end_time = time.time()
                    decoded_line = line.decode('utf-8')
                    data = json.loads(decoded_line)
                    response_time = end_time - start_time
                    print(f"Received data point: {data}, Response time: {response_time:.6f} seconds")
                    events.request.fire(request_type="GET", name=full_url, response_time=int(response_time * 1000), response_length=len(line))
                    response_times.append(response_time)
                    start_time = time.time()

def on_stop(environment, **kwargs):
    if len(response_times) > 0:
        average_response_time = sum(response_times) / len(response_times)
        percentile_95 = sorted(response_times)[int(len(response_times) * 0.95)]
        print("Average response time:", average_response_time)
        print("95th percentile response time:", percentile_95)
    else:
        print("No data points collected")

events.quitting.add_listener(on_stop)
