## Overview

These python scripts let a user interact with their spotify profile and listening data using the console on [Spotify for Developers](https://developer.spotify.com/). Further development opportunities are available, these are just the ones I found to be most interesting. Each requires users to log into their spotify account on [Spotify for Developers](https://developer.spotify.com/) to generate an authorization token.

## Setup

Some sort of platform or IDE that supports python will be required - I am currently using VS Code. Clone this repo.

I recommend creating and activating a virtual environment.

Install the necessary libraries (or library) by running *pip install -r requirements.txt* in the terminal.

## Playback

The file, *playback.py* allows a user to interact with an active Spotify device. This includes playing, pausing, skipping, and going to a previous song. 

In order to interact your Spotify, you need an authorization token which can be generated [here](https://developer.spotify.com/console/get-users-available-devices/) by scrolling down and clicking the green *GET TOKEN* button, selecting the default *user-read-playback-state* option as well as the *user-modify-playback-state* option, and clicking *REQUEST TOKEN*. The token can then be copied - it should be somewhere around 100-200 characters long and will last approximately 30 minutes before expiring.

Running this file allows a user to play, pause, skip a song, or go back to the previous song. An argument will be passed to determine which action will be taken - "play" to play, "pause" to pause, "next" to skip to the next song, or "previous" to go back the the previous song. The default action is pause.

Once you have an authorization token, run *playback.py* using the token as the first command line argument and the desired action as the second command line argument. The general format is: python playback.py [YOUR TOKEN HERE] [ACTION HERE]

example: *python playback.py abcdefghijklmnopqrstuvwxyz1234567890987654321 pause*

This will complete the desired action if there is an active device for the account that generated the authorization token.

## Data Generation

The file, *generatedata.py* allows a user to access data on their top Spotify tracks and artists over different periods of time. 

In order to generate your Spotify data, you need an authorization token which can be generated [here](https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/) by scrolling down and clicking the green *GET TOKEN* button, selecting the default *user-top-read* option, and clicking *REQUEST TOKEN*. The token can then be copied - it should be somewhere around 100-200 characters long and will last approximately 30 minutes before expiring.

Once you have an authorization token, run *generatedata.py* using the token as the first command line argument and an output file name as the second command line argument (optional). The general format is: python generatedata.py [YOUR TOKEN HERE] [OUTPUT FILE NAME HERE]

example: *python generatedata.py abcdefghijklmnopqrstuvwxyz1234567890987654321 myspotifydata*

This will generate a text file with the name provided that includes the user's top 50 artists and tracks of the past month, 6 months, and all time.