from html.parser import HTMLParser
from py_w3c.validators.html.validator import HTMLValidator
import urllib
import sys
import requests


url = sys.argv[1]
validator = HTMLValidator()
validator.validate(url)

if len(validator.errors):
    print('------ERRORS------\n')

for error in validator.errors:
    print(error['message'] + '\n')

if len(validator.warnings):
    print('-----WARNINGS-----\n')

for warning in validator.warnings:
    print(warning['messages'] + '\n')

# TODO - use HTMLParser to grade