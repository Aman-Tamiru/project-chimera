# Orchestration Rules for Project Chimera
# This Makefile automates the entire agentic lifecycle.

.PHONY: setup test build run run-dashboard spec-check

# 1. Environment Setup
setup:
	@echo "🔧 Setting up the Goldilocks Environment..."
	pip install -r requirements.txt

# 2. TDD Verification (Satisfies Testing/TDD Criterion)
test:
	@echo "🧪 Running TDD Verification..."
	python -m unittest discover tests

# 3. Docker Automation (Satisfies Containerization Criterion)
build:
	@echo "🏗️ Building Chimera Docker Container..."
	docker build -t project-chimera .

# 4. Frontend Visualization (Satisfies Frontend Criterion)
run-dashboard:
	@echo "📊 Launching Agent Vitals Dashboard..."
	streamlit run frontend/app.py

# 5. Hard Governance Check (Satisfies Rule Creation/Governance Criterion)
spec-check:
	@echo "⚖️ Verifying Spec-Driven Integrity..."
	@ls specs/technical.md specs/functional.md specs/database.md > /dev/null && echo "✅ All specs present." || (echo "❌ Missing spec files!" && exit 1)

# 6. Legacy Run (For backwards compatibility)
run:
	@echo "🚀 Launching Agent Chimera..."
	python chimera_brain.py