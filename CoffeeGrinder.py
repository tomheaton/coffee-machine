class CoffeeGrinder:
    power: bool = False
    beans: int = 0
    beans_capacity: int = 100

    def __init__(self):
        print("Coffee Grinder created.")

    def turn_on(self) -> None:
        self.power = True

    def turn_off(self) -> None:
        self.power = True

    def add_beans(self, beans: int) -> None:
        self.beans = min(self.beans_capacity, self.beans + beans)

    def grind_beans(self) -> None:
        print("grinding beans...")
