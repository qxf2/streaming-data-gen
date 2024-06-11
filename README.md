# streaming-data-gen
This project is a data streaming generator built using FastAPI. It produces streaming data of various waveforms and distributions, which can be accessed using HTTP endpoints.  

## Key Features
- **Multiple Data Distributions**: Supports various waveforms such as sine, cosine, square, sawtooth and distributions such as normal, uniform, and exponential.
- **Customizable Parameters**: Users can fine-tune data generation parameters to suit their specific requirements.
- **FastAPI-based**: Utilizes FastAPI to provide efficient and scalable data streaming capabilities.
- **Easy Integration**: Can be seamlessly incorporated into existing applications and workflows via simple HTTP requests to the provided endpoints.

## Usage
The app is accessible at http://datagen.pythonanywhere.com. Append the desired endpoint to this base URL to access streaming data. 
The available endpoints include:

**Regular Data Streams**:

- `/sine`: Generates a sine wave data stream.
- `/cosine`: Generates a cosine wave data stream.
- `/square`: Generates a square wave data stream.
- `/sawtooth`: Generates a sawtooth wave data stream.
- `/normal`: Generates a data stream with values sampled from a normal distribution.
- `/uniform`: Generates a data stream with values sampled from a uniform distribution.
- `/exponential`: Generates a data stream with values sampled from an exponential distribution.

**Anomalous Data Streams**:

- `/random`: Generates data with random anomalies.
- `/random-square`: Generates data with random square wave anomalies.
- `/clustered`: Generates data with clustered anomalies.
- `/periodic-spike`: Generates data with periodic spike anomalies within a 1-hour duration.
- `/count-per-duration`: Generates data with a specified number of anomalies within a 1-hour duration.

For example:
- http://datagen.pythonanywhere.com/sine
- http://datagen.pythonanywhere.com/normal

Customize the parameters of the requested waveform or distribution by passing query parameters in the URL. If no parameters are provided, the default parameters for each endpoint will be applied.

## Documentation
Documentation for the API endpoints is available at <a href="http://datagen.pythonanywhere.com/docs" target="_blank">http://datagen.pythonanywhere.com/docs</a>. It has information on how to use each endpoint and the available parameters.

## Examples

### 1. Example: Direct Endpoint Access
To consume streaming data directly from the endpoint, you can use a simple Python script like the following: 

```python
import requests
import json

def consume_stream(url):
    try:
        response = requests.get(url, stream=True)
        print(f"Connected to {url}")
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    data = json.loads(decoded_line)
                    print(data)
        else:
            print(f"Failed to connect, status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    stream_url = 'http://datagen.pythonanywhere.com/sine'  #In this case, the default values for the parameters will be used
    consume_stream(stream_url)
```

### 3.2. Example: Access with Parameters
You can also pass parameters to customize the generated data. Here's an example of how to request a sine wave with specific parameters:

```python
import requests

def consume_stream(url, amplitude, frequency, phase, sample_rate, interval):
    try:
        url = f"{url}?amplitude={amplitude}&frequency={frequency}&phase={phase}&sample_rate={sample_rate}&interval={interval}"
        response = requests.get(url, stream=True)
        print(f"Connected to {url}")       
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    print(decoded_line)
        else:
            print(f"Failed to connect, status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    stream_url = 'http://datagen.pythonanywhere.com/sine'
    amplitude = 10
    frequency = 2
    phase = 0 
    sample_rate = 100
    interval = 2
    consume_stream(stream_url, amplitude, frequency, phase, sample_rate, interval)
```

## Setup Instructions
To set up the project locally, follow these instructions:

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/qxf2/streaming-data-gen.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the FastAPI server locally:

   ```bash
   python app/main.py
   ```

2. Access various endpoints to request streaming data with desired parameters. Eg: http://localhost:8000/sine

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
