#Authors billy_smalls and kipper86

#Ideas
#Script will read a file for input of what to look for when alt spamming, file type/format not yet decided

import Resources.read_file

affixes = Resources.read_file.read_file()

for affix, names in affixes.items():
    quoted_names = [f'"{name}"' for name in names]  # wrap each name in double quotes
    print(f"{affix} = [{', '.join(quoted_names)}]")