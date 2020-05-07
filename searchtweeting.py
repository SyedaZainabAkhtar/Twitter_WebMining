from searchtweets import load_credentials

#premium_search_args = load_credentials("twitter_keys_fullarchive.yaml",
#                                       yaml_key="search_tweets_api",
#                                       env_overwrite=False)
#print(premium_search_args)

from searchtweets import gen_rule_payload

rule = gen_rule_payload("from:luca", 
                        results_per_call=100#,
                        #from_date="2019-10-25 07:15",
                        #to_date="2019-11-04 23:11"
                       )