#Authors billy_smalls and kipper86

#Ideas
#Script will read a file for input of what to look for when alt spamming, file type/format not yet decided

import Resources.read_file

affixes = Resources.read_file.read_file()

for affix, names in affixes.items():
    quoted_names = [f'"{name}"' for name in names]  # wrap each name in double quotes
    print(f"{affix} = [{', '.join(quoted_names)}]")








# @kipper
#Example of two methods, first is copying without advanced mod description, second is with advanced mod description
'''
Item Class: Bows
Rarity: Magic
Tempered Spine Bow of the Phantom
--------
Bow
Physical Damage: 77-182 (augmented)
Critical Strike Chance: 6.50%
Attacks per Second: 1.40
--------
Requirements:
Level: 64
Dex: 212 (unmet)
--------
Sockets: R 
--------
Item Level: 87
--------
+46 to Dexterity
Adds 39 to 67 Physical Damage





Item Class: Bows
Rarity: Magic
Tempered Spine Bow of the Phantom
--------
Bow
Physical Damage: 77-182 (augmented)
Critical Strike Chance: 6.50%
Attacks per Second: 1.40
--------
Requirements:
Level: 64
Dex: 212 (unmet)
--------
Sockets: R 
--------
Item Level: 87
--------
{ Prefix Modifier "Tempered" (Tier: 2) — Damage, Physical, Attack }
Adds 39(30-40) to 67(63-73) Physical Damage
{ Suffix Modifier "of the Phantom" (Tier: 2) — Attribute }
+46(43-50) to Dexterity

'''