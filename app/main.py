import requests
import json

url = 'http://localhost:9200/foodreview/'
headers = {'Content-Type': 'application/json'}

def main():
    print('# SEARCH ENGINE SIMULATION #')

    while True:
        print('Hello! Type some food keyword you have in mind:')
        keyword = input()
        i = {
            'query': {
                'multi_match' : {
                    'query' : keyword,
                    "fields": ["food", "description"],
                    "fuzziness": "AUTO"
                }
            },
        }

        r = requests.get(url + '_search/', headers=headers, data=json.dumps(i)).json()
        time_taken = r['took']
        hits = r['hits']['hits']

        print('=====================================')
        print('RESULTS')
        print('=====================================')
        for h in hits:
            print('%s - [SCORE %s]' % (h['_source']['food'], round(h['_score'], 2)))
            print(h['_source']['description'])
            print('=====================================')

        print('Retrieved in %s ms' % time_taken)
        print('\n')

if __name__ == '__main__':
    main()