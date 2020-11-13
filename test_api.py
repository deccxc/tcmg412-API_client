import yaml
import argparse
import requests


parser = argparse.ArgumentParser(description='Test the functions of the API')
parser.add_argument('-d', '--destination', metavar='', help='specify an external url')
parser.add_argument('-f', '--file', metavar='', required=True, help='specify a YAML file')
args = parser.parse_args()

def get_basic(operation):    
    if args.destination is None:
        url = 'http://localhost:5000/{}'.format(operation)
    else:
        url = 'http://{}/{}'.format(args.destination, operation)
    r = requests.get(url)
    return r.status_code

def crud_requests(operation, request_type, kv_key, kv_val):
    if args.destination is None:
        dest = 'localhost:5000' 
    else:
        dest = args.destination
    if request_type == 'POST':
        url = 'http://{}/{}'.format(dest, operation)
        r = requests.post(url, json={'key':kv_key, 'value':kv_val})        
    elif request_type == 'PUT':
        url = 'http://{}/{}'.format(dest, operation)
        r = requests.put(url, json={'key':kv_key, 'value':kv_val})
    elif request_type == 'DELETE':
        url = 'http://{}/{}'.format(dest, operation)
        r = requests.delete(url)
    elif request_type == 'GET':
        url = 'http://{}/{}'.format(dest, operation)
        r = requests.get(url)    
    return r.status_code

if __name__ == '__main__':
    with  open(args.file, 'r') as tests:
        testObject = yaml.full_load(tests)

        for item in testObject:      
            actualCode = item['status_codes']      

            if item['method'] == 'GET':
                resultedCode = get_basic(item['url'])
            else: 
                resultedCode = crud_requests(item['url'], item['method'], item['kv_key'], item['kv_val'])

            if resultedCode not in actualCode:
                print(item)
                print('This request does not return the expected result')
            else:
                print('All tests passed)
            
                
            




        
