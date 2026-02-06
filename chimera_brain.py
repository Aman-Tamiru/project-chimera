from web3 import Web3
import time

# 1. Connect to the Base Sepolia "Network"
RPC_URL = "https://sepolia.base.org"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# 2. Chimera's Credentials
CHIMERA_ADDRESS = "0x932f455DdC368B273668fABeb505A893Cb6157c3"
# Keep this safe! 
PRIVATE_KEY = "0xbdf4...your_full_key_here..." 

def check_vitals():
    balance = w3.eth.get_balance(CHIMERA_ADDRESS)
    eth_balance = w3.from_wei(balance, 'ether')
    print(f"--- 🤖 CHIMERA CORE VITALS ---")
    print(f"📍 Address: {CHIMERA_ADDRESS}")
    print(f"🔋 Fuel: {eth_balance} ETH")
    print(f"🌐 Network: Base Sepolia")
    return eth_balance

if __name__ == "__main__":
    vitals = check_vitals()
    if vitals > 0:
        print("\n✅ CORE ONLINE: Chimera is ready for instructions.")
    else:
        print("\n⚠️ ERROR: System underfunded.")