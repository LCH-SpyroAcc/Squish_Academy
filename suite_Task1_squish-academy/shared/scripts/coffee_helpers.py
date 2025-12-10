# -*- coding: utf-8 -*-
#File for coffee helpers

from squish import *
import names


def fetch_coffee_card_object(coffee_type):
    match coffee_type.lower():
        case "cappuccino":
            return waitForObject(names.cappuccino_CoffeeCard)
            
        case "latte":
            return waitForObject(names.latte_CoffeeCard)
            
        case "espresso":
            return waitForObject(names.espresso_CoffeeCard)
            
        case "macchiato":
            return waitForObject(names.macchiato_CoffeeCard)
            
        case _:
            raise Exception("Unsupported coffee name provided")
            test.fail("Test failed.")
            

