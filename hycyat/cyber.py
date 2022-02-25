import requests
import time

def hicyat.at(url, sleep):
  proxy = {
    'http':'socks5://127.0.0.1:9050',
    'https':'socks5://127.0.0.1:9050'
  }
  r = requests.get(url,proxies=proxy)
  sleep(sleep)

def hicyat.eval(code):
  eval("async def eval_expr():\n",code)
