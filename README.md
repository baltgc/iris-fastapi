# Iris Flower Prediction API

A machine learning API built with FastAPI that predicts iris flower species based on sepal and petal measurements using a Logistic Regression model.

## 🚀 Features

- **RESTful API**: Built with FastAPI for high performance and automatic API documentation
- **Machine Learning Model**: Uses scikit-learn's Logistic Regression for iris species prediction
- **Docker Support**: Containerized application for easy deployment
- **Input Validation**: Pydantic models for request validation
- **Auto-generated Documentation**: Interactive API docs with Swagger UI

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd first_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn scikit-learn pydantic numpy
   ```

4. **Train the model**
   ```bash
   python model_training.py
   ```

5. **Run the application**
   ```bash
   uvicorn app:app --reload
   ```

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t iris-prediction-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 iris-prediction-api
   ```

## 🏃‍♂️ Quick Start

1. Start the server (if not already running):
   ```bash
   uvicorn app:app --reload
   ```

2. Open your browser and navigate to:
   - **API Documentation**: http://localhost:8000/docs
   - **Alternative Docs**: http://localhost:8000/redoc
   - **Home Endpoint**: http://localhost:8000/

3. Make a prediction request:
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{
          "sepal_length": 5.1,
          "sepal_width": 3.5,
          "petal_length": 1.4,
          "petal_width": 0.2
        }'
   ```

## 📚 API Endpoints

### GET `/`
- **Description**: Welcome message
- **Response**: `{"message": "Welcome to the Iris Flower Prediction API"}`

### POST `/predict`
- **Description**: Predict iris species based on flower measurements
- **Request Body**:
  ```json
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
  ```
- **Response**:
  ```json
  {
    "predicted_species": 0
  }
  ```

### Species Mapping
- `0`: Setosa
- `1`: Versicolor
- `2`: Virginica

## 📁 Project Structure

```
first_project/
├── app.py                 # FastAPI application
├── model_training.py      # Model training script
├── iris_model.pkl        # Trained model file
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🔧 Configuration

### Environment Variables
The application can be configured using environment variables:

- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `8000`)

### Model Parameters
The Logistic Regression model is trained with:
- `max_iter=200`: Maximum iterations for convergence
- Dataset: scikit-learn's built-in iris dataset

## 🧪 Testing

### Manual Testing
1. Use the interactive API documentation at `http://localhost:8000/docs`
2. Test with curl commands as shown in the Quick Start section

### Example Test Cases
```bash
# Setosa (small flowers)
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

# Versicolor (medium flowers)
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 6.3, "sepal_width": 3.3, "petal_length": 4.7, "petal_width": 1.6}'

# Virginica (large flowers)
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 6.3, "sepal_width": 3.3, "petal_length": 6.0, "petal_width": 2.5}'
```

## 🚀 Deployment

### Production Deployment
For production deployment, consider:

1. **Using a production ASGI server**:
   ```bash
   pip install gunicorn
   gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

2. **Environment variables**:
   ```bash
   export HOST=0.0.0.0
   export PORT=8000
   ```

3. **Reverse proxy** (nginx example):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 🔍 Monitoring and Logging

The application includes basic logging. For production, consider:
- Structured logging with `structlog`
- Application monitoring with Prometheus/Grafana
- Error tracking with Sentry

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning capabilities
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation
- [Uvicorn](https://www.uvicorn.org/) for the ASGI server

## 📞 Support

If you encounter any issues or have questions:
1. Check the [API documentation](http://localhost:8000/docs)
2. Review the project structure and code
3. Open an issue on the repository

---

**Happy Predicting! 🌸** 