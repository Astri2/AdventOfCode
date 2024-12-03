from lxml import html
import requests
page = requests.get('https://adventofcode.com/2024/day/2')
tree = html.fromstring(page.content)
