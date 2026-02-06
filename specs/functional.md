# Project Chimera: Functional Specifications

## 1. Overview
This document defines the behavioral requirements for the Chimera Agent. These requirements act as the "Goal Posts" for our Test-Driven Development (TDD) process.

## 2. User Stories (The Agent's Perspective)

### Core Identity
- **As an Agent**, I need to register a Basename on Base Sepolia so that I have a verified, human-readable on-chain identity.
- **As an Agent**, I need to resolve my Basename to my wallet address to verify ownership of my assets.

### Trend Research & Content
- **As an Agent**, I need to scan blockchain activity and social trends so that I can identify high-growth topics for content generation.
- **As an Agent**, I need to store identified trends in a structured database schema to ensure historical traceability of my decisions.

### Autonomous Governance
- **As an Agent**, I need to verify my instructions against the `specs/` directory before executing any code to prevent hallucination.
- **As an Agent**, I need to report my operational status to the OpenClaw network so other agents can interact with me.

## 3. Success Criteria (Definition of Done)
1. **Identity Verified:** The agent can successfully return its registered name: `aman-chimera.basetest.eth`.
2. **On-chain Action:** The agent can execute a transaction on Base Sepolia using its own private key.
3. **Traceability:** Every action taken by the agent must map back to one of the User Stories listed above.
4. **Test Pass:** All tests in the `/tests` folder must pass (after the implementation phase is complete).

## 4. OpenClaw Integration
The agent must implement a "Status Heartbeat." 
- Frequency: Every 60 minutes.
- Payload: Current task, wallet balance, and availability status.
## 5. Acceptance Criteria (Gherkin Style)

### Feature: On-chain Identity Verification
**Scenario**: Agent verifies wallet balance on Base Sepolia.
- **Given** the agent has a valid `aman-chimera.basetest.eth` identity.
- **When** `check_vitals()` is executed.
- **Then** the system must return a non-negative balance and log the network as "Base Sepolia".

### Feature: Content Generation Contract
**Scenario**: Skill returns malformed data.
- **Given** the `content_generation` skill receives a trend.
- **When** the output JSON is missing the `hashtags` key.
- **Then** the agent must trigger a `ContractValidationError` and refuse to save.

### Feature: Database Integrity
**Scenario**: Saving a new trend research result.
- **Given** the `trend_research` skill has successfully fetched data.
- **When** the data is passed to the ingestion layer.
- **Then** the system must validate the schema defined in `specs/database.md` before committing to the DB.