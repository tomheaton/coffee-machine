from CoffeeMachine import CoffeeMachine


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    coffee_machine.turn_on()
    coffee_machine.add_water(100)
    coffee_machine.brew_coffee()
