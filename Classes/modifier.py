#read the file and create object

#create Modifier object which has a name and a value ex: modifer="dictator's"
class Modifier:
    def __init__ (self, name: str, affix: str):
        self.name = name
        self.affix = affix

    def __repr__(self):
        return f'Modifier(name="{self.name}", value)'