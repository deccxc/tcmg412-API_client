
import argparse

parser = argparse.ArgumentParser(description='Return the true extent of chungs\' width')
parser.add_argument('size', type=int, metavar='', help='How big chungus should be...')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='return just basics')
group.add_argument('-v', '--verbous', action='store_true', help='return exlpanation')
args = parser.parse_args() 

def chungsize_q(size):
    result = (f'Big chungus is {size} units wide')
    return result   

def chungsize_v(size):
    result = f'You have have chosen based on educated guess that he who we call Big Chungus is {size} units wide.. this seem like a highly acurate assesment and I aplaud you.'
    return result
    
if __name__ == '__main__':
    if args.quiet:
        print (chungsize_q(args.size))
    elif args.verbous:
        print (chungsize_v(args.size))
    else:
        print(chungsize_q(args.size))