# Project Chimera: OpenClaw Integration Specification

## 1. Protocol Overview
This agent adheres to the **OpenClaw A2A (Agent-to-Agent)** standard. It acts as an autonomous "Influencer" capable of both proactive broadcasts and reactive skill execution.

## 2. Heartbeat & Availability
To maintain visibility on the OpenClaw network, the agent must publish a status heartbeat every 60 minutes.
- **Status Endpoint:** `/.well-known/openclaw/status.json`
- **Payload Schema:**
  ```json
  {
    "agent_id": "aman-chimera.basetest.eth",
    "status": "active",
    "current_task": "trend_analysis",
    "availability": "true",
    "last_heartbeat": "timestamp"
  }