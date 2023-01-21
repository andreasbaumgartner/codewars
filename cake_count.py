recipe = {'flour': 2, 'sugar': 3, 'eggs': 4}
available = {'flour': 4, 'sugar': 10, 'eggs': 12}


def cakes(recipe, available):

    count_list = []

    for key in recipe:

        if key in available:
            count_list.append(available[key] // recipe[key])
        else:
            return 0

    return min(count_list)


result = cakes(recipe, available)
print(result)
