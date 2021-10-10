import tweepy

creds = {
    "consumer_key": "0Ex34lGWEnplcisTVzfZV5nOv",
    "consumer_secret": "wcIasfkl8W8p4Haw3gvQpywKDdftKslRUf9okALfgTPjpf9hp9",
    "access_token": "1459501699-7yL7Yyq9TgjIQvgomwxT0ey73LSR1zNGy1MgCWV",
    "access_token_secret": "j7B1WczL0dExfO9ondn4Z61fn7hviNhTVqiZZD58VgUvS",
}

auth = tweepy.OAuthHandler(creds["consumer_key"], creds["consumer_secret"])
auth.set_access_token(creds["access_token"], creds["access_token_secret"])
api = tweepy.API(auth)
api.update_status("My_Bot_Message")

# bearer-token: AAAAAAAAAAAAAAAAAAAAAMXdUQEAAAAAekDLGTH2Nq55TzupcTlWeq4rGZU%3DZ7DvavQ1noNxWT7fW6aRTpzfOzSfVz7AFvxszXUj9MBhDa3uYj
