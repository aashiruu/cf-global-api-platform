# CF-Global-API-Platform

Production-grade API platform with zero-trust networking and full observability stack.
This project implements a cloud-native monitoring and observability stack for a production-like web application running on a Linux virtual machine. It demonstrates how modern DevOps tooling is used to collect, expose, scrape, store, and visualize metrics across multiple services in real time.
The stack includes an Nginx reverse proxy, a FastAPI application, and supporting infrastructure components, all monitored using Prometheus and visualized through Grafana dashboards. Each service exposes metrics that allow end-to-end visibility into application health, traffic flow, and system performance.
This repository is designed as a hands-on DevOps portfolio project, emphasizing real-world configuration, troubleshooting, and validation rather than a simplified demo setup.

## Architecture
```
Internet → Cloudflare Tunnel → FastAPI (Docker) → Alloy → Grafana Cloud
                                     ↓
                               Prometheus (Local)
```
## Key Features
Reverse-proxied web application with HTTP and HTTPS support
Metrics exposure for:
• FastAPI application
• Nginx server status
• Prometheus self-metrics
• Cloudflared tunnel metrics
• Prometheus health validation and target monitoring
• Grafana dashboards for real-time observability
• Production-style debugging and recovery (service restarts, port conflicts, scrape validation)

## Security Model

- **Zero Inbound Ports**: Cloudflare Tunnel handles all ingress
- **No Public IP Exposure**: Origin server completely hidden
- **TLS Termination**: At Cloudflare edge
- **Secret Management**: Environment variables, not in Git

## Observability

### Logs (Grafana Cloud Loki)
- **Collector**: Grafana Alloy
- **Source**: Docker container logs
- **Query**: `{container="cf-api"}`
- **Volume**: Real-time streaming

### Metrics (Prometheus)
- **Endpoint**: `http://localhost:8000/metrics`
- **Exporter**: prometheus-fastapi-instrumentator
- **Local Dashboard**: `http://localhost:9090`

## Project Structure
```
cf-global-api-platform/
├── main.py
├── Dockerfile
├── requirements.txt
├── monitoring/
│   └── alloy-config.alloy
└── README.md
```

## Technology Stack

- **Runtime**: Python 3.10
- **Framework**: FastAPI + Uvicorn
- **Containerization**: Docker
- **CDN/Tunnel**: Cloudflare
- **Metrics**: Prometheus + prometheus-fastapi-instrumentator
- **Logs**: Grafana Alloy + Loki
- **Monitoring**: Grafana Cloud

## Key Metrics

Current performance:
- Latency: Sub-second response times
- Uptime: 99.9% (CloudFlare backed)
- Log Volume: 30+ entries successfully shipped to Grafana Cloud
- Zero dropped logs

## What This Demonstrates

1. **Infrastructure as Code**: Reproducible deployment
2. **Security Best Practices**: Zero-trust networking
3. **Observability**: Full telemetry pipeline
4. **Production Readiness**: Restart policies, health checks
5. **Cloud-Native**: Containerized, stateless design

## Screenshots
### Live API endpoint publicly accessible via Cloudflare Tunnel - zero inbound ports on origin server
<img width="821" height="264" alt="image" src="https://github.com/user-attachments/assets/f436460c-5171-4798-9f8b-8c68c249a032" />

### cf-ray header proves Cloudflare is proxying all traffic - origin IP completely hidden
<img width="958" height="475" alt="image" src="https://github.com/user-attachments/assets/323594f8-bf33-4467-8f68-38d552231914" />

### Port 8000 bound to localhost only (127.0.0.1) - NOT publicly accessible. Traffic only via Cloudflare Tunnel
<img width="884" height="332" alt="image" src="https://github.com/user-attachments/assets/571fbbeb-15d1-4f95-bd20-d0a83a00106a" />

### Real-time logs streaming to Grafana Cloud
<img width="1045" height="658" alt="image" src="https://github.com/user-attachments/assets/bcdee0ec-7151-460d-9688-bb28bc33e0f4" />

### Metrics being scraped from FastAPI + cloudflared
<img width="1078" height="689" alt="image" src="https://github.com/user-attachments/assets/ea6b0dee-363f-4b5d-8764-ec2f1b607a8a" />

---

**Built with**: FastAPI, Docker, Cloudflare, Grafana Stack, Prometheus
