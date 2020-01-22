#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 100000000
  for x in recipe.keys():
    if x in ingredients.keys() and ingredients[x] // recipe[x]  < batches:
      batches = ingredients[x] // recipe[x]
    elif x not in ingredients.keys():
      batches = 0
      break
  return batches






if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))