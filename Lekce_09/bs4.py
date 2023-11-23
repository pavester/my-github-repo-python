from pip._vendor import requests
import bs4 

adresa = "https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana"

print(dir(requests))

odpoved = requests.get(adresa)
print(odpoved.text)