from config.elemental import ELEMENTAL

class Elemental:
    @staticmethod
    def is_sinh(a, b):
        return ELEMENTAL[a]["interactions"]["Tương sinh"] == b

    @staticmethod
    def is_khac(a, b):
        return ELEMENTAL[a]["interactions"]["Tương khắc"] == b

    @staticmethod
    def get_health(a):
        return ELEMENTAL[a]["health"]