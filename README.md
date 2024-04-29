# streaming-data-gen
This project is a data streaming generator built using FastAPI. It produces streaming data of various waveforms and distributions, which can be accessed using HTTP endpoints.  

## Key Features
- **Multiple Data Distributions**: Supports various waveforms such as sine, cosine, square, sawtooth and distributions such as normal, uniform, and exponential.
- **Customizable Parameters**: Users can fine-tune data generation parameters to suit their specific requirements.
- **FastAPI-based**: Utilizes FastAPI to provide efficient and scalable data streaming capabilities.
- **Easy Integration**: Can be seamlessly incorporated into existing applications and workflows via simple HTTP requests to the provided endpoints.

## Getting Started

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

2. Access various endpoints to request streaming data with desired parameters.

### 3.1. Example: Direct Endpoint Access
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
    stream_url = 'http://localhost:7000/sine'  #In this case, the default values for the parameters will be used
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
    stream_url = 'http://localhost:7000/sine'
    amplitude = 10
    frequency = 2
    phase = 0 
    sample_rate = 100
    interval = 2
    consume_stream(stream_url, amplitude, frequency, phase, sample_rate, interval)
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs with Python.
- [NumPy](https://numpy.org/) - NumPy library for numerical computing with Python.
