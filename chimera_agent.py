from eth_account import Account
from coinbase_agentkit import (
    EthAccountWalletProvider,
    EthAccountWalletProviderConfig,
    basename_action_provider
)

# 1. Your Wallet (0xC8C5...)
# Paste that key you found: 0b837492fa46c516df83e0d8ec3f32531ec10a7ff41a3ef7496a238da95d1cb4
MY_PRIVATE_KEY = "0b837492fa46c516df83e0d8ec3f32531ec10a7ff41a3ef7496a238da95d1cb4".strip()
# 2. Setup
local_account = Account.from_key(MY_PRIVATE_KEY)
wallet_provider = EthAccountWalletProvider(EthAccountWalletProviderConfig(
    account=local_account,
    chain_id="84532"  # Base Sepolia
))
base_provider = basename_action_provider()

# 3. The Registration (10+ chars = CHEAP)
# We use 'aman-chimera' (12 chars) to ensure it costs only 0.0001 ETH
NAME = "aman-chimera.basetest.eth"

print(f"🚀 PROJECT CHIMERA: GO!")
print(f"📍 Wallet: {wallet_provider.get_address()}")
print(f"📝 Registering: {NAME}...")

try:
    # duration in seconds (1 year = 31536000)
    params = {"basename": NAME, "amount": 31536000}
    result = base_provider.register_basename(wallet_provider, params)
    
    print("\n✅ REGISTRATION COMPLETE!")
    print(f"🔗 View on Basescan: https://sepolia.basescan.org/address/{wallet_provider.get_address()}")
    print("-" * 30)
    print(f"AGENT IDENTITY: {NAME}")
    print("-" * 30)

except Exception as e:
    print(f"\n❌ FAILED: {e}")