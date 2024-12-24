import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Charger les clés API depuis le fichier .env
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Configurer le client Tweepy pour l'API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Fonction pour collecter des tweets
def collect_tweets_v2(query, max_tweets=100):
    tweets_data = []
    response = client.search_recent_tweets(
        query=query, 
        max_results=100,  # Limitation par requête de l'API v2
        tweet_fields=["created_at", "author_id", "public_metrics", "text"],
        expansions=["author_id"]
    )
    # Traiter les tweets récupérés
    if response.data:
        for tweet in response.data:
            tweets_data.append({
                'Date': tweet.created_at,
                'Utilisateur': tweet.author_id,  # Nécessite des requêtes supplémentaires pour le nom
                'Texte': tweet.text,
                'Likes': tweet.public_metrics["like_count"],
                'Retweets': tweet.public_metrics["retweet_count"]
            })
    return pd.DataFrame(tweets_data)

# Récupérer les tweets sur un mot-clé
mot_cle = "marketing"
nombre_de_tweets = 100  # Ajusté selon les limites
tweets = collect_tweets_v2(mot_cle, nombre_de_tweets)

# Chemin de sauvegarde pour les tweets bruts
output_path = 'data/tweets_marketing_raw.csv'
tweets.to_csv(output_path, index=False)
print(f"Tweets collectés et sauvegardés dans '{output_path}'")
