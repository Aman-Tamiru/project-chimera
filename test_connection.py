import os
from coinbase_agentkit import AgentKit

# 1. Use RAW strings to prevent Python from misinterpreting the '+' or '/' symbols
key_id = "925569d8-38b5-4399-9150-fcc42168671e"
key_secret = "imdh9FeRV4G2cSEnU9gRw+1SMR42t7WThf6BQHxTgn0/HDEWFIoEb1vBoW+q8I3SmQXkrJCVSgI/ZSroG0CQLw=="

# 2. Map to the EXACT names requested by the SDK
os.environ["CDP_API_KEY_ID"] = key_id.strip()
os.environ["CDP_API_KEY_SECRET"] = key_secret.strip()
os.environ["CDP_WALLET_SECRET"] = "Chimera_Secret_2025" # Required encryption password
os.environ["NETWORK_ID"] = "base-sepolia"

def verify_agent_link():
    print("--- 🔗 Chimera Connection Audit ---")
    print(f"DEBUG: Key Secret Length is {len(os.environ['CDP_API_KEY_SECRET'])} characters.")
    
    try:
        # Initialize AgentKit
        agent_kit = AgentKit()
        
        # Fetch the Wallet Address
        address = agent_kit.wallet.default_address.address_id
        
        print(f"✅ SUCCESS: Agent is Live on Base Sepolia!")
        print(f"📍 Wallet Address: {address}")
        
    except Exception as e:
        print(f"❌ CONNECTION FAILED: {e}")

if __name__ == "__main__":
    verify_agent_link()