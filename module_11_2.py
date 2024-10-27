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
    info['attributes'] = dir(obj)
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__module__
    if hasattr(obj, '__module__'):
        info['module'] = module
    return info


first_mage = Mage('Мерлин', 30, ["Огненный шар", "водяной гейзер", "Лечение"])
first_knight = Knight('Сэр Ланцелот', 10)
info = introspection_info(first_knight)
print(info)
info = introspection_info(first_mage)
print(info)