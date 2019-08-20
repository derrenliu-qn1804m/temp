#Imports the request package
import requests
import unittest

class getrequest(object):
   def __init__(self):
      self.headers = {
         'User-agent' :'Mobile'
      }
      self.url ="http://172.18.58.238/headers.php"


   def get(self):
      try:
          r = requests.get(url=self , headers=self.headers ,timeout=1)
          if r.ok:
             return r
          else:
             return None
      except requests.exceptions.Timeout:
         return 'Bad Response'