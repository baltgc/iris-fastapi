# Iris Flower Prediction API

FastAPI application that predicts iris flower species using machine learning.

## Quick Start

### Build Docker Image
```bash
docker build -t iris-fastapi .
```

### Run with Docker
```bash
docker run -p 8080:8000 iris-fastapi
```

### Local Development
```bash
pip install -r requirements.txt
python model_training.py
uvicorn app:app --reload
```

## API Endpoints

- `GET /` - Welcome message
- `POST /predict` - Predict iris species
- `GET /docs` - Interactive API documentation

## Example Request
```bash
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }'
```

## Species Mapping
- `0`: Setosa
- `1`: Versicolor  
- `2`: Virginica 