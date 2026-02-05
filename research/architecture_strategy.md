# Architecture Strategy – Project Chimera

## Agent Pattern
Chosen pattern: Planner–Worker–Judge (Hierarchical Swarm)
Reason:
- Scalability
- Safety
- Clear responsibility separation

## Human-in-the-Loop (HITL)
Human approval happens when:
- Low confidence content
- Sensitive topics
- Financial transactions over limits

## Database Choice
- SQL (Postgres): metadata, campaigns, logs
- Vector DB (Weaviate): memory, persona, context
