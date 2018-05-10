import json
from sseclient import SSEClient as EventSource

def fetch_changes():
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'
    for event in EventSource(url):
        if event.event == 'message':
            try:
                change = json.loads(event.data)
            except ValueError:
                pass
            else:
                #print('bot? {bot}, {user} edited {title}'.format(**change))
                if change['bot'] == False:
                    print(json.dumps(change, indent=4))

if __name__ == '__main__':
    fetch_changes()