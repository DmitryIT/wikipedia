import json
from sseclient import SSEClient as EventSource
from save_json import es_connect, save_json

es = es_connect()

def fetch_changes():
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'
    for event in EventSource(url):
        if event.event == 'message':
            try:
                change = json.loads(event.data)
            except ValueError:
                pass
            else:
                if change['bot'] == False:
                    res = save_json(es, change)
                    print(res)

if __name__ == '__main__':
    fetch_changes()