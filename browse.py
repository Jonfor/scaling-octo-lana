import requests
import json
import time
from pprint import pprint
import getpass
 
#----------------------------------------------------------------------
def login(username, password):
    """logs into reddit, saves cookie"""
 
    print 'Begin login'
    #username and password
    UP = {'user': username, 'passwd': password, 'api_type': 'json',}
    headers = {'user-agent': '/u/Chaosruiner\'s API python bot', }
    #POST with user/pwd
    client = requests.session()
    client.headers = headers
    r = client.post('http://www.reddit.com/api/login', data = UP)

    # Print out error codes on attempting login
    j = json.loads(r._content)
    for jsons, userData in j.iteritems():
        print userData.pop(u'errors')
        break

    client.user = username
    def name():
        return '{}\'s client'.format(username)

    #grabs the modhash from the response
    client.modhash = j['json']['data']['modhash']

    return client

def usersubreddit(client, limit, return_json = True, **kwargs):

    parameters = {'limit': limit,}
    parameters.update(kwargs)
    url = r'http://www.reddit.com/subreddits/mine/subscriber.json'
    r = client.get(url)
    j = json.loads(r.text)

    if return_json:
        return j
    else:
        stories = []
        for story in j['data']['children']:
            #print story['data']['title']
            stories.append(story)
        return stories
        


def main():
    print 'Please enter your username'
    username = raw_input("-->")
    password = getpass.getpass()
    client = login(username, password)
    j = usersubreddit(client, limit = 10)
    pprint(j)
if  __name__ =='__main__':main()





