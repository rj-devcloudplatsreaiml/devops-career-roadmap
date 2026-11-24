"""Train a lightweight classifier, log run to MLflow, and save model artifact."""
from pathlib import Path
import joblib
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACT_PATH = BASE_DIR / "app" / "model.joblib"
TRACKING_URI = (BASE_DIR / "mlruns").as_uri()


def main(max_iter: int = 200, test_size: float = 0.2, random_state: int = 42) -> None:
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment("lab-11-iris-baseline")

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    with mlflow.start_run(run_name="logreg-baseline"):
        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("max_iter", max_iter)
        mlflow.log_param("test_size", test_size)
        mlflow.log_metric("accuracy", float(acc))

        ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump({"model": model, "accuracy": float(acc)}, ARTIFACT_PATH)
        mlflow.log_artifact(str(ARTIFACT_PATH), artifact_path="model_artifact")

        print(f"Run complete | accuracy={acc:.4f} | artifact={ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
