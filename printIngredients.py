import requests

# An API request for the cocktail margarita
url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita'

response = requests.get(url)
info = response.json()
cocktail = info['drinks']


def ingredients():
    """Adds one to strIngredient as each ingredient has its own key. This is to reduce errors from copying and pasting,
    and allows only keys with a value to be included"""
    count = 1
    while count != -1:
        if x['strIngredient' + str(count)] is not None:
            print(x['strIngredient' + str(count)], end=',')
            count += 1
        else:
            count = -1
            print()

# Uses a for loop for the details of the cocktail.
# Loop is for finding the ingredients as each ingredient has a separate key


for x in cocktail:
    name = x['strDrink']
    alcoholic = x['strAlcoholic']
    glass = x['strGlass']
    instructions = x['strInstructions']

# Prints the details of the cocktails with explanations
    print(f"Name: {name} \n")
    if alcoholic == 'Alcoholic':
        print("Is the drink alcoholic: Yes \n")
    else:
        print("Is the drink alcoholic: No \n")
    print(f"Type of glass: {glass} \n")
    print("Ingredients: "), ingredients()
    print(f"\n Instructions: {instructions}  \n")

