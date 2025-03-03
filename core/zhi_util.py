from config.interaction_config import THREE_GROUP, THREE_COMBINATIONS, TWO_COMBINATIONS, TWO_HARM, TWO_DESTRUCTION, TWO_CLASS, TWO_CONTROL, THREE_PUNISHMENT, TWO_PUNISHMENT, THREE_GROUP_DICT, THREE_COMBINATION_DICT
from config.zhi import ZHI


class ZhiUtil:

    @staticmethod
    def is_tam_hoi(a, b, c):
        for value in THREE_GROUP:
            if a in value and b in value and c in value and a != b and b != c and a != c:
                return True
        return False

    @staticmethod
    def is_tam_hop(a, b, c):
        for value in THREE_COMBINATIONS:
            if a in value and b in value and c in value and a != b and b != c and a != c:
                return True
        return False

    @staticmethod
    def is_nhi_hop(a, b):
        for value in TWO_COMBINATIONS:
            if a in value and b in value and a != b:
                return True
        return False

    @staticmethod
    def is_hai(a, b):
        for value in TWO_HARM:
            if a in value and b in value and a != b:
                return True
        return False

    @staticmethod
    def is_pha(a, b):
        for value in TWO_DESTRUCTION:
            if a in value and b in value and a != b:
                return True
        return False

    @staticmethod
    def is_xung(a, b):
        for value in TWO_CLASS:
            if a == value[0] and b == value[1]:
                return True
        return False

    @staticmethod
    def is_khac(a, b):
        for value in TWO_CONTROL:
            if a == value[0] and b == value[1]:
                return True
        return False

    @staticmethod
    def is_tam_hinh(a, b, c):
        for value in THREE_PUNISHMENT:
            if a in value and b in value and c in value and a != b and b != c and a != c:
                return True
        return False

    @staticmethod
    def is_tu_hinh(a, b):
        for value in TWO_PUNISHMENT:
            if a in value and b in value and a == b:
                return True
        return False

    @staticmethod
    def get_tam_hoi_elemental(zhi: str):
        for value in THREE_GROUP_DICT:
            zhi_list = value['zhi']
            if zhi in zhi_list:
                return value['elemental']
        return None

    @staticmethod
    def get_tam_hop_elemental(zhi: str):
        for value in THREE_COMBINATION_DICT:
            zhi_list = value['zhi']
            if zhi in zhi_list:
                return value['elemental']
        return None

    @staticmethod
    def get_polarity(zhi):
        return ZHI[zhi]["polarity"]

    @staticmethod
    def get_elemental(zhi):
        return ZHI[zhi]["element"]