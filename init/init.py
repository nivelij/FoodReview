import mysql.connector as mariadb
import requests
import json

headers = {'Content-Type': 'application/json'}
url = 'http://localhost:9200/foodreview/'

def get_connection():
    c = mariadb.connect(user='foodusr', host='localhost', port='3306', password='foodpwd', database='foodreviewdb')

    if c.is_connected():
        return c
    else:
        raise Exception('Unable to connect to database')


def readall():
    sqlstr = 'SELECT * FROM foods'

    try:
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(sqlstr)
        l = cursor.fetchall()
        resp = []

        for d in l:
            resp.append({
                'id': d[0],
                'food': d[1],
                'description': d[2],
                'date_added': d[3].strftime('%Y-%m-%d'),
            })

        return resp
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        db.close()

def init_elastic_index():
    idx = {
        'settings': {
            'index': {
                'number_of_shards':1,
                'number_of_replicas':1
            }
        }
    }

    props = {
        'properties': {
            'id': {'type': 'text'},
            'food': {'type':'text','analyzer': 'english'},
            'description': {'type': 'text', 'analyzer': 'english'},
            'date_added': {'type': 'date'}
        }
    }

    # Create food review index
    r = requests.put(url, headers=headers, data=json.dumps(idx))

    if r.ok:
        r = requests.put(url + '_mapping/', headers=headers, data=json.dumps(props))

    return r.ok

def main():
    init_elastic_index()
    r = readall()

    for x in r:
        r = requests.post(url + '_doc/', headers=headers, data=json.dumps(x))
        print(r.text)


if __name__ == '__main__':
    main()