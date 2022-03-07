import requests
import time

def hicyatat(url, sleep):
  r = requests.get(url)
  sleep(sleep)
