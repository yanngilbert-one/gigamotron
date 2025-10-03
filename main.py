#Authors billy_smalls and kipper86

#Ideas
#Script will read a file for input of what to look for when alt spamming, file type/format not yet decided

import Resources.read_file
import Resources.autogui
import pyautogui
import time

affixes = Resources.read_file.read_file()

for affix, names in affixes.items():
    quoted_names = [f'"{name}"' for name in names]  # wrap each name in double quotes
    print(f"{affix} = [{', '.join(quoted_names)}]")

#loop to test if the functions together are working and it did!
for i in range(10):
    Resources.autogui.use_alt()
    pyautogui.click(button="left")
    
    time.sleep(0.1)
    Resources.autogui.copy_item()
    if Resources.autogui.check_clipboard_for("Girded", 3):
        print("Found Girded in item, stopping")
        break
    else:
        print("not Girded, againnnn")
        time.sleep(0.1)






# @kipper
#Example of two methods, first is copying without advanced mod description, second is with advanced mod description
#seems like we will need to use advanced to be able to see mod names so we will need to ctrl + alt + c
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