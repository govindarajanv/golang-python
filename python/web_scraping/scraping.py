import requests
from bs4 import BeautifulSoup

URL = "https://github.com/kubernetes/kubernetes"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
releases = soup.find("span", {"class": "css-truncate css-truncate-target text-bold mr-2"})
release = releases.text.split()
print ("Available k8s release on GitHub home repo is",release[1])
