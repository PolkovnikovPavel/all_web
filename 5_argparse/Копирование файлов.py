import argparse


def copy_file(start_file, end_file, upper, lines):
    with open(start_file, 'r') as f:
        start_text = f.read()

    if lines > len(start_text.split('\n')):
        lines = len(start_text.split('\n'))
    if lines == -1:
        lines = len(start_text.split('\n'))
    text = '\n'.join(start_text.split('\n')[:lines - 1])

    if upper:
        text = text.upper()

    with open(end_file, 'w') as fi:
        fi.write(text)
        fi.close()


parser = argparse.ArgumentParser()
parser.add_argument("source_file", nargs=1)
parser.add_argument("ended_file", nargs=1)
parser.add_argument("--upper", action='store_true')
parser.add_argument("--lines", default=-1, type=int)

args = parser.parse_args()

start_file = args.source_file
end_file = args.ended_file
upper = args.upper
lines = args.lines


copy_file(start_file[0], end_file[0], upper, lines)
