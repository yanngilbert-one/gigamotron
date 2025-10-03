#Authors billy_smalls and kipper86

#Ideas
#Script will read a file for input of what to look for when alt spamming, file type/format not yet decided
import Resources.read_config
import Resources.read_file
import Resources.autogui
import pyautogui
import time

CONFIG_DATA = Resources.read_config.read_config()
affixes = Resources.read_file.read_file()
time.sleep(3)
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
