from random import randint, choice


class Droid:
    body_parts = ["head", "chest", "legs"]

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __bool__(self):
        if self.health > 0:
            return True
        return False

    def __str__(self):
        return 'Name: {}. Health: {}'.format(self.name, self.health)

    def attack(self, enemy):
        attack_power = randint(1, 15)
        attack_part = choice(self.body_parts)

        defence_power, defence_part = enemy.defence()
        if attack_part == defence_part:
            print('Defence is guessed: {}'.format(defence_part))
            attack_power = attack_power - defence_power
        if attack_power > 0:
            enemy.health -= attack_power

    def defence(self):
        defence_power = randint(5, 10)
        defence_part = choice(self.body_parts)
        return (defence_power, defence_part)

    def find_temp_enemy(self, droids):
        sorted_droids = list(reversed(sorted(droids, key=lambda x: x.health)))
        target = sorted_droids[0] if self != sorted_droids[0] \
            else sorted_droids[1]
        return target


class IronDroid(Droid):

    def strike_with_swort(self):
        print("strike_with_swort")

    def attack(self, enemy):
        self.strike_with_swort()
        return super().attack(enemy)


class ElectroDroid(Droid):

    def electro_shock(self):
        print("electro_shock")

    def attack(self, enemy):
        self.electro_shock()
        return super().attack(enemy)


class Arena:
    def __init__(self, droids):
        self.droids = droids
        self.round = 0

    def start_battle(self):
        while len(self.droids) > 1:
            self.make_round()
        print('Game over')
        if self.droids:
            print(self.droids[0])
        else:
            print('Tie')

    def make_round(self):
        self.round += 1
        print('Round is {}'.format(self.round))
        for dr in self.droids:
            print(dr)

        for droid in self.droids:
            droid.attack(droid.find_temp_enemy(self.droids))

        self.check_droids()

    def check_droids(self):
        for droid in self.droids:
            if droid.health <= 0:
                self.droids.remove(droid)
        if len(self.droids) == 1 and self.droids[0].health <= 0:
            self.droids = []


if __name__ == "__main__":
    iro = IronDroid("iron")
    ele = ElectroDroid("electro")
    ele2 = ElectroDroid("electro2")

    arena = Arena([iro, ele, ele2])
    arena.start_battle()