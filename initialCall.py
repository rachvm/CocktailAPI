import requests

# An API request for the cocktail margarita
url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

response = requests.get(url)
cocktail = response.json()

# Requests the details of the cocktail
drinkDetails = cocktail['drinks'][0]

name = drinkDetails['strDrink']
alcoholic = drinkDetails['strAlcoholic']
glass = drinkDetails['strGlass']
instructions = drinkDetails['strInstructions']

# Prints the details of the cocktails with explanations
print(f"Name: {name} \n")
if alcoholic == 'Alcoholic':
    print("Is the drink alcoholic: Yes \n")
else:
    print("Is the drink alcoholic: No \n")
print(f"Type of glass: {glass} \n")
print(f"Instructions: {instructions}  ")

