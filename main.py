from CoffeeMachine import CoffeeMachine
from CoffeeGrinder import CoffeeGrinder


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.turn_on()
    coffee_machine.add_water(100)
    coffee_machine.brew_coffee()

    coffee_machine = CoffeeGrinder()
    coffee_machine.turn_on()
    coffee_machine.add_beans(100)
    coffee_machine.grind_beans()
