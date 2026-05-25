import os
import pandas as pd
from sklearn.datasets import make_classification


def main():
    os.makedirs("data/raw", exist_ok=True)

    X, y = make_classification(
        n_samples=1000,
        n_features=5,
        n_informative=3,
        n_redundant=0,
        random_state=42
    )

    cols = [f"feature_{i}" for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=cols)
    df["target"] = y

    df.to_csv("data/raw/train_v1.csv", index=False)
    print("Saved data/raw/train_v1.csv")

if __name__ == "__main__":
    main()