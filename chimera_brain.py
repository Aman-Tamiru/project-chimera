import os
from dotenv import load_dotenv
from web3 import Web3
import time

# Load variables from your .env file
load_dotenv()

# 1. Connect to the Base Sepolia "Network"
RPC_URL = "https://sepolia.base.org"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# 2. Chimera's Credentials (FETCHED SECURELY)
CHIMERA_ADDRESS = "0x932f455DdC368B273668fABeb505A893Cb6157c3"
PRIVATE_KEY = os.getenv("CHIMERA_PRIVATE_KEY") 

# Security Guardrail: Stop the script if the key is missing
if not PRIVATE_KEY:
    raise ValueError("SECURITY ALERT: Private Key missing! Ensure CHIMERA_PRIVATE_KEY is in your .env file.")

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