recipes = []

with open('recipes.txt', 'rt', encoding = 'utf8') as rec_fail:
    for text in rec_fail:
        dish_name = text.strip()
        dish = {"name": dish_name, "ingredients": []}
        ingredients_count = rec_fail.readline()
        for ing in range(int(ingredients_count)):
            ingredients = rec_fail.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
        blank_line = rec_fail.readline()
        recipes.append(dish)

# print(recipes)

def get_shop_list_by_dishes(dishes, person_count):
    products = {}
    for dish in dishes:
        for cook_book in recipes:
            if cook_book['name'] == dish:
                for ing in cook_book['ingredients']:
                    if ing['name'] not in products.keys():
                        measure = ing['measure']
                        quantity = person_count * int(ing['quantity'])
                        products[ing['name']] = {'measure': measure, 'quantity': quantity}

                    elif ing['name'] in products.keys():
                        measure = ing['measure']
                        quantity = person_count * int(ing['quantity']) + int((products[ing['name']])['qmeasure'])
                        products[ing['name']] = {'measure': measure, 'quantity': quantity}  

    return products

print(get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 2))