#!/usr/bin/env python
import requests
import random

def check_name(API_KEY, name):
    name = name.strip()
    req = requests.get("https://xboxapi.com/v2/xuid/" + name, headers={"X-AUTH":API_KEY})
    status = req.status_code
    if status == 200:
        return False#not avail
    elif status == 404:
        return True#user not found - avail
    else:
        print "Status code " + str(status) + " was returned. This is unexpected."

def gen_name():
    adjective = random_line('wsgi/adj.txt').strip()
    noun = random_line('wsgi/noun.txt').strip().title().replace(' ','')
    return adjective + noun

def random_line(filename):
    line = "#"
    while line.startswith('#'):
        line = random.choice(list(open(filename)))
    return line
