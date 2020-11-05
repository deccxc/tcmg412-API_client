import argparse
import requests


parser = argparse.ArgumentParser(description='Run, retrieve, or execute the desired action')
parser.add_argument('operation', type=str, help='The operation you would like to execute. (md5, factorial, keyval...)')
parser.add_argument('load', help='The object you would like to be run against the operation')
args = parser.parse_args()

def get_home(operation, load):
    load = str(load)
    url = 'http://localhost:5000/{}/{}'.format(operation, load)
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    print(get_home(args.operation, args.load))