import argparse

parser = argparse.ArgumentParser(prog = 'argparse_top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
print(args.lines)
print(args.filenames)