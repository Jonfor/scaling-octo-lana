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
    client.headers=headers
    r = client.post('http://www.reddit.com/api/login', data=UP)
    client.user = username
    def name():
        return '{}\'s client'.format(username)

    return client
 
#----------------------------------------------------------------------
def subredditInfo(client, limit, sr='askreddit',
                  sorting='', return_json=False, **kwargs):
    """retrieves X (max 100) amount of stories in a subreddit
    'sorting' is whether or not the sorting of the reddit should be customized or not,
    if it is: Allowed passing params/queries such as t=hour, week, month, year or all"""
 
    #query to send
    parameters = {'limit': limit,}
    parameters.update(kwargs)
 
    url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
    r = client.get(url,params=parameters)
    print 'sent URL is', r.url
    j = json.loads(r.text)
 
    #return raw json
    if return_json:
        return j
 
    #or list of stories
    else:
        stories = []
        for story in j['data']['children']:
            stories.append(story['data']['title'])
 
        return stories


def userSubreddit(client, limit, return_json=False, **kwargs):

    parameters = {'limit': limit,}
    parameters.update(kwargs)
    url = r'http://www.reddit.com/subreddits/mine/subscriber.json'
    r = client.get(url, params=parameters)
    print r
    # j = json.loads(r.text)

    # if return_json:
    #     return j
    # else:
    #     subreddits = []
    #     for subreddit in j['data']['children']:
    #         subreddits.append(subreddit['data']['permalink'])

    #     return subreddits


def main():
    print 'Please enter your username'
    username = raw_input("-->")
    password = getpass.getpass()
    client = login(username, password)
    j = userSubreddit(client, limit=10)
    pprint(j)
if  __name__ =='__main__':main()





