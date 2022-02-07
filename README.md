# slack-nuker
Python bot that deletes your slack messages from the current channel. Uses Slack Bolt and socket mode to listen for the /nuke command.

## Instructions for configuration
1. Create a Slack app using socket mode, with the following permissions
    1.  chat:write
    2.  files:write
    3.  search:read
2. Create slash command /nuke for the app
3. Copy the API and APP tokens, and paste in the corresponding config vars when deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Usage
1. /nuke : deletes all of your messages in the current channel
