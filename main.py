import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ["SLACK_API_TOKEN"])


@app.command("/nuke")
def nuke_it(ack, body):
    user_id = body["user_id"]
    user_name = body["user_name"]
    channel_name = body["channel_name"]
    ack(f"Deleting messages for <@{user_id}> in channel <{channel_name}> :nuke:")
    response = app.client.search_messages(query=f"in:#{channel_name} from:{user_name}", count=100)
    matches = response.get('messages')
#   need to add in paging
    while matches['total'] > 0:
        for match in matches['matches']:
            timestamp = match.get('ts')
            channel = match.get('channel')['id']
            app.client.chat_delete(channel=channel, ts=timestamp)
        response = app.client.search_messages(query=f"in:<#{channel_name}> from:<{user_id}>", count=100)
        matches = response.get('messages')


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
