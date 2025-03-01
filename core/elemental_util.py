from config.elemental import ELEMENTAL


class ElementalUtil:

    @staticmethod
    def is_sinh(guest: str, host: str):
        return host == ELEMENTAL[guest]['interactions']['Tương sinh']

    @staticmethod
    def is_khac(guest: str, host: str):
        return host == ELEMENTAL[guest]['interactions']['Tương khắc']