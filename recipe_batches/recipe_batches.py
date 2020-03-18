#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Create while loop while cooking
  # First check ingredients dictionary has all the same properties and recipe
  # # If not return 0
  # Have counter and loop throut ingredients dictionaryand subtract the recipe amount
  # from the ingredient. check if our ingredient is less than 0
  # If it's less than 0 break out of loop and  set cooing to false
  # return the count because no more can be made 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))