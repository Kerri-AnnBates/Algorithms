#!/usr/bin/python

import math

#    			  i
# recipe_keys = [milk, butter, flour]
# check ingredietns for milk
# if there is milk, then set batch = recipe.get(recipe_keys[i]) / ingredients.get(recipe_keys[i]) and push to batch_nums which is a list.


def recipe_batches(recipe, ingredients):
    recipe_keys = list(recipe.keys())
    batch_nums = []

    if len(ingredients) < len(recipe):
        return 0

    for i in range(0, len(recipe_keys)):
        recipe_amount = recipe.get(recipe_keys[i])
        ingredients_amount = ingredients.get(recipe_keys[i])

        batch = ingredients_amount // recipe_amount
        batch_nums.append(batch)

    return min(batch_nums)


print(
    recipe_batches(
        {"milk": 100, "butter": 50, "cheese": 10},
        {"milk": 198, "butter": 52, "cheese": 10},
    )
)
# print(
#     recipe_batches(
#         {"milk": 2, "sugar": 40, "butter": 20}, {"milk": 5, "sugar": 120, "butter": 500}
#     )
# )

if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {"milk": 100, "butter": 50, "flour": 5}
    ingredients = {"milk": 132, "butter": 48, "flour": 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

