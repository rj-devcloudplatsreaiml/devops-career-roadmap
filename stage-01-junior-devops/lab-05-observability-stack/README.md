# Lab 05: Observability Stack (Prometheus, Grafana & Datadog)

Hybrid observability stack combining open-source metrics/alerting (Prometheus, Node Exporter, Grafana) with enterprise infrastructure, container, log, and APM collection via the Datadog Agent.

## Architecture & Files

- `docker-compose.yml` — Runs Prometheus (`9090`), Node Exporter (`9100`), Grafana (`3000`), and an optional `datadog` profile for the Datadog Agent (`8125/udp` DogStatsD, `8126` APM)
- `prometheus/prometheus.yml` — Scrape configuration for Prometheus self-metrics and Node Exporter
- `prometheus/alert_rules.yml` — Alerting rule detecting unreachable scrape targets (`InstanceDown`)
- `grafana/provisioning/datasources/datasource.yml` — Auto-provisions Prometheus as the default Grafana datasource
- `datadog/datadog.yaml` — Datadog Agent configuration enabling logs, APM, process collection, and unified service tags
- `datadog/conf.d/docker.d/conf.yaml` — Datadog Docker integration check configuration

## Local Usage

Start Prometheus, Node Exporter, and Grafana:
`docker compose up -d`

Start the full stack including Datadog Agent:
`DD_API_KEY=<your_api_key> docker compose --profile datadog up -d`

Stop and clean up:
`docker compose --profile datadog down`
