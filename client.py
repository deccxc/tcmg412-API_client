import argparse
import requests


parser = argparse.ArgumentParser(description='Run, retrieve, or execute the desired action')
parser.add_argument('operation', type=str, help='The operation you would like to execute. (md5, factorial, keyval...)')
parser.add_argument('load', help='The object you would like to be run against the operation')
parser.add_argument('-r', '--request_type', metavar='', type=str, help='Type of request to be past to API when using the \'keyval\' operation. (post, put, get, delete) default is \'get\' ')
parser.add_argument('-d', '--destination', metavar='', help='specify an external url')
args = parser.parse_args()

def get_basic(operation, load):
    load = str(load)
    if args.destination is None:
        url = 'http://localhost:5000/{}/{}'.format(operation, load)
    else:
        url = 'http://{}/{}/{}'.format(args.destination, operation, load)
    r = requests.get(url)
    return r.text

def crud_requests(operation, load):    
    if args.request_type == 'post':
        pair = load.split(':')
        key = str(pair[0])
        val = str(pair[1])
        url = 'http://localhost:5000/{}'.format(operation)
        r = requests.post(url, json={'key':key, 'value':val})        
    elif args.request_type == 'put':
        pair = load.split(':')
        key = str(pair[0])
        val = str(pair[1])
        url = 'http://localhost:5000/{}'.format(operation)
        r = requests.put(url, json={'key':key, 'value':val})
    elif args.request_type == 'delete':
        url = 'http://localhost:5000/{}/{}'.format(operation, load)
        r = requests.delete(url)
    elif args.request_type == 'get':
        url = 'http://localhost:5000/{}/{}'.format(operation, load)
        r = requests.get(url)    
    return r.text
    
if __name__ == '__main__':
    if args.request_type is None:
        print(get_basic(args.operation, args.load))
    else:
        print(crud_requests(args.operation, args.load))
