from elasticsearch import Elasticsearch

def es_connect():
    es = Elasticsearch([{'host':'localhost', 'port':9200}])
    return es

def save_json(es, json):
    res = es.index(index="wiki", doc_type="change", body=json)
    return res['result']