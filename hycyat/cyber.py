import requests
import time

def hicyatat(url, sleep):
  proxy = {
    'http':'socks5://127.0.0.1:9050',
    'https':'socks5://127.0.0.1:9050'
  }
  r = requests.get(url,proxies=proxy)
  sleep(sleep)

def hicyateval(code):
  eval("async def eval_expr():\n",code)
