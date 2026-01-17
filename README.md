# CF-Global-API-Platform

Production-grade API platform with zero-trust networking and full observability stack.

## 🏗️ Architecture
```
Internet → Cloudflare Tunnel → FastAPI (Docker) → Alloy → Grafana Cloud
                                     ↓
                               Prometheus (Local)
```

## 🔒 Security Model

- **Zero Inbound Ports**: Cloudflare Tunnel handles all ingress
- **No Public IP Exposure**: Origin server completely hidden
- **TLS Termination**: At Cloudflare edge
- **Secret Management**: Environment variables, not in Git

## 📊 Observability

### Logs (Grafana Cloud Loki)
- **Collector**: Grafana Alloy
- **Source**: Docker container logs
- **Query**: `{container="cf-api"}`
- **Volume**: Real-time streaming

### Metrics (Prometheus)
- **Endpoint**: `http://localhost:8000/metrics`
- **Exporter**: prometheus-fastapi-instrumentator
- **Local Dashboard**: `http://localhost:9090`

## 🚀 Live Demo

- **API**: https://api.aashiruu.online/
- **Health Check**: https://api.aashiruu.online/healthz
- **Metrics**: http://localhost:8000/metrics (internal only)

## 📁 Project Structure
```
cf-global-api-platform/
├── main.py              # FastAPI application
├── Dockerfile           # Container definition
├── requirements.txt     # Python dependencies
├── monitoring/
│   └── alloy-config.alloy  # Log collection config
└── README.md
```

## 🔧 Technology Stack

- **Runtime**: Python 3.10
- **Framework**: FastAPI + Uvicorn
- **Containerization**: Docker
- **CDN/Tunnel**: Cloudflare
- **Metrics**: Prometheus + prometheus-fastapi-instrumentator
- **Logs**: Grafana Alloy + Loki
- **Monitoring**: Grafana Cloud

## 📈 Key Metrics

Current performance:
- Latency: Sub-second response times
- Uptime: 99.9% (CloudFlare backed)
- Log Volume: 30+ entries successfully shipped to Grafana Cloud
- Zero dropped logs

## 🎓 What This Demonstrates

1. **Infrastructure as Code**: Reproducible deployment
2. **Security Best Practices**: Zero-trust networking
3. **Observability**: Full telemetry pipeline
4. **Production Readiness**: Restart policies, health checks
5. **Cloud-Native**: Containerized, stateless design

## 🔮 Future Enhancements

- [ ] Grafana dashboard JSON templates
- [ ] Alert rules for SLO violations  
- [ ] Distributed tracing (OpenTelemetry)
- [ ] Multi-region deployment
- [ ] Load testing results

## 📝 License

MIT

---

**Built with**: FastAPI, Docker, Cloudflare, Grafana Stack, Prometheus
