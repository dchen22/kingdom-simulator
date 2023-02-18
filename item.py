from __future__ import annotations
from character import Character


class Item:
    """ A standard item

    Maybe keep this abstract for now

    === Attributes ===
    name:
        - name of item
    sell_price:
        - the price that this item is sold at
        - generic Item default price is $100

    """
    name: str
    sell_price: float

    def __init__(self, name: str) -> None:
        self.name = name
        self.sell_price = 100

    def get_price(self) -> float:
        """ Return this item's price """
        return self.sell_price

    def set_price(self, new_price: float) -> None:
        """ Change this item's price

        - New price must be at least 0
        - The price will be changed to 0 if the set price is negative
        """
        self.sell_price = max(new_price, 0)


class Consumable(Item):
    """ A generic Consumable

    You can eat them to improve your stats (like foods irl)

    === Attributes ===
    hp_restore:
        - the amount of hp this Krispie restores
    mana_restore:
        - the amount of mana this Krispie restores
    """
    hp_restore: float
    mana_restore: float

    def __init__(self, name, hp_restore, mana_restore):
        Item.__init__(self, name)
        self.hp_restore = hp_restore
        self.mana_restore = mana_restore

    def grant_stats(self, eater: Character):
        raise NotImplementedError


class Weapon(Item):
    """ A generic Weapon class

    Gives its user stats when equipped

    === Attributes ===
    bonus_dmg:
        - the amount of granted damage
    """
    bonus_dmg: float

    def __init__(self, name, bonus_dmg):
        Item.__init__(self, name)
        self.bonus_dmg = bonus_dmg


class Armor(Item):
    """ A generic Armor class

    Gives its users stats when equipped

    === Attributes ===
    bonus_hp:
        - the amount of granted hp
    """
    bonus_hp: float

    def __init__(self, name, bonus_hp):
        Item.__init__(self, name)
        self.bonus_hp = bonus_hp


class Krispie(Consumable):
    """ A (rice) Krispie

    A staple food source.

    === Attributes ===

    increased_hp: (IGNORE FOR NOW)
        - the amount of extra hp this Krispie grants
    """

    def __init__(self):
        Consumable.__init__(self, name='Krispie', hp_restore=150, mana_restore=150)

    def grant_stats(self, eater: Character):
        pass





