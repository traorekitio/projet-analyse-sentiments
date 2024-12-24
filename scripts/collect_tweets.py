import os
import tweepy

# Charger les clés API depuis .env
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Configurer le client Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Requête pour récupérer des tweets récents contenant un mot-clé
query = "data science"
tweets = client.search_recent_tweets(query=query, max_results=10)

# Afficher les tweets récupérés
for tweet in tweets.data:
    print(f"Tweet : {tweet.text}")
