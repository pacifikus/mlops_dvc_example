import os
import joblib
import yaml
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def load_params(path="params.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_data(path):
    df = pd.read_csv(path)
    X = df.drop(columns=["target"]).values
    y = df["target"].values
    return X, y

def train_test_split_data(X, y, test_size, random_state):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def evaluate_and_save(model, X_test, y_test, metrics_path):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)
    with open(metrics_path, "w") as f:
        yaml.safe_dump({"accuracy": float(acc)}, f)
    print(f"Accuracy: {acc:.4f}")