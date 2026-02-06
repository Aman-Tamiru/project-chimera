# 🦁 Project Chimera: Autonomous Influencer Factory
**Governed AI Orchestrator on Base Sepolia**

Project Chimera is a spec-driven autonomous agent framework. It shifts the paradigm from "Vibe Coding" to **Hard Governance**, where an agent’s actions are strictly bounded by technical blueprints and on-chain identity verification.

---

## 🗺️ Project Map
This directory structure enforces the separation of concerns and ensures the agent can navigate its own codebase without "guessing."

```text
project-chimera/
├── .cursor/rules/          # ⚖️ Hard Governance (MDC Rules)
│   └── chimera-governance.mdc
├── specs/                  # 📐 The Source of Truth (Blueprints)
│   ├── technical.md        # Technical architecture
│   ├── functional.md       # Given/When/Then acceptance criteria
│   └── database.md         # ERDs and Schema definitions
├── skills/                 # 🛠️ Skill Factory (Modular Tools)
│   ├── trend_research/     # JSON Contract for data sensing
│   └── content_generation/ # JSON Contract for LLM output
├── tests/                  # 🧪 TDD Suite (Pytest/Unittest)
├── frontend/               # 📊 Streamlit Vitals Dashboard
├── Dockerfile              # 🐳 Multi-stage build (Verification layer)
├── Makefile                # ⚡ Automation targets (setup, test, build)
└── chimera_brain.py        # 🧠 Core Logic & On-chain Identity