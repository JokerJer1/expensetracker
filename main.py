import argparse



parser = argparse.ArgumentParser()

parser.add_argument('operation', choices=['add', 'multiply'])  # or whatever operations you want
parser.add_argument("numero", type=int, help="an integer number")
parser.add_argument("number", type=int, help="an integer number")

args = parser.parse_args()
if args.operation == 'add':
    result = args.numero + args.number
elif args.operation == 'multiply':
    result = args.numero * args.number

print(result)