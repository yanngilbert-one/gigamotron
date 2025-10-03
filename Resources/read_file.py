def read_file():
    #read the file and create an object for each line of the file. "r" to read the file and cannot write
    modifiers_by_affix={}
    with open("src\modifiers.txt", "r") as file:
        current_block={}
        for line in file:
            line = line.strip()
            if line.startswith("{"):
                current_block={}
            elif line.startswith("}"):
                if "modifier" in current_block and "affix" in current_block:
                    affix=current_block["affix"]
                    name=current_block["modifier"]
                    if affix not in modifiers_by_affix:
                        modifiers_by_affix[affix] = []
                    modifiers_by_affix[affix].append(name)
            elif "=" in line:
                key, value = line.split ("=", 1)
                key = key.strip()
                value = value.strip().strip('"').lower() #I am removing the "" could probably just not add them to the txt file and lower case
                current_block[key] = value
        return modifiers_by_affix
