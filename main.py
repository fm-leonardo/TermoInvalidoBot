import json
import tweepy
import random

creds = open("./assets/credentials.json", 'r').read()
creds = json.loads(creds)

terms = open("./assets/terms.txt", 'r').read().strip().split("\n")

numin = [int(i) for i in open("./assets/numbers.txt", "r").read().strip().split("\n")]
numout = open("./assets/numbers.txt", 'w')

auth = tweepy.OAuthHandler(creds["key"], creds["key_secret"])
auth.set_access_token(creds["token"], creds["token_secret"])
api = tweepy.API(auth)

def choose_term():
    chosen_term_index = random.choice(numin)
    
    numin.pop(chosen_term_index)
    for n in numin:
        numout.write(f"{n}\n")

    return terms[chosen_term_index]

api.update_status(choose_term())
