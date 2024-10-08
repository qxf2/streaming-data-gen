# streaming-data-gen
This project is a data streaming generator built using FastAPI. It produces streaming data of various waveforms and distributions, which can be accessed using HTTP endpoints. 

This project has been designed, developed and maintained by [Qxf2 Services](https://qxf2.com/?utm_source=github&utm_medium=click&utm_campaign=Streaming%20datagen). Qxf2 provides flexible and custom QA services to startups and early-stage products.

## Key Features
- **Multiple Data Distributions**: Supports various waveforms such as sine, cosine, square, sawtooth and distributions such as normal, uniform, and exponential.
- **Customizable Parameters**: Users can fine-tune data generation parameters to suit their specific requirements.
- **FastAPI-based**: Utilizes FastAPI to provide efficient and scalable data streaming capabilities.
- **Easy Integration**: Can be seamlessly incorporated into existing applications and workflows via simple HTTP requests to the provided endpoints.
- **Authentication**: Requires bearer token authentication for accessing the endpoints.

## Usage
The app is accessible at http://datagen.pythonanywhere.com. The available endpoints include:

**Regular Data Streams**:
 Append the desired endpoint to the base_url.
 
- `/sine`: Generates a sine wave data stream.
- `/cosine`: Generates a cosine wave data stream.
- `/square`: Generates a square wave data stream.
- `/sawtooth`: Generates a sawtooth wave data stream.
- `/normal`: Generates a data stream with values sampled from a normal distribution.
- `/uniform`: Generates a data stream with values sampled from a uniform distribution.
- `/exponential`: Generates a data stream with values sampled from an exponential distribution.

**Anomalous Data Streams**:
 Append the desired endpoint to base_url/anomalies.
 
- `/random`: Generates data with random anomalies.
- `/random-square`: Generates data with random square wave anomalies.
- `/clustered`: Generates data with clustered anomalies.
- `/periodic-spike`: Generates data with periodic spike anomalies within a 1-hour duration.
- `/count-per-duration`: Generates data with a specified number of anomalies within a 1-hour duration.

For example:
- http://datagen.pythonanywhere.com/sine
- http://datagen.pythonanywhere.com/anomalies/random

To access these endpoints, provide a valid bearer token in the request headers.

Customize the parameters of the requested waveform or distribution by passing query parameters in the URL. If no parameters are provided, the default parameters for each endpoint will be applied.

## Documentation
Documentation for the API endpoints is available at <a href="http://datagen.pythonanywhere.com" target="_blank">http://datagen.pythonanywhere.com/ </a>. It has information on how to use each endpoint and the available parameters.

## Obtaining Bearer Token
To obtain a bearer token for accessing these endpoints, follow these steps:

1. **Register**:
   - Navigate to the registration section at http://datagen.pythonanywhere.com/#register-section.
   - Enter your desired username and password and submit to register with our application.
   
2. **Login**:
   - Go to the login section at http://datagen.pythonanywhere.com/#login-section.
   - Enter your registered username and password to log in.

3. **Use the Token**:
   - After successful login, copy the generated bearer token provided.
   - Include the token in the Authorization header of your HTTP requests to access the streaming endpoints.

Alternatively, you can use curl commands to register and obtain the token:

```bash
curl -X POST http://datagen.pythonanywhere.com/register -H "Content-Type: application/json" -d '{"username": "youruser", "password": "yourpassword"}'

curl -X POST http://datagen.pythonanywhere.com/token -H "Content-Type: application/x-www-form-urlencoded" -d "username=youruser&password=yourpassword"

curl -X GET http://datagen.pythonanywhere.com/sine -H "Authorization: Bearer YOUR_TOKEN_HERE"

```

## Examples

### 1. Example: Direct Endpoint Access
To consume streaming data directly from the endpoint, you can use a simple Python script like the following: 

```python
import requests
import json

def consume_stream(url):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, stream=True)
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
    stream_url = 'http://datagen.pythonanywhere.com/sine'   #In this case, the default values for the parameters will be used
    consume_stream(stream_url)
```

### 3.2. Example: Access with Parameters
You can also pass parameters to customize the generated data. Here's an example of how to request a sine wave with specific parameters:

```python
import requests

def consume_stream(url, amplitude, frequency, phase, sample_rate, interval):
    try:
        url = f"{url}?amplitude={amplitude}&frequency={frequency}&phase={phase}&sample_rate={sample_rate}&interval={interval}"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, stream=True)
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

### Configuration

1. Generate 'SECRET_KEY'
   
   This is essential for cryptograhic signing within the application. To generate the key, run the following command in your terminal:

   ```bash
   openssl rand -hex 32
   ```

2. Set 'SECRET_KEY' as Environment Variable.
   * Create a '.env' file in the project root
   
   * Add the following line to '.env' replaceing 'your_secret_key_value_here' with the generated 'SECRET_KEY'"

   ```bash
   SECRET_KEY=your_secret_key_value_here
   ```
   * Ensure '.emv' is listed in your '.gitignore' file to prevent it from being committed to version control.

### Usage

1. Run the FastAPI server locally:

   ```bash
   python app/main.py
   ```

2. Access the application at 'http://localhost:8000'.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Qxf2 Services - custom testing services for startups
This application is an off-shoot of some technical testing that [Qxf2](https://qxf2.com/?utm_source=github&utm_medium=click&utm_campaign=Streaming%20datagen) performed at a client. **Qxf2 provides flexible QA services for startups and early-stage products**. We frequently support employ advanced testing techniques and develop QA tools to test what matters to our clients. Our vast experience with early-stage products has lead us to design and offer flexible testing services that are unique in the market. Some examples of QA services that you might not know about include - [lightweight testing service for startups](https://qxf2.com/essential-service-offering), our [foundational testing service](https://qxf2.com/foundational-service-offering), fractional QA advisor role, [deep AI/ML testing](https://qxf2.com/aiml-testing-offering) and so much more. If this streaming data generator helped you, consider spreading the word about Qxf2 and give this repo a star. And if you want to hire us for some advanced, technical testing, simply drop an note to Arun (mak@qxf2.com).