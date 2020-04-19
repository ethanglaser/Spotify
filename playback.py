import requests
import json
import sys


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
    raise ValueError('Error: No devices currently active for this user.')

def playback(action, device, oAuth):
    url='https://api.spotify.com/v1/me/player/' + action + '?device_id='+device
    if action == 'next' or action == 'previous':
        response = requests.post(url=url, headers=getHeaders(oAuth))
    elif action == 'pause' or action == 'play':
        response = requests.put(url=url, headers=getHeaders(oAuth))
    else:
        raise ValueError('Please select a valid playback option: play, pause, next, or previous.')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Error: Include authorization token in command line arguments.")
    auth = sys.argv[1]
    action = 'pause'
    if len(sys.argv) > 2:
        action = sys.argv[2]
    
    devices = getDevices(auth)
    active = getActive(devices)
    playback(action, active, auth)