import sys
import requests

#print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    test = "test"
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting 

r = requests.get('http://coreyms.com')
print(r.status_code)
print('hello')