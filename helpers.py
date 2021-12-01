import requests
import pathlib
import sys


def run(day, f):
    test_inp = get_test_input(day)
    if test_inp is not None:
        print('--- with test input ---')
        f(test_inp)
    else:
        print('test-inputs/day{:02}.txt file is not present'.format(day))
    print('--- with real input ---')
    inp = get_input(day)
    f(inp)


def run_with_test_input(f):
    try:
        with open('input.txt') as f:
            test_input = f.read()
    except FileNotFoundError:
        print('input.txt does not exist')
        sys.exit(1)
    f(test_input)


def get_input(day):
    cached = get_cached_input(day)
    if cached is not None:
        return cached
    print('input is not cached, retrieving from adventofcode.com')
    token = get_token()
    inp = request_input(day, token)
    cache_input(day, inp)
    return inp


def get_token():
    try:
        with open('token.txt') as f:
            return f.read().strip()
    except FileNotFoundError:
        print('token.txt file does not exist')
        sys.exit(1)


def get_cached_input(day):
    filename = 'inputs/day{:02}.txt'.format(day)
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return None


def get_test_input(day):
    filename = 'test-inputs/day{:02}.txt'.format(day)
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return None


def cache_input(day, text):
    pathlib.Path('inputs').mkdir(parents = True, exist_ok = True)
    filename = 'inputs/day{:02}.txt'.format(day)
    with open(filename, 'w') as f:
        f.write(text)


def request_input(day, token):
    url = 'https://adventofcode.com/2021/day/{}/input'.format(day)
    headers = {
        'cookie': 'session={}'.format(token),
    }
    response = requests.get(url, headers = headers)
    return response.content.decode('utf-8')
