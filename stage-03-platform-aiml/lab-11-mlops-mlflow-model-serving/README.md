# Lab 11: MLOps Experiment Tracking (MLflow) & Model Serving (FastAPI)

## Objective
Demonstrate reproducible ML lifecycle basics from a platform/DevOps lens:
- Track training hyperparameters and metrics in **MLflow** (`training/train.py`)
- Serve predictions via a typed **FastAPI** endpoint (`/health` and `/predict`)
- Package model training and serving cleanly inside a **Docker** image (`Dockerfile`)
