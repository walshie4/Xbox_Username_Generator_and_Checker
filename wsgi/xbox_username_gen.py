#!/usr/bin/env python
import requests

def check_name(API_KEY, name):
    name = name.strip()
    req = requests.get("https://xboxapi.com/v2/xuid/" + name, headers={"X-AUTH":API_KEY})
    status = req.status_code
    if status == 200:
        return False#not avail
    elif status == 404:
        return True#user not found
    else:
        print "Status code " + status + " was returned. This is unexpected."

