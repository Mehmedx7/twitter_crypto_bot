import requests
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.rpc.types import TxOpts

# Jupiter API endpoint
JUPITER_API_URL = "https://quote-api.jup.ag/v4/quote"

def get_jupiter_quote(input_mint, output_mint, amount):
    try:
        response = requests.get(
            JUPITER_API_URL,
            params={
                "inputMint": input_mint,
                "outputMint": output_mint,
                "amount": amount,
                "slippage": 1,  # 1% slippage
            },
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching Jupiter quote: {e}")
        return None

def create_transaction(quote, wallet_keypair):
    try:
        swap_response = requests.post(
            "https://quote-api.jup.ag/v4/swap",
            json={
                "quoteResponse": quote,
                "userPublicKey": str(wallet_keypair.public_key),
                "wrapAndUnwrapSol": True,
            },
        )
        swap_response.raise_for_status()
        swap_data = swap_response.json()

        transaction = Transaction.deserialize(bytes.fromhex(swap_data["swapTransaction"]))
        return transaction
    except Exception as e:
        print(f"Error creating transaction: {e}")
        return None

def send_transaction(transaction, wallet_keypair):
    try:
        transaction.sign(wallet_keypair)

        solana_client = Client("https://api.mainnet-beta.solana.com")
        tx_signature = solana_client.send_transaction(transaction, opts=TxOpts(skip_preflight=True))
        return tx_signature
    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None