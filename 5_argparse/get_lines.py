import argparse


def count_lines(name):
    try:
        with open(name) as f:
            lines = f.readlines()
        return len(lines)
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='', required=True)

    args = parser.parse_args()
    print(count_lines(args.file))
