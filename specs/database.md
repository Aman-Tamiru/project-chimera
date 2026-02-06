# Database Specification
## Entity Relationship Diagram (ERD)
```mermaid
erDiagram
    TREND {
        uuid id PK
        string keyword
        datetime detected_at
        string source
    }
    GENERATED_CONTENT {
        uuid id PK
        uuid trend_id FK
        text body
        string status
        datetime created_at
    }
    TREND ||--o{ GENERATED_CONTENT : triggers