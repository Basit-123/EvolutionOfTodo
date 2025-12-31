# Phase V Spec: Advanced Cloud Deployment & Event-Driven Architecture

## Objective
Scale the application to a production-grade cloud environment (DOKS) using Dapr and Kafka for event-driven microservices communication.

## Functional Requirements
1. **Event-Driven Completion**:
    - When a task is marked `completed`, publish a `TodoCompleted` event.
2. **Distributed Resilience**:
    - Use Dapr sidecars for state management and reliable pub/sub.
3. **Cloud Hosting**:
    - Deployment to DigitalOcean Kubernetes (DOKS).

## Technical Architecture
- **Runtime**: Dapr (Distributed Application Runtime).
- **Message Broker**: Apache Kafka.
- **Microservices**:
    - `api`: Publishes events to Kafka via Dapr.
    - `analytics-worker` (new): Subscribes to events to track user productivity.

## Dapr Components (`blueprints/dapr/`)
- `pubsub-kafka.yaml`: Configuration for Kafka pub/sub component.
- `statestore-redis.yaml`: (Optional) For distributed caching.

## Event Schema
```json
{
  "event_type": "todo.completed",
  "data": {
    "todo_id": 123,
    "user_id": "user_123",
    "timestamp": "2025-12-31T23:59:59Z"
  }
}
```

## DOKS Blueprint
Infrastructure as Code (IaC) principles:
- LoadBalancer for traffic entry.
- PersistentVolumes for state if using self-hosted Kafka.
- Horizontal Pod Autoscaler (HPA) based on CPU/Memory/Message Lag.
