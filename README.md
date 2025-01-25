# Twitter Crypto Bot

![Application Architecture](/img/image.png)

The **Twitter Crypto Bot** is a Python-based application that monitors a specific Twitter account for new tweets and performs actions (e.g., buying cryptocurrency) based on the content of the tweets. This project is designed to demonstrate how to integrate Twitter data with cryptocurrency trading logic.

---

## Table of Contents
1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Architecture](#architecture)
4. [Installation](#installation)
5. [Usage](#usage)

---

## Features
- **Monitor Twitter Account**: Fetches the latest tweets from a specified Twitter account.
- **Crypto Trading Logic**: Analyzes tweet content and performs actions (e.g., buying cryptocurrency) based on predefined rules.
- **Error Handling**: Robust error handling and retries for network issues.
- **Free and Open Source**: Uses free tools like Nitter for tweet scraping.

---

## How It Works
1. The bot fetches the latest tweet from a specified Twitter account using **Nitter** (a privacy-friendly Twitter front-end).
2. It analyzes the tweet content for specific keywords (e.g., "buy").
3. If a keyword is detected, the bot performs an action (e.g., buying cryptocurrency) using a cryptocurrency exchange API.

---

## Architecture
The application follows a modular architecture:

![Application Architecture](/img/image.png)

---