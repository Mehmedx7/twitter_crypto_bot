from src.twitter_service import get_latest_tweet
from src.llm_service import extract_solana_address
from src.transaction_service import get_jupiter_quote, create_transaction, send_transaction
from solana.keypair import Keypair
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    username = "elonmusk"
    latest_tweet = get_latest_tweet(username)

    if latest_tweet:
        print(f"Latest tweet from @{username}: {latest_tweet}")
        solana_address = extract_solana_address(latest_tweet)

        if solana_address:
            input_mint = "So11111111111111111111111111111111111111112"
            output_mint = solana_address 
            amount = 1000000000

            quote = get_jupiter_quote(input_mint, output_mint, amount)
            if quote:
                wallet_private_key = os.getenv("WALLET_PRIVATE_KEY")
                wallet_keypair = Keypair.from_secret_key(bytes.fromhex(wallet_private_key))

                transaction = create_transaction(quote, wallet_keypair)
                if transaction:
                    tx_signature = send_transaction(transaction, wallet_keypair)
                    if tx_signature:
                        print(f"Transaction sent. Signature: {tx_signature}")
                    else:
                        print("Failed to send transaction.")
                else:
                    print("Failed to create transaction.")
            else:
                print("Failed to fetch quote from Jupiter.")
        else:
            print("No Solana token contract address found in the tweet.")
    else:
        print(f"No tweets found for @{username} or an error occurred.")

if __name__ == "__main__":
    main()