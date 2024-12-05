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


def get_names(food_list):
    return [food["name"] for food in food_list]

def get_spiciest_foods(food_list):
    return [food for food in food_list if food["heat_level"] > 5]

def print_spicy_foods(food_list):
    for food in food_list:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(food_list, cuisine):
    for food in food_list:
        if food["cuisine"] == cuisine:
            return food
    return None  

def print_spiciest_foods(food_list):
    spiciest = get_spiciest_foods(food_list)
    print_spicy_foods(spiciest)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)


def create_spicy_food(food_list, new_food):
    food_list.append(new_food)
    return food_list


if __name__ == "__main__":
    print(get_names(spicy_foods))  
    print(get_spiciest_foods(spicy_foods)) 
    print_spicy_foods(spicy_foods)
    print(get_spicy_food_by_cuisine(spicy_foods, "American")) 
    print_spiciest_foods(spicy_foods)
    print(average_heat_level(spicy_foods))  
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    print(create_spicy_food(spicy_foods, new_food))  