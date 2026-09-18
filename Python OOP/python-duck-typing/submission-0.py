class SpiderMan:
    def attack(self) -> str:
        return "Web Shooter!"
    
    def defend(self) -> str:
        return "Spider Sense!"


class BlackWidow:
    def attack(self) -> str:
        return "Widow's Bite!"
    
    def defend(self) -> str:
        return "Acrobatic Dodge!"


def battle_sequence(obj) -> None:
    print(obj.attack())
    print(obj.defend())


spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
