# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nGJLTKK6ypFeTNKhIIRvMglpdOACWORz
"""

# Importing Libraries 
from bs4 import BeautifulSoup
import requests
import time

# Url of webpage so as to extract real time bitcoin value in USD 
url = 'https://www.google.com/search?q=bitcoin+price&oq=bitcoin&aqs=chrome.0.0i67i131i433i457j69i57j0i67i131i433l2j0i131i433j0i67j0i67i131i433j0i131i433.2076j0j7&sourceid=chrome&ie=UTF-8'
# request to webiste
Html = requests.get(url)
#Parsing HTML
x = BeautifulSoup(Html.text, 'html.parser')
# printing x to find where is the text which contains cryptocurrrency
print(x.prettify())

#creating function
def get_crypto_price(coin):
  # <div class="BNeawe iBp4i AP7Wnd">
  url = 'https://www.google.com/search?q='+coin+'+price&oq=bitcoin&aqs=chrome.0.0i67i131i433i457j69i57j0i67i131i433l2j0i131i433j0i67j0i67i131i433j0i131i433.2076j0j7&sourceid=chrome&ie=UTF-8'
  Html = requests.get(url)
  x = BeautifulSoup(Html.text, 'html.parser')
  # calling text that has cryptocurrrency price
  text =  x.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
  return text

price = get_crypto_price('bitcoin')

earlierprice = 0.0
g = 0
sum = 0.0
LIst = [] # making an empty list
# running an infinte loop
while True:
  cry = 'bitcoin'
  price = get_crypto_price(cry)
  g = g + 1
  value = ''
  # for converting sting to float 
  for i in price:
    if (i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '0' or i == '9' or i == '.' ):
      value = value+i
  sum = sum + float(value)
  avg_value = sum/g
  LIst.append(float(value))
# for suspening output which are similar to previous one I used if float(value) != earlierprice:
  if float(value) != earlierprice:
    print(cry+ 'price:', price)
    percent = (float(value) - earlierprice)/float(value) * 100
    #when g = 1 there is no meaning of printing percentage and rise in value
    if (g != 1): 
      print('increment percentage:', percent, '%' )
      print('Rise in value:', float(value) - earlierprice, 'United States Dollar')
    else:
      percent = 0
    
    earlierprice = float(value)
    avg_increment = (float(value) - avg_value)/float(value) *100
    print('average value:', avg_value)

    # since for finding accurate average value we should take many reading so used if g>100 so that it shall print message after getting a lot of reading
    if (g > 100): 
      print('avg_increment percentage:', avg_increment, '%' )
      print('difference between current value and average value', float(value) - avg_value)
    else:
      avg_increment = 0
    
    print('MAX:', max(LIst))
    # printing wether to buy or sell bitcoins
    if (percent>1):
      print('Sell')
    if (percent<0):
      print('Buy')
  # to suspend running for 10seconds
  time.sleep(10)





