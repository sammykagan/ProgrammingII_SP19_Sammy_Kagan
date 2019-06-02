

def my_handler(event, context): # To use AWS Lambda, all of my code has to be inside of a function. Don't worry about it.
    # 2020 Candidate Retweeter
    # @2020_democrats
    # twitter.com/2020_democrats
    # Final Project for Programming II by @realsamkagan of Francis W. Parker School

    import tweepy as tw

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    candidate_accounts = ["MichaelBennet", "JoeBiden", "CoryBooker", "GovernorBullock", "PeteButtigieg",
                          "JulianCastro", "BilldeBlasio", "JohnDelaney", "TulsiGabbard", "SenGillibrand", "MikeGravel",
                          "KamalaHarris", "Hickenlooper", "JayInslee", "amyklobuchar", "WayneMessam", "sethmoulton",
                          "BetoORourke", "TimRyan", "BernieSanders", "ericswalwell", "ewarren", "marwilliamson",
                          "AndrewYang"]
    # This list needs to be a current list of candidate accounts. Alphabetization doesn't matter.

    def retweet(candidate_account):
        info = api.user_timeline(screen_name=candidate_account, count=5, include_rts=False, include_replies=False)

        # Increase "count" to increase the number of tweets back the retweeter goes.
        tweet_count = 0
        for status in info:
            try:
                api.retweet(status.id)
            except:
                tweet_count += 1
                print("The " + str(tweet_count) + " most recent tweet from " + str(
                    candidate_account) + " has already been retweeted.")

    for i in range(len(candidate_accounts)):
        retweet(candidate_accounts[i])
