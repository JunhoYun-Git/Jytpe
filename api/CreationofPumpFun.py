import requests
import subprocess
import json

# Solana Token Configuration
SOLANA_KEYPAIR_PATH = "/path/to/your/solana/keypair.json"  # Path to your Solana wallet keypair file
TOKEN_NAME = "Jytpe the Destroyer of Agents"
TOKEN_TICKER = "Jytpe"
TWITTER_ACCOUNT = "https://x.com/JypteAgent"
WEBSITE = "https://github.com/JunhoYun-Git/Jytpe"

# Pump.fun API base URL (replace with actual base URL of the Pump.fun API)
PUMP_FUN_API_URL = "https://api.pump.fun"  # Replace with real API URL
PUMP_FUN_API_KEY = "your-api-key"  # API key for authentication

# Create the Token on Solana using Solana CLI
def create_token_on_solana():
    # Set Solana configuration
    subprocess.run(["solana", "config", "set", "--keypair", SOLANA_KEYPAIR_PATH])
    
    # Create a new token using `spl-token`
    create_token_result = subprocess.run(["spl-token", "create-token"], capture_output=True, text=True)
    token_address = create_token_result.stdout.split("Token Address: ")[1].split("\n")[0]
    print(f"Token Address: {token_address}")
    
    # Create an account to hold the token
    subprocess.run(["spl-token", "create-account", token_address])
    
    # Mint tokens to the account
    subprocess.run(["spl-token", "mint", token_address, str(TOKEN_SUPPLY)])
    
    # Return the token address for further use
    return token_address

# Register the Token with Pump.fun API
def register_token_with_pump_fun(token_address):
    # Define the payload for token registration
    payload = {
        "token_name": TOKEN_NAME,
        "ticker": TOKEN_TICKER,
        "token_address": token_address,
        "initial_supply": TOKEN_SUPPLY,
        "creator_wallet": SOLANA_KEYPAIR_PATH,
    }

    # Set headers with API Key for authentication
    headers = {
        "Authorization": f"Bearer {PUMP_FUN_API_KEY}",
        "Content-Type": "application/json",
    }

    # Send a POST request to register the token
    response = requests.post(f"{PUMP_FUN_API_URL}/create-token", json=payload, headers=headers)
    
    # Check the response status
    if response.status_code == 200:
        print("Token successfully registered with Pump.fun!")
        print(f"Token details: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Failed to register token with Pump.fun. Error: {response.text}")

def main():
    # Step 1: Create token on Solana
    token_address = create_token_on_solana()
    
    # Step 2: Register the token with Pump.fun
    register_token_with_pump_fun(token_address)

if __name__ == "__main__":
    main()
