import openai
import re
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def is_valid_solana_address(address):
    solana_regex = r"^[1-9A-HJ-NP-Za-km-z]{32,44}$"
    return re.match(solana_regex, address) is not None

def extract_solana_address(tweet):
    try:
        prompt = (
            f"Extract the Solana token contract address from the following tweet. "
            f"Solana addresses are base58-encoded and typically 32-44 characters long. "
            f"If no Solana wallet address is found, return 'None'. "
            f"Tweet: {tweet}"
        )

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts Solana token contract addresses from tweets."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=50,
            temperature=0.3,
        )

        llm_response = response.choices[0].message["content"].strip()

        if is_valid_solana_address(llm_response):
            return llm_response
        else:
            return None
    except Exception as e:
        print(f"An error occurred while calling the LLM: {e}")
        return None