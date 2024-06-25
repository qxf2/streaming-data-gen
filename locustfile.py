from locust import HttpUser, task, between, events
import json
import time

response_times = []


class DataGenUser(HttpUser):
    host = "http://datagen.pythonanywhere.com"
    wait_time = between(1, 2)

    @task
    def get_sine(self):
        """
        Generates a sine wave data stream by making a GET request to the "/sine" endpoint and 
        processing the received lines to calculate response time and record custom metrics.
        """
        global response_times
        with self.client.get("/sine", stream=True) as response:
            start_time = time.time()
            for line in response.iter_lines():
                if line:
                    end_time = time.time()
                    decoded_line = line.decode("utf-8")
                    data = json.loads(decoded_line)
                    response_time = end_time - start_time
                    print(
                        f"Received data point: {data}, Response time: {response_time:.6f} seconds"
                    )
                    # record custom metric
                    events.request.fire(
                        request_type="GET",
                        name="/sine",
                        response_time=int(response_time * 1000),
                        response_length=len(line),
                    )
                    response_times.append(response_time)
                    start_time = time.time()