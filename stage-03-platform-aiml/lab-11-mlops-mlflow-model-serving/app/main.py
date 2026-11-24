"""FastAPI inference service loading the trained model artifact."""
from pathlib import Path
from typing import List
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).resolve().parent / "model.joblib"
TARGET_NAMES = ["setosa", "versicolor", "virginica"]

app = FastAPI(title="Lab 11 ML Inference Service", version="1.0.0")


class PredictRequest(BaseModel):
    features: List[float] = Field(
        ...,
        min_length=4,
        max_length=4,
        description="Four numeric input features [sepal_len, sepal_wid, petal_len, petal_wid]",
    )


class PredictResponse(BaseModel):
    predicted_class_id: int
    predicted_label: str
    model_accuracy: float


def _load_bundle() -> dict:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model artifact not found at {MODEL_PATH}. Run training/train.py first.")
    return joblib.load(MODEL_PATH)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "model_present": MODEL_PATH.exists()}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    try:
        bundle = _load_bundle()
        model = bundle["model"]
        pred_id = int(model.predict([payload.features])[0])
        label = TARGET_NAMES[pred_id] if 0 <= pred_id < len(TARGET_NAMES) else str(pred_id)
        return PredictResponse(
            predicted_class_id=pred_id,
            predicted_label=label,
            model_accuracy=float(bundle.get("accuracy", 0.0)),
        )
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
