from config.elemental import ELEMENTAL
from util import group_pairs, find_thap_than, get_hidden_thap_than, print_message
from zhi_util import is_tam_hoi, get_tam_hoi_elemental, is_tam_hop, get_tam_hop_elemental, is_tu_hinh, is_nhi_hop, is_tuong_hai, is_tuong_pha, is_tuong_xung, is_tuong_khac, is_tam_hinh


class Util:
    def __init__(self, bazi: dict, guest: str):
        self.bazi = bazi
        self.guest = guest

    def is_elemental_sinh(self, guest, host):
        interactions = ELEMENTAL[guest]['interactions']
        for interaction, elm in interactions:
            if elm == host and interaction == 'Tương sinh':
                return True



    def find_guest_zhi_interactions(self):
        bazi = self.bazi
        guest = self.guest
        day_master = bazi['day'][0]
        guest_can = bazi[guest][0]
        guest_chi = bazi[guest][1]
        guest_thap_than = find_thap_than(guest_can, day_master)

        guest_zhi_interactions = []

        columns = [key for key in bazi.keys() if key != guest]
        two_columns = group_pairs(columns)
        for pair in two_columns:
            column_0 = pair[0]
            column_1 = pair[1]
            can_0 = bazi[column_0][0]
            can_1 = bazi[column_1][0]
            chi_0 = bazi[column_0][1]
            chi_1 = bazi[column_1][1]

            is_base_bazi_columns = {column_0, column_1} & {'year', 'month', 'day', 'hour'}
            if not is_base_bazi_columns:
                continue

            # print_message([column_0, column_1, chi_0, chi_1])

            tam_hinh = is_tam_hinh(guest_chi, chi_0, chi_1)
            tam_hoi = is_tam_hoi(guest_chi, chi_0, chi_1)
            tam_hoi_elemental = get_tam_hoi_elemental(guest_chi)
            tam_hop = is_tam_hop(guest_chi, chi_0, chi_1)
            tam_hop_elemental = get_tam_hop_elemental(guest_chi)

            _is_tu_hinh = is_tu_hinh(guest_chi, chi_0) or is_tu_hinh(guest_chi, chi_1)
            _is_nhi_hop = is_nhi_hop(guest_chi, chi_0) or is_nhi_hop(guest_chi, chi_1)
            _is_tuong_hai = is_tuong_hai(guest_chi, chi_0) or is_tuong_hai(guest_chi, chi_1)
            _is_tuong_pha = is_tuong_pha(guest_chi, chi_0) or is_tuong_pha(guest_chi, chi_1)
            _is_tuong_xung = is_tuong_xung(guest_chi, chi_0) or is_tuong_xung(guest_chi, chi_1)
            _is_tuong_khac = is_tuong_khac(guest_chi, chi_0) or is_tuong_khac(guest_chi, chi_1)
            _is_tam_hoi = is_tam_hoi(guest_chi, chi_0, chi_1)
            _is_tam_hop = is_tam_hop(guest_chi, chi_0, chi_1)

            # print_message(is_tuong_pha('Dần', 'Thân'))
            # exit(0)

            if tam_hinh:
                guest_zhi_interactions.append({
                    "column": (guest, pair[0], pair[1]),
                    "zhi": (guest_chi, chi_0, chi_1),
                    "thap_than": [guest_thap_than] + [x for x in get_hidden_thap_than(chi_0, day_master)] + [x for x in get_hidden_thap_than(chi_1, day_master)],
                    "name": "Tam hình"
                })

            elif _is_tu_hinh:
                guest_zhi_interactions.append({
                    "column": is_tu_hinh(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_tu_hinh(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than]
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_tu_hinh(guest_chi, chi_0)]
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_tu_hinh(guest_chi, chi_1)],
                    "name": "Tự hình"
                })
            if _is_tuong_hai:
                guest_zhi_interactions.append({
                    "column": is_tuong_hai(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_tuong_hai(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than]
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_tuong_hai(guest_chi, chi_0)]
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_tuong_hai(guest_chi, chi_1)],
                    "name": "Tương hại"
                })

            if _is_tuong_pha:
                guest_zhi_interactions.append({
                    "column": is_tuong_pha(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_tuong_pha(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than] \
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_tuong_pha(guest_chi, chi_0)] \
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_tuong_pha(guest_chi, chi_1)],
                    "name": "Tương phá"
                })

            if _is_tuong_xung:
                guest_zhi_interactions.append({
                    "column": is_tuong_xung(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_tuong_xung(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than]
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_tuong_xung(guest_chi, chi_0)]
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_tuong_xung(guest_chi, chi_1)],
                    "name": "Tương xung"
                })

            if _is_tuong_khac:
                guest_zhi_interactions.append({
                    "column": is_tuong_khac(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_tuong_khac(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than]
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_tuong_khac(guest_chi, chi_0)]
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_tuong_khac(guest_chi, chi_1)],
                    "name": "Tương khắc"
                })

            if _is_nhi_hop:
                guest_zhi_interactions.append({
                    "column": is_nhi_hop(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                    "zhi": is_nhi_hop(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                    "thap_than": [guest_thap_than]
                                 + [x for x in get_hidden_thap_than(chi_0, day_master) if is_nhi_hop(guest_chi, chi_0)]
                                 + [x for x in get_hidden_thap_than(chi_1, day_master) if is_nhi_hop(guest_chi, chi_1)],
                    "name": "Nhị hợp"
                })

        for x in guest_zhi_interactions:
            x['thap_than'] = list(set(x['thap_than']))

        return guest_zhi_interactions