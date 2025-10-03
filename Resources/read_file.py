def read_file():
    #read the file and create an object for each line of the file. "r" to read the file and cannot write
    prefixes = []
    suffixes = []
    with open("src/modifiers.txt", "r") as file:
        current_block={}
        for line in file:
            line = line.strip()
            if line.startswith("{"):
                current_block={}
            elif line.startswith("modifier"):
                current_block["modifier"] = line.split("=", 1)[1].strip('"')
            elif line.startswith("affix"):
                current_block["affix"] = line.split("=", 1)[1].strip('"')
            elif line.startswith("use="):
                current_block["use"] = int(line.split("=", 1)[1])
            elif line.startswith("}"):
                # End of block, keep only if use=1
                if current_block.get("use", 0) == 1 and "modifier" in current_block and "affix" in current_block:
                        if current_block["affix"].lower() == "prefix":
                            prefixes.append(current_block["modifier"])
                        elif current_block["affix"].lower() == "suffix":
                            suffixes.append(current_block["modifier"])
        return prefixes, suffixes
