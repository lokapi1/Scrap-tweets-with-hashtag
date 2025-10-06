import tweepy

# Remplacez les valeurs ci-dessous par vos propres clés d'API Twitter
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Authentification avec les clés d'API Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Définir le hashtag à rechercher
hashtag = "#DontSayGay"

# Récupérer les tweets
tweets = tweepy.Cursor(api.search_tweets, q=hashtag, tweet_mode='extended', lang='en').items(100)

# Triez les tweets par le nombre de retweets
sorted_tweets = sorted(tweets, key=lambda x: x.retweet_count, reverse=True)

# Afficher les 100 premiers tweets triés par le nombre de retweets
for tweet in sorted_tweets[:10]:
    print(f"{tweet.full_text} - Retweets: {tweet.retweet_count}")
