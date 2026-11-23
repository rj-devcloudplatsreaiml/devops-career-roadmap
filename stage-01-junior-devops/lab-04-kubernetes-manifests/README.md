# Lab 04: Kubernetes Manifests & Schema Validation CI

Production-style Kubernetes manifests (`Namespace`, `ConfigMap`, `Deployment`, and `Service`) for an unprivileged web workload, validated strictly against Kubernetes schemas via `kubeconform` in GitHub Actions.

## Project Structure

- `k8s/namespace.yaml` — Isolated `lab-04-demo` namespace
- `k8s/configmap.yaml` — Runtime configuration injected into pods
- `k8s/deployment.yaml` — 2-replica unprivileged `Deployment` with resource requests/limits and liveness/readiness probes
- `k8s/service.yaml` — Internal `ClusterIP` service routing port 80 to container port 8080

## Local Validation

`kubeconform -strict -summary stage-01-junior-devops/lab-04-kubernetes-manifests/k8s/`
`kubectl apply --dry-run=client -f stage-01-junior-devops/lab-04-kubernetes-manifests/k8s/`
