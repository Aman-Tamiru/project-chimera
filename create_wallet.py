from eth_account import Account
import secrets

print("--- 🔗 Chimera Independent Wallet ---")

# 1. Generate a secure private key without any SDK bugs
priv_key = "0x" + secrets.token_hex(32)
account = Account.from_key(priv_key)

print(f"✅ SUCCESS: Chimera Wallet Created!")
print(f"📍 Address: {account.address}")
print(f"🔑 Private Key: {priv_key} (SAVE THIS SOMEWHERE SECRET!)")
print(f"🔗 View on BaseScan: https://sepolia.basescan.org/address/{account.address}")

# Save it to a file so we never have to do this again
with open("chimera_wallet.txt", "w") as f:
    f.write(f"Address: {account.address}\nPrivate Key: {priv_key}")