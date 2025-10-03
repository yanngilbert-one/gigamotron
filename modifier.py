#read the file and create object

#create Modifier object which has a name and a value ex: modifer="dictator's"
class Modifier:
    def __init__ (self, name: str, value: str):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.value}"
    
#read the file and create an object for each line of the file. "r" to read the file and cannot write

modifiers=[]   
with open("modifiers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "=" in line:
            name, value = line.split ("=", 1)
            name = name.strip()
            value = value.strip().strip('"').lower() #I am removing the "" could probably just not add them to the txt file and lower case
            modifiers.append(Modifier(name, value))

print(modifiers)