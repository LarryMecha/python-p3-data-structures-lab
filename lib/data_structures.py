spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
        return [food['name'] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]


def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Generate chili pepper emojis based on the heat level
        chili_emojis = '🌶' * heat_level
        
        # Format the output string
        output = f"{name} ({cuisine}) | Heat Level: {chili_emojis}"
        
        # Print the formatted string
        print(output)



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        
        # Generate chili pepper emojis based on the heat level
        chili_emojis = '🌶' * heat_level
        
        # Format the output string
        output = f"{name} ({cuisine}) | Heat Level: {chili_emojis}"
        
        # Print the formatted string
        print(output)

def get_average_heat_level(spicy_foods):
      if not spicy_foods:
        return 0  # Return 0 if the list is empty to avoid division by zero

    # Calculate the total heat level
      total_heat = sum(food['heat_level'] for food in spicy_foods)
    
    # Calculate the number of spicy foods
      num_foods = len(spicy_foods)
    
    # Calculate the average heat level
      average_heat = total_heat / num_foods
    
    # Return the average heat level as an integer
      return int(round(average_heat))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    
    # Return the updated list
    return spicy_foods