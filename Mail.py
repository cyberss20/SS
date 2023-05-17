import requests

from bs4 import BeautifulSoup

url = 'https://mail.google.com/mail/u/0/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

email_list = []

for link in soup.find_all('a'):

    email = link.get('href')

    if email.startswith('mailto:'):

        email_list.append(email[7:])

print(email_list)
