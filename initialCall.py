import requests

# An API request for the cocktail margarita
url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

response = requests.get(url)
cocktail = response.json()

# Prints the name of the cocktail
print(cocktail['drinks'][0]['strDrink'])
print(cocktail['drinks'][0]['strInstructions'])