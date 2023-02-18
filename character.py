from item import Consumable, Krispie


class Character:
    """ A Character

    === Attributes ===
    name:
        - name
    natural_curr_hp:
        - base current hp, without applied items
    natural_max_hp:
        - base max hp, without applied items
    curr_hp:
        - current hp
    max_hp:
        - maximum hp
    natural_curr_mana:
        - base current mana, without applied items
    natural_max_mana:
        - base max mana, without applied items
    curr_mana:
        - current mana
    max_mana:
        - maximum mana
    natural_dmg:
        - base attack damage, without applied items
    dmg:
        - attack damage
    curr_xp:
        - current xp amount
    max_xp:
        - required xp to level up
    level:
        - level
    balance:
        - how much money this character has
    inventory:
        - all of this character's items
    equipped_items:
        - all of this character's equipped gear

    Don't do anything with this class
    """
    name: str

    natural_curr_hp: float
    natural_max_hp: float
    curr_hp: float
    max_hp: float

    natural_curr_mana: float
    natural_max_mana: float
    curr_mana: float
    max_mana: float

    natural_dmg: float
    dmg: float

    curr_xp: float
    max_xp: float
    level: int
    balance: float
    inventory: list
    equipped_items: list

    def __init__(self, name, max_hp, max_mana, dmg) -> None:
        self.name = name
        self.natural_curr_hp, self.natural_max_hp, self.max_hp, self.curr_hp = max_hp, max_hp, max_hp, max_hp
        self.natural_curr_mana, self.natural_max_mana, self.max_mana, self.curr_mana = max_mana, max_mana, max_mana, max_mana
        self.natural_dmg, self.dmg = dmg, dmg
        self.curr_xp = 0
        self.max_xp = 100
        self.level = 1
        self.balance = 0
        self.inventory = [Krispie(), Krispie()]
        self.equipped_items = []

    def update_xp(self, xp_amount: float) -> None:
        """ Update this character's gain in xp

        Character's can't lose xp no matter what
        """
        self.curr_xp += xp_amount
        while self.curr_xp >= self.max_xp:  # in case they get several levels' worth of xp at once
            self.curr_xp -= self.max_xp
            self.level_up()

    def level_up(self) -> None:
        """ Level up this character

        - Update level
        - Update max_hp and dmg
        """
        self.level += 1
        hp_gained = 75
        dmg_gained = 8
        self.natural_max_hp += hp_gained  # increase our max hp depending on level
        self.natural_curr_hp += hp_gained  # adjust current hp by same amount
        self.natural_dmg += dmg_gained  # increase our damage

        self.apply_item_stats()

        self.max_xp *= 1.5  # increase level-up xp requirement

    def consume(self, consumable: Consumable) -> None:
        self.curr_hp = min(self.curr_hp + consumable.hp_restore, self.max_hp)
        self.curr_mana = min(self.curr_mana + consumable.mana_restore, self.max_mana)

    def apply_item_stats(self):
        self.curr_hp = self.natural_curr_hp
        self.max_hp = self.natural_max_hp
        self.dmg = self.natural_dmg

        for item in self.equipped_items:
            # TODO
            pass


class Knight(Character):
    """ Knight

    A noble fellow with good status.

    - starts with high stats
    - large amount of starter money
    - early access to high level shops
    """
    def __init__(self, name):
        Character.__init__(self, name, max_hp=1200, max_mana=800, dmg=100)
        self.balance = 5000

    def consume(self, consumable: Consumable):
        self.curr_hp = min(self.curr_hp + consumable.hp_restore, self.max_hp)
        self.curr_mana = min(self.curr_mana + consumable.mana_restore, self.max_mana)
