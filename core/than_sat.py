class ThanSat:

    def __init__(self, bazi: dict):
        self.bazi = bazi

    def find_van_xuong(self):
        bazi = self.bazi
        can_ngay = self.bazi['day'][0]
        can_nam = self.bazi['year'][0]
        result = []

        van_xuong_map = {
            'Giáp': 'Tị',
            'Ất': 'Ngọ',
            ('Bính', 'Mậu'): 'Thân',
            ('Đinh', 'Tị'): 'Dậu',
            'Canh': 'Hợi',
            'Tân': 'Tị',
            'Nhâm': 'Dần',
            'Quý': 'Mão'
        }

        for column, (can, chi) in bazi.items():
            for key, value in van_xuong_map.items():
                if (isinstance(key, tuple) and (can_ngay in key or can_nam in key)) or (can_ngay == key or can_nam == key):
                    if chi == value:
                        result.append({
                            "column": column,
                            "name": 'Văn Xương'
                        })

        return result
