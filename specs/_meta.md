# Project Chimera: Meta Specification

## 1. Vision Statement
Project Chimera is an autonomous influencer system designed to research trends, generate high-quality content, and manage on-chain identity without human intervention. The goal is to build a "Factory" where intent (Specs) drives implementation.

## 2. Prime Directive
**NEVER generate implementation code without first verifying requirements against the `/specs` directory.** Ambiguity is the enemy of the agent; if a spec is missing, the agent must request a spec update before proceeding.

## 3. Project Constraints
- **Identity:** Must use Basenames on Base Sepolia (`aman-chimera.basetest.eth`).
- **Network:** Base (Layer 2).
- **Communication:** Social protocols must adhere to the OpenClaw standard for agent-to-agent availability.
- **Verification:** All builds must pass through Dockerized linting and TDD (Test-Driven Development) pipelines.

## 4. Social Protocols (OpenClaw)
The agent will publish its "Thinking" and "Availability" to the OpenClaw network. 
- **Status Endpoint:** `/.well-known/openclaw/status.json`
- **Capability:** Trend Research, On-chain Registration, Social Posting.

## 5. Traceability
All development steps must be recorded via **Tenx MCP Sense**. Every PR (Pull Request) must map back to a requirement in `functional.md` or `technical.md`.