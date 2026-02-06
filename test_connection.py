import os
import asyncio
# In v2, we import CdpClient, not Cdp or Wallet
from cdp import CdpClient

# 1. Credentials
key_id = "925569d8-38b5-4399-9150-fcc42168671e"
key_secret = "imdh9FeRV4G2cSEnU9gRw+1SMR42t7WThf6BQHxTgn0/HDEWFIoEb1vBoW+q8I3SmQXkrJCVSgI/ZSroG0CQLw=="

async def main():
    print("--- 🔗 Chimera Core Link (V2 SDK) ---")
    
    try:
        # Step 1: Initialize the V2 Client
        # We pass the credentials directly into the client
        async with CdpClient(
            api_key_id=key_id,
            api_key_secret=key_secret,
            wallet_secret="Chimera_Secret_Pass_2026"
        ) as cdp:
            print("✅ V2 Client Connected.")

            # Step 2: Create a Server-Managed Account
            # In V2, wallets are accessed via the 'evm' or 'solana' property
            print("🔄 Creating EVM Account on Base Sepolia...")
            account = await cdp.evm.create_account()
            
            print(f"\n🚀 CHIMERA IS ONLINE!")
            print(f"📍 Wallet Address: {account.address}")
            
            # Step 3: Optional - Request some test funds to prove it's live
            print("💧 Requesting testnet ETH from faucet...")
            await cdp.evm.request_faucet(
                address=account.address,
                network="base-sepolia",
                token="eth"
            )
            print("✅ Faucet request sent! Check BaseScan shortly.")

    except Exception as e:
        print(f"❌ CONNECTION FAILED: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())