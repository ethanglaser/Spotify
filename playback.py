import requests
import os
import json


def getHeaders(oAuth):
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + oAuth,
    }
    return headers

def getDevices(oAuth):
    url='https://api.spotify.com/v1/me/player/devices'
    response = requests.get(url=url, headers=getHeaders(oAuth))
    devices = json.loads(response.content)
    return devices

def getActive(devices):
    for value in devices['devices']:
        if value['is_active']:
            return value['id']
    return None

def playback(action, device, oAuth):
    url='https://api.spotify.com/v1/me/player/' + action + '?device_id='+device
    if action == 'next' or action == 'previous':
        response = requests.post(url=url, headers=getHeaders(oAuth))
    elif action == 'pause' or action == 'play':
        response = requests.put(url=url, headers=getHeaders(oAuth))
    else:
        response = requests.get(url='https://api.spotify.com/v1/me/player', headers=getHeaders(oAuth))
        print(response.content)
    print(response)


if __name__ == "__main__":
    devices = getDevices(auth)
    active = getActive(devices)
    playback('play', active, auth)