# streaming-data-gen
This project is a data streaming generator built using FastAPI. It enables users to dynamically generate streaming data of various distributions, including sine, cosine, and more. Additionally, it provides functionalities to introduce anomalies into straight-line data, allowing users to simulate real-world scenarios. (coming-up)

## Key Features

- **FastAPI-based**: Utilizes FastAPI to provide efficient and scalable data streaming capabilities.
- **Multiple Data Distributions**: Supports various distributions such as sine, cosine, and more for generating diverse data streams.
- **Anomaly Introduction**: Allows users to introduce anomalies into straight-line data to simulate real-world scenarios.  - Coming up
- **Customizable Parameters**: Users can fine-tune data generation parameters to suit their specific requirements.
- **Easy Integration**: Seamlessly integrates with existing applications and workflows for testing, analysis, and experimentation.

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

1. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Access various endpoints to request streaming data with desired parameters.

### Example

```python
import requests

# Example: Request sine data with frequency 0.5 and interval 0.1 seconds
response = requests.get("http://localhost:8000/data/sine/?frequency=0.5&interval=0.1")
print(response.text)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework for building APIs with Python.
- [NumPy](https://numpy.org/) - NumPy library for numerical computing with Python.
