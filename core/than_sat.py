from util import print_message
from zhi_util import get_zhi_polarity


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

    def find_tuong_tinh(self):
        bazi = self.bazi
        chi_nam = bazi['year'][1]
        chi_ngay = bazi['day'][1]
        result = []

        for k, (can, chi) in bazi.items():

            if chi_nam in ["Dần", "Ngọ", "Tuất"] or chi_ngay in ["Dần", "Ngọ", "Tuất"]:
                if chi == "Ngọ":
                    result.append({'name': "Tướng Tinh", 'column': k})

            if chi_nam in ["Thân", "Tý", "Thìn"] or chi_ngay in ["Thân", "Tý", "Thìn"]:
                if chi == "Tý":
                    result.append({'name': "Tướng Tinh", 'column': k})

            if chi_nam in ["Tị", "Dậu", "Sửu"] or chi_ngay in ["Tị", "Dậu", "Sửu"]:
                if chi == "Dậu":
                    result.append({'name': "Tướng Tinh", 'column': k})

            if chi_nam in ["Hợi", "Mão", "Mùi"] or chi_ngay in ["Hợi", "Mão", "Mùi"]:
                if chi == "Mão":
                    result.append({'name': "Tướng Tinh", 'column': k})

        return result

    def find_trach_ma(self):
        bazi = self.bazi
        chi_nam = bazi['year'][1]
        chi_ngay = bazi['day'][1]
        result = []

        for k, (can, chi) in bazi.items():

            if chi_nam in ["Dần", "Ngọ", "Tuất"] or chi_ngay in ["Dần", "Ngọ", "Tuất"]:
                if chi == "Thân":
                    result.append({'name': "Trạch Mã", 'column': k})

            if chi_nam in ["Thân", "Tý", "Thìn"] or chi_ngay in ["Thân", "Tý", "Thìn"]:
                if chi == "Dần":
                    result.append({'name': "Trạch Mã", 'column': k})

            if chi_nam in ["Tị", "Dậu", "Sửu"] or chi_ngay in ["Tị", "Dậu", "Sửu"]:
                if chi == "Hợi":
                    result.append({'name': "Trạch Mã", 'column': k})

            if chi_nam in ["Hợi", "Mão", "Mùi"] or chi_ngay in ["Hợi", "Mão", "Mùi"]:
                if chi == "Tị":
                    result.append({'name': "Trạch Mã", 'column': k})

        return result

    def find_kiep_sat(self):
        bazi = self.bazi
        result = []
        chi_ngay = bazi['day'][1]
        chi_nam = bazi['year'][1]

        for k, (can, chi) in bazi.items():
            if chi_ngay in ["Dần", "Ngọ", "Tuất"] or chi_nam in ["Dần", "Ngọ", "Tuất"]:
                if chi == "Hợi":
                    result.append({'name': "Kiếp Sát", 'column': k})

            if chi_ngay in ["Thân", "Tý", "Thìn"] or chi_nam in ["Thân", "Tý", "Thìn"]:
                if chi == "Tị":
                    result.append({'name': "Kiếp Sát", 'column': k})

            if chi_ngay in ["Tị", "Dậu", "Sửu"] or chi_nam in ["Tị", "Dậu", "Sửu"]:
                if chi == "Dần":
                    result.append({'name': "Kiếp Sát", 'column': k})

            if chi_ngay in ["Hợi", "Mão", "Mùi"] or chi_nam in ["Hợi", "Mão", "Mùi"]:
                if chi == "Thân":
                    result.append({'name': "Kiếp Sát", 'column': k})

        return result

    def find_tai_sat(self):
        bazi = self.bazi
        chi_nam = bazi['year'][1]
        result = []

        for k, (can, chi) in bazi.items():
            if chi_nam in ["Dần", "Ngọ", "Tuất"] and chi == "Tý":
                result.append({'name': "Tai Sát", 'column': k})
            elif chi_nam in ["Thân", "Tý", "Thìn"] and chi == "Ngọ":
                result.append({'name': "Tai Sát", 'column': k})
            elif chi_nam in ["Tị", "Dậu", "Sửu"] and chi == "Mão":
                result.append({'name': "Tai Sát", 'column': k})
            elif chi_nam in ["Hợi", "Mão", "Mùi"] and chi == "Dậu":
                result.append({'name': "Tai Sát", 'column': k})

        return result

    def find_nguyen_than(self, gender):
        bazi = self.bazi
        chi_nam = bazi["year"][1]
        chieu_thuan = (get_zhi_polarity(chi_nam) == 'Dương' and gender == 1) or (get_zhi_polarity(chi_nam) == 'Âm' and gender == 0)
        result = []

        mapping = {
            "Tý": ("Mùi", "Tị"),
            "Sửu": ("Thân", "Ngọ"),
            "Dần": ("Dậu", "Mùi"),
            "Mão": ("Tuất", "Thân"),
            "Thìn": ("Hợi", "Dậu"),
            "Tị": ("Tý", "Tuất"),
            "Ngọ": ("Sửu", "Hợi"),
            "Mùi": ("Dần", "Tị"),
            "Thân": ("Mão", "Sửu"),
            "Dậu": ("Thìn", "Dần"),
            "Tuất": ("Tị", "Mão"),
            "Hợi": ("Ngọ", "Thìn"),
        }

        for k, (can, chi) in bazi.items():
            if chi == mapping[chi_nam][0] if chieu_thuan else chi == mapping[chi_nam][1]:
                result.append({"name": 'Nguyên Thần', "column": k})

        return result

    def find_luc_giap_khong_vong(self):
        luc_giap_map = {
            "Giáp Tý": ["Giáp Tý", "Ất Sửu", "Bính Dần", "Đinh Mão", "Mậu Thìn", "Kỷ Tị", "Canh Ngọ", "Tân Mùi", "Nhâm Thân", "Quý Dậu"],
            "Giáp Tuất": ["Giáp Tuất", "Ất Hợi", "Bính Tý", "Đinh Sửu", "Mậu Dần", "Kỷ Mão", "Canh Thìn", "Tân Tị", "Nhâm Ngọ", "Quý Mùi"],
            "Giáp Thân": ["Giáp Thân", "Ất Dậu", "Bính Tuất", "Đinh Hợi", "Mậu Tý", "Kỷ Sửu", "Canh Dần", "Tân Mão", "Nhâm Thìn", "Quý Tị"],
            "Giáp Ngọ": ["Giáp Ngọ", "Ất Mùi", "Bính Thân", "Đinh Dậu", "Mậu Tuất", "Kỷ Hợi", "Canh Tý", "Tân Sửu", "Nhâm Dần", "Quý Mão"],
            "Giáp Thìn": ["Giáp Thìn", "Ất Tị", "Bính Ngọ", "Đinh Mùi", "Mậu Thân", "Kỷ Dậu", "Canh Tuất", "Tân Hợi", "Nhâm Tý", "Quý Sửu"],
            "Giáp Dần": ["Giáp Dần", "Ất Mão", "Bính Thìn", "Đinh Tị", "Mậu Ngọ", "Kỷ Mùi", "Canh Thân", "Tân Dậu", "Nhâm Tuất", "Quý Hợi"]
        }

        luu_giap_khong_vong_map = {
            "Giáp Tý": ["Tuất", "Hợi"],
            "Giáp Tuất": ["Thân", "Dậu"],
            "Giáp Thân": ["Ngọ", "Mùi"],
            "Giáp Ngọ": ["Thìn", "Tị"],
            "Giáp Thìn": ["Dần", "Mão"],
            "Giáp Dần": ["Tý", "Sửu"]
        }

        bazi = self.bazi
        can_chi_ngay = " " . join(list(bazi['day']))
        found_tuan = None
        result = []

        for key, list_values in luc_giap_map.items():
            if can_chi_ngay in list_values:
                found_tuan = key
                break

        if found_tuan:
            khong_vong_chi = luu_giap_khong_vong_map.get(found_tuan, [])

            for k, (can, chi) in bazi.items():
                if chi in khong_vong_chi:
                    result.append({
                        'name': "Không Vong",
                        'column': k
                    })

        return result