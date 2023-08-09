from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

extinction_url = 'https://www.bbc.com/news/science-environment-61242789'
extinction_html = urlopen(extinction_url)
extinction_html_parse = BeautifulSoup(extinction_html, 'html.parser')

for index, element in enumerate(extinction_html_parse.find_all('body')):
  words = element.get_text()
  print(f'\nTokens in Paragraph {index + 1}: {word_tokenize(words)}')


##
##
##
##
##
#
#
#
#
#