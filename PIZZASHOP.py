# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:51:21 2023

@author: chugh
"""

def cost_calculator(*pizzas, **kwargs):
    toppings_dict = {"pepperoni":1, "mushroom":0.5, "olive":0.5, "anchovy":2, "ham":1.5}
    drinks_dict = {"small":2, "medium":3, "large":3.5, "tub":3.75}
    wings_dict = {"10":5, "20":9, "40":17.5, "100":48}
    argsspecified= kwargs.keys()
    # find cost of *pizza -->
    plain_pizzas_cost = 13*len(pizzas)
    sum_pizzas_cost = plain_pizzas_cost
    for pizza in pizzas:
#        if not pizza:
        for topping in pizza:
            cost_of_topping = toppings_dict[topping]
            sum_pizzas_cost = sum_pizzas_cost + cost_of_topping
    # find cost of wings
    sum_wgorder_cost = 0
    if 'wings' in argsspecified:
        for wgpack in kwargs['wings']:
            wings_cost_of_pack = wings_dict[str(wgpack)]
            sum_wgorder_cost = sum_wgorder_cost + wings_cost_of_pack        
    # find cost of drinks
    sum_drink_order_cost = 0
    if 'drinks' in argsspecified:
        for drink in kwargs['drinks']:
            cost_of_drink = drinks_dict[drink]
            sum_drink_order_cost = sum_drink_order_cost + cost_of_drink
    discount = 0
    if 'coupon' in argsspecified:
        discount = kwargs['coupon']
    total_cost_of_food = sum_pizzas_cost + sum_wgorder_cost + sum_drink_order_cost
    taxes = .0625 * total_cost_of_food
    discount_amount = discount * total_cost_of_food
    final_cost = (total_cost_of_food + taxes) - discount_amount
    return(round(final_cost, 2))

# space

#print(cost_calculator(drinks=['tub'], coupon = 0.1))
print(cost_calculator([]))
#print(cost_calculator([], ["ham", "anchovy"], drinks=["tub", "tub"], coupon=0.1))
#print(cost_calculator([], [], drinks=['tub', 'small'], wings = [10,10], coupon = 0.1))
# print(cost_calculator(drinks=["small"]))
# z = cost_calculator([], [], ["pepperoni", "pepperoni"], wings=[10, 20], drinks=["small"])