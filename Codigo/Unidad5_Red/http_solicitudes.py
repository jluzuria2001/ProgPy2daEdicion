"""
imprime en el navegador:
Test
It's working if you can read this!
"""

import requests

def abrir_web():
    url = 'http://micropython.org/ks/test.html'
    html = requests.get(url).text
    print(html)


if __name__ == '__main__':
    abrir_web()