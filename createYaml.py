import yaml

config = dict(
    search_tweets_api = dict(
        account_type = 'premium',
        endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/decissionmakerdev.json',
        consumer_key = 'nDgalakt5nAglyDfCjz5Xvb8y',
        consumer_secret = 'DpQlErDlkGrUr3LR37OxAalZM7splX0ig4r1qTCsfFXoCWvlHU'
    )
)

with open('twitter_keys_fullarchive.yaml', 'w') as config_file:
    yaml.dump(config, config_file, default_flow_style=False)