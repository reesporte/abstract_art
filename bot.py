import sys
import random
import art
import os
import config
import peepee
from mastodon import Mastodon
import datetime

def new_output():
    word = art.command(random.randint(25, 50))
    os.system(word)

def loginTOOT():
    key = config.key
    secret = config.secret
    access = config.access

    mastodon = Mastodon(
        client_id=key, client_secret=secret, access_token=access,
        api_base_url="https://botsin.space"
    )

    print("creating toot")
    new_output()
    des = peepee.gen()
    print(des)
    print("posting toot")
    x = mastodon.media_post("art.jpeg", "image/jpeg", description=des)
    mastodon.status_post(des, media_ids=x)
    with open("log", "w+") as f:
        f.write("\ndatetime: ")
        f.write(str(datetime.datetime.now()))
        f.write("\n")
        f.write("\n")
        f.write(str(x))
        f.write("\n")
        f.write("\n")
    print("done")

def LOCALTEST():
    new_output()
    des = peepee.gen()
    print(des)
    os.system("open art.jpeg")

if __name__ == '__main__':
    if sys.argv[1] == "local":
        LOCALTEST()
    elif sys.argv[1] == "full":
        loginTOOT()
