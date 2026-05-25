from sklearn.ensemble import RandomForestClassifier
from utils import (
    load_params,
    load_data,
    train_test_split_data,
    save_model,
    evaluate_and_save,
)

def main():
    params = load_params()

    data_path = "data/processed/train_v2.csv"
    model_path = "models/model_v2.joblib"
    metrics_path = "metrics/model_v2_metrics.yaml"

    X, y = load_data(data_path)

    X_train, X_test, y_train, y_test = train_test_split_data(
        X, y,
        test_size=params["split"]["test_size"],
        random_state=params["split"]["random_state"],
    )

    clf = RandomForestClassifier(
        n_estimators=params["model_v2"]["n_estimators"],
        max_depth=params["model_v2"]["max_depth"],
        random_state=params["model_v2"]["random_state"],
    )

    clf.fit(X_train, y_train)

    save_model(clf, model_path)
    evaluate_and_save(clf, X_test, y_test, metrics_path)

if __name__ == "__main__":
    main()