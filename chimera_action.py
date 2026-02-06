import os
from coinbase_agentkit import (
    AgentKit,
    AgentKitConfig,
    CdpWalletProvider,
    CdpWalletProviderConfig,
    basename_action_provider
)

# 1. Setup Wallet Provider (Using the address we funded!)
# Note: In a real agent, we'd use your Private Key to sign.
# For now, we'll initialize AgentKit to see what it can do.
wallet_provider = CdpWalletProvider(CdpWalletProviderConfig(
    api_key_name=os.getenv("CDP_API_KEY_NAME"), # You'll get these in the next step
    api_key_private=os.getenv("CDP_API_KEY_PRIVATE_KEY"),
    network_id="base-sepolia"
))

# 2. Initialize AgentKit with the "Basename" skill
agent_kit = AgentKit(AgentKitConfig(
    wallet_provider=wallet_provider,
    action_providers=[basename_action_provider()]
))

print("🛠️ Chimera Skill Unlocked: Basename Registration")