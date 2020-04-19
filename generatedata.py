import requests
import os
import json
import sys


timeKey = {'long_term': "all time", 'medium_term': "the past 6 months", 'short_term': "the past month", None: "the past 6 months"}


def getHeaders(oAuth):
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + oAuth,
    }
    return headers

def getTop(category, time, limit, offset, oAuth, fileName):
    url = 'https://api.spotify.com/v1/me/top/' + category
    args = False
    if time:
        url +=  '?time_range=' + time
        args = True
    if limit:
        if not args:
            url += '?'
            args = True
        else:
            url += '&'
        url += 'limit=' + limit
    if offset:
        if not args:
            url += '?'
            args = True
        else:
            url += '&'
        url += 'offset=' + offset
    else:
        offset = 0
    response = requests.get(url=url, headers=getHeaders(oAuth))
    items = json.loads(response.content)
    with open(fileName, 'a') as f:
        f.write("Your top " + category + " of " + timeKey[time] + ":\n")
        for index, item in enumerate(items['items']):
            if category == "tracks":
                f.write(str(index + int(offset) + 1) + '. ' + item['name'] + ' by ' + item['artists'][0]['name'] + '\n')
            else:
                f.write(str(index + int(offset) + 1) + '. ' + item['name'] + '\n')
        f.write('\n')

def generateAll(auth, fileName):
    for category in ['artists', 'tracks']:
        for time in ['short_term', 'medium_term', 'long_term']:
            getTop(category, time, '50', '0', auth, fileName)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Error: Include authorization token in command line arguments.")
    auth = sys.argv[1]
    fileName = 'spotifydata.txt'
    if len(sys.argv) > 2:
        fileName = sys.argv[2] + '.txt'
    if fileName in os.listdir():
        os.remove(fileName)

    generateAll(auth, fileName)
