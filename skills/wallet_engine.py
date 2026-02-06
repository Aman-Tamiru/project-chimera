import os
from dotenv import load_dotenv
# ... other imports like from cdp import Wallet ...

# 1. Load the secrets immediately
load_dotenv()

# 2. Assign variables
api_key_name = os.getenv("CDP_API_KEY_NAME")
api_key_private_key = os.getenv("CDP_API_KEY_PRIVATE_KEY")
network_id = os.getenv("NETWORK_ID", "base-sepolia")

# 3. Your existing wallet logic follows...
def initialize_wallet():
    # Use the variables here
    pass