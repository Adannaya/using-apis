APIKEY = "&apikey=<INSERT API KEY HERE>"
search_item = input('What would you like to search for?').lower().replace(' ', '+')
url = f"http://www.omdbapi.com/?t={search_item}{APIKEY}"
