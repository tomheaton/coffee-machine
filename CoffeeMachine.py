class CoffeeMachine:
    power: bool = False
    water: int = 0
    water_capacity: int = 100

    def __init__(self):
        print("Coffee Machine created.")

    def turn_on(self) -> None:
        self.power = True

    def turn_off(self) -> None:
        self.power = True

    def add_water(self, water: int) -> None:
        self.water = min(self.water_capacity, self.water + water)

    def brew_coffee(self) -> None:
        if not self.power:
            raise Exception("power is off")

        if self.water == 0:
            raise Exception("not enough water")

        print("brewing coffee...")

        water_to_use: int = 4

        for i in range(0, 3):
            self.water = max(0, self.water - water_to_use)

        print("brewing done")
