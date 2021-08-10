from random import randint
from random import choice
import requests
from time import sleep

wait_time = 0.2
separator = ' | '

base_url = 'https://ws2.kik.com/user/'


def pad_right(string, n_chars):
    return string + (' ' * (n_chars - len(string)))


class Id:
    def __init__(self, url):
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        self.exist = not 'The page you requested was not found.' in req.text


def gen_word(words):
    words = words.split('\n')
    return choice(words)


if __name__ == '__main__':
    print( \
        f'config:\n\
        wait_time = {wait_time}\n\
        separator = {separator}\n\
        list = list.txt' \
        )
    with open('list.txt') as f:
        words = f.read()
    while True:
        url = base_url + gen_word(words)
        curr = Id(url)
        url_space = len(base_url) + 15
        url = pad_right(url, url_space)
        s = separator
        if not curr.exist:
            print(f'{url}{s}not taken')

        sleep(wait_time)