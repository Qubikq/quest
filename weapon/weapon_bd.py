from systems import locales
from weapon import weapon_classes
output = locales.localization
language = locales.language

weapon_types = [
    weapon_classes.MeleeWeapon(output['weapon']['sword'][language], 10),
    weapon_classes.MeleeWeapon(output['weapon']['axe'][language], 12),
    weapon_classes.MeleeWeapon(output['weapon']['mace'][language], 15),
]

mage_weapon_types = [
    weapon_classes.MageWeapon(output['weapon']['staff'][language], 10),
    weapon_classes.MageWeapon(output['weapon']['wand'][language], 8),
    weapon_classes.MageWeapon(output['weapon']['orb'][language], 12),
]

archer_weapon_types = [
    weapon_classes.ArcherWeapon(output['weapon']['bow'][language], 12),
    weapon_classes.ArcherWeapon(output['weapon']['crossbow'][language], 14),
    weapon_classes.ArcherWeapon(output['weapon']['longbow'][language], 15),
]
