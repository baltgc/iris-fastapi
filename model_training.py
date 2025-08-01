# model_training.py

import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model to a file
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)