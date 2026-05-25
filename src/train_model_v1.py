from sklearn.linear_model import LogisticRegression
from utils import (
    load_params,
    load_data,
    train_test_split_data,
    save_model,
    evaluate_and_save,
)

def main():
    params = load_params()

    data_path = "data/raw/train_v1.csv"
    model_path = "models/model_v1.joblib"
    metrics_path = "metrics/model_v1_metrics.yaml"

    X, y = load_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split_data(
        X, y,
        test_size=params["split"]["test_size"],
        random_state=params["split"]["random_state"],
    )

    clf = LogisticRegression(
        C=params["model_v1"]["C"],
        max_iter=params["model_v1"]["max_iter"],
        random_state=params["model_v1"]["random_state"],
    )

    clf.fit(X_train, y_train)

    save_model(clf, model_path)
    evaluate_and_save(clf, X_test, y_test, metrics_path)

if __name__ == "__main__":
    main()