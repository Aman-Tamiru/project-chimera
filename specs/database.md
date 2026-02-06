# 🗄️ Chimera Data Architecture

This document defines the schema and data lifecycle for the Project Chimera agent. The agent uses a structured storage layer to maintain trajectory logs and market trend data.

---

## 🏗️ Entity Relationship Diagram (ERD)



```mermaid
erDiagram
    TRENDS ||--o{ CONTENT_LOGS : "triggers"
    CONTENT_LOGS ||--|| TRAJECTORY : "records"
    
    TRENDS {
        string keyword
        float score
        datetime detected_at
    }
    TRAJECTORY {
        uuid id
        string action_taken
        string blockchain_tx_hash
        string status
    }