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
        if not self.power:
            raise Exception("power is off")

        if self.beans == 0:
            raise Exception("not enough beans")

        print("grinding beans...")

        beans_to_grind: int = 20

        for i in range(0, 3):
            self.beans = max(0, self.beans - beans_to_grind)

        print("grinding done")
