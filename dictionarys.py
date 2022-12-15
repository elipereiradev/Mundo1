favorites = {
    "appetizer": "calamari",
    "vegetable": "broccoli",
    "beverage": "coffee",  
}


print(favorites)

def describe(category):
    food = favorites.get(category)
    
    if food is None:
        message = "I don't have a favorite {}. I love them all!".format(category)
    else:
        message = "My favorite {} is {}".format(category, food)
        
    print(message)