import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures


def main():
    input_path = "data/raw/train_v1.csv"
    output_dir = "data/processed"
    output_path = os.path.join(output_dir, "train_v2.csv")

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)

    feature_cols = [c for c in df.columns if c != "target"]
    X = df[feature_cols].values
    y = df["target"].values

    # Масштабирование
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Полиномиальные признаки второй степени (без bias)
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X_scaled)

    poly_feature_names = poly.get_feature_names_out(feature_cols)

    df_poly = pd.DataFrame(X_poly, columns=poly_feature_names)
    df_poly["target"] = y

    df_poly.to_csv(output_path, index=False)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    main()