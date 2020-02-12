import argparse


def print_error(message):
    print(f'ERROR: {message}!!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('message', nargs='+')

    args = parser.parse_args()
    message = ' '.join(args.message)

    print('Welcome to my program')
    print_error(message)
