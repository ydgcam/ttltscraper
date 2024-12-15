# ttltscraper

A localized personal web tool for preserving your TikTok Community!

###### Scrapes your TikTok following list for linktree links and exports them into different file formats.
- Aimed to allow users to take their current following list and have a resource to where they can find the community they have built on TikTok so far on other apps in preparation for the impeding [TikTok Ban](https://en.wikipedia.org/wiki/Restrictions_on_TikTok_in_the_United_States)

## More should be seen to come from this...

#### Support Me! 

##### If you'd like to join the effort to make this a more useful tool. Contact Me!
1. Discord: ydgcam
2. Email me: cadenceann817@gmail.com

## Ideas I currently have for the future:

1. a UI/UX experience that will allow you to subscribe/follow/etc users you follow on TikTok directly from the 
app on other platforms using the APIs of the apps involved 

2. Hosting this on a publically accessible IP to utilize this as a web based tool. 
    1. Oauth authentication service that will allow users to sign in through TikTok as the primary way to be able to interact with the app and consume all of it's features.

# Supported OS environments:
1. Linux: (I'm using Ubuntu 24.04.1 LTS)
2. Windows (w/(WSL/Ubuntu)): Windows default Ubuntu distribution should be compatible although this is untested.
3. MacOS: (With a Homebrew installation, you should be able to set up a python3 virtual environment pretty easily.)

# Setup

*** IMPORTANT ***

In order to make use of this application please follow these steps first:

1. Go to tiktok.com and navigate to `More > Settings > Privacy`
2. Under Privacy find: `Data > Download your data > Download TikTok data`
3. Select All Data and JSON. 
4. Download the .zip file and have the unzipped contents handy for use when running this tool. the unzipped contents should be a `.json` file

## Setup Steps (Linux) 
1. Run `python3 -m venv .` if this is a fresh clone
2. Run `source ./bin/active` in the root of the project
3. Run `pip install -r requirements.txt` to install dependencies
4. Run `python3 ./db/initDb.py` to set up sqlite3
5. Run `python3 ./db/importData.py $YOUR_TIKTOK_DATA_HERE.json` to import your user info

## (Optional) Setup with my shell script.
1. Optionally: use the `setup.sh` file to do all of this for you! (`./setup.sh`)