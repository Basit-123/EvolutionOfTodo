# Phase IV Spec: Local Kubernetes Deployment

## Objective
Containerize the application and deploy it to a local Kubernetes cluster (Minikube) using Helm charts and AIOps best practices.

## Requirements
1. **Containerization**:
    - Multi-stage Dockerfile for Next.js (`apps/web`).
    - Lean Python Dockerfile for FastAPI (`apps/api`).
    - Dedicated Dockerfile for AI Chatbot (`apps/chatbot`).
2. **Orchestration**:
    - Deploy to Minikube.
    - Use Helm for release management.
3. **AIOps & Blueprints**:
    - Define reusable K8s blueprints in `blueprints/`.
    - Integration with `kubectl-ai` patterns for cluster management.
4. **Environment Management**:
    - Use ConfigMaps and Secrets for environment variables (DB URLs, AI Keys).

## High-Level Topology
- **LoadBalancer/Ingress**: Entry point for Web and API.
- **Services**:
    - `todo-web`: ClusterIP
    - `todo-api`: ClusterIP
    - `todo-chatbot`: ClusterIP

## Helm Chart Structure
`blueprints/helm/todo-app/`
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── api-deployment.yaml
│   ├── web-deployment.yaml
│   ├── chatbot-deployment.yaml
│   ├── ingress.yaml
│   └── secrets.yaml
