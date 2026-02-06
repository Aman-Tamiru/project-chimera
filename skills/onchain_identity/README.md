# Skill: Onchain Identity Management

## Description
This skill allows the agent to interact with the Base Sepolia network to manage its Basename (aman-chimera.basetest.eth).

## Input Contract (JSON)
{
  "action": "register" | "verify" | "resolve",
  "name": "string"
}

## Output Contract (JSON)
{
  "status": "success" | "failed",
  "transaction_hash": "string",
  "resolved_address": "string"
}