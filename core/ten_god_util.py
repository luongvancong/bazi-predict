from config.ten_god import TEN_GOD


class TenGodUtil:

    @staticmethod
    def is_sinh(a, b):
        for keys, value in TEN_GOD.items():
            if a in keys and b in value['sinh']:
                return True
        return False

    @staticmethod
    def is_khac(a, b):
        for keys, value in TEN_GOD.items():
            if a in keys and b in value['khắc']:
                return True
        return False
