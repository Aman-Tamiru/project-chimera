# Skill: Trend Research

This skill is responsible for analyzing current topics, signals, and discussions
from provided text, links, or datasets to identify emerging trends.

The agent must behave like a research analyst, not a content writer.

---

## Responsibilities

When this skill is invoked, the agent must:

1. Analyze the provided input (text, topic, or data)
2. Identify patterns, repeated themes, or rising topics
3. Extract why the trend is important
4. Classify the trend category
5. Provide structured research output

---

## Output Contract (JSON)

The agent MUST always return results in this JSON format:

{
  "trend_name": "string",
  "category": "string",
  "description": "string",
  "why_it_is_trending": "string",
  "key_signals": ["string"],
  "audience": "string",
  "opportunity": "string"
}
