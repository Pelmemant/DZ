class Knight:
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


class Mage:
    def __init__(self, name, mana, spellbook=[]):
        self.name = name
        self.mana = mana
        self.spellbook = spellbook


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    module = obj.__module__
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    if hasattr(obj, '__module__'):
        info['module'] = module
        info['attributes'] = attributes
        info['methods'] = methods

    return info


first_mage = Mage('Мерлин', 30, ["Огненный шар", "водяной гейзер", "Лечение"])
first_knight = Knight('Сэр Ланцелот', 10)
info = introspection_info(first_knight)
print(info)
info = introspection_info(first_mage)
print(info)
