import requests
from bs4 import BeautifulSoup

# Making a GET request; I have 10 links
links = [
'https://www.reddit.com/r/technews',
'https://www.reddit.com/r/savedyouaclick/',
'https://www.reddit.com/r/news/',
'https://www.reddit.com/r/nottheonion/',
'https://www.reddit.com/r/science/',
'https://www.reddit.com/r/technology/',
'https://www.reddit.com/r/worldnews/',
'https://www.reddit.com/r/offbeat/',
'https://www.reddit.com/r/gamernews/',
'https://www.reddit.com/r/UpliftingNews/'
]
for url in links:
	r = requests.get(url)

	# Parsing the HTML Parsing=Analizowanie
	soup = BeautifulSoup(r.content, 'html.parser')

	# Finding by id
	s = soup.find('div', class_ ='rpBJOHq2PR60pnwJlUyP0')
	if s is not None:
		print('Znalazłem')
	# find all the anchor tags with "href"
		for link in s.find_all('a'):

			var = link.get('href')
			if var is not None and 'https' in var:
				print(var)	
	else:
		print('Nic nie znalazłem')
		
			

