# -*- encoding: utf-8 -*-
from collections import defaultdict

from config.gan import GAN
from core.gan_util import GanUtil
from core.ten_god_util import TenGodUtil
from core.than_sat import ThanSat
from core.util import Util
from core.zhi_util import ZhiUtil
from util import find_thap_than, get_hidden_thap_than, find_gan_interaction, print_message
from zhi_util import get_hidden_gans, check_zhi_interaction_priority, is_tuong_xung, is_tuong_khac


class ConditionCollector:

    day_master_data = {}
    month_data = {
        'zhi_thap_than': []
    }
    guest_data = {
        'have_than_sat': {}
    }
    data = {}
    quan_tinh_set = {'Thất Sát', 'Chính Quan'}
    an_tinh_set = {'Thiên Ấn', 'Chính Ấn'}
    tai_tinh_set = {'Thiên Tài', 'Chính Tài'}
    thuc_thuong_set = {'Thực Thần', 'Thương Quan'}
    ty_kiep_set = {'Tỷ Kiên', 'Kiếp Tài'}

    column_labels = {
        "year": 'năm',
        "month": "tháng",
        "day": "ngày",
        "hour": "giờ",
        "menh_cung": "mệnh cung",
        "than_cung": "thân cung",
        "thai_nguyen": "thai nguyên",
        "dai_van": "đại vận",
        "tieu_van": "tiểu vận",
        "luu_nien": "lưu niên"
    }

    def __init__(self, bazi: dict, guest: str):
        self.bazi = bazi
        self.guest = guest
        self.init_share_data()

    def init_share_data(self):
        bazi = self.bazi
        guest = self.guest

        util = Util(bazi, guest)

        guest_can = bazi[guest][0]
        guest_chi = bazi[guest][1]

        # B1. Luận tương tác thiên can, thập thần, có phối trụ, thần sát
        # B2. Luận tương tác địa chi, thập thần, có phối trụ, thần sát
        # B3. Không có gì luận tổ hợp khách trụ

        day_master = bazi['day'][0]
        day_master_elemental = GAN[day_master]['element']

        guest_thap_than = find_thap_than(guest_can, day_master)
        guest_hidden_gans = get_hidden_gans(guest_chi)
        guest_hidden_thap_than = []
        for hidden_gan in guest_hidden_gans:
            guest_hidden_thap_than.append(find_thap_than(hidden_gan, day_master))

        month_gan = bazi['month'][0]
        month_zhi = bazi['month'][1]
        month_gan_thap_than = find_thap_than(month_gan, day_master)
        month_zhi_thap_than = get_hidden_thap_than(month_zhi, day_master)
        month_gan_interactions = find_gan_interaction(guest_can, month_gan)
        month_zhi_interactions = check_zhi_interaction_priority((guest_chi, month_zhi))

        than_sat = ThanSat(bazi)
        van_xuong_items = than_sat.find_van_xuong()
        tuong_tinh_items = than_sat.find_tuong_tinh()
        trach_ma_items = than_sat.find_trach_ma()

        all_than_sat = van_xuong_items + tuong_tinh_items + trach_ma_items

        self.day_master_data['gan'] = day_master
        self.day_master_data['elemental'] = day_master_elemental

        for column, (can, chi) in bazi.items():
            if column == guest:
                continue
            if column not in self.data:
                self.data[column] = {}
            self.data[column]['gan'] = can
            self.data[column]['zhi'] = chi
            self.data[column]['gan_thap_than'] = find_thap_than(can, day_master)
            self.data[column]['zhi_thap_than'] = get_hidden_thap_than(chi, day_master)
            self.data[column]['than_sat'] = [item["name"] for item in all_than_sat if item["column"] == column]
            self.data[column]['gan_interactions'] = find_gan_interaction(guest_can, can)

        self.month_data['gan'] = month_gan
        self.month_data['zhi'] = month_zhi
        self.month_data['gan_thap_than'] = month_gan_thap_than
        self.month_data['zhi_thap_than'] = month_zhi_thap_than
        self.month_data['gan_interactions'] = month_gan_interactions
        self.month_data['zhi_interactions'] = month_zhi_interactions
        self.month_data['than_sat'] = [item["name"] for item in all_than_sat if item["column"] == 'month']

        self.guest_data['gan'] = guest_can
        self.guest_data['zhi'] = guest_chi
        self.guest_data['gan_thap_than'] = guest_thap_than
        self.guest_data['zhi_thap_than'] = guest_hidden_thap_than
        self.guest_data['have_than_sat']['Văn Xương'] = any(item["column"] == guest for item in van_xuong_items)
        self.guest_data['have_than_sat']['Tướng Tinh'] = any(item["column"] == guest for item in tuong_tinh_items)
        self.guest_data['have_than_sat']['Trạch Mã'] = any(item["column"] == guest for item in trach_ma_items)
        self.guest_data['than_sat'] = [item["name"] for item in all_than_sat if item["column"] == guest]
        self.guest_data['gan_interactions'] = find_gan_interaction(guest_can, day_master)
        self.guest_data['zhi_interactions'] = util.find_guest_zhi_interactions()

    def collect_conditions(self):
        # B1. Luận tương tác thiên can, thập thần, có phối trụ, thần sát
        # B2. Luận tương tác địa chi, thập thần, có phối trụ, thần sát
        # B3. Không có gì luận tổ hợp khách trụ
        # return self.find_month_column_conditions() + self.find_guest_column_conditions() + self.find_than_sat_conditions()
        return self.find_thap_than_conditions()

    def find_guest_column_conditions(self):
        day_master_data = self.day_master_data
        guest_data = self.guest_data

        guest_thap_than = guest_data['gan_thap_than']
        guest_hidden_thap_than = guest_data['zhi_thap_than']

        conditions = []

        # Find guest conditions
        if guest_thap_than in {'Chính Quan'} and guest_hidden_thap_than[0] in self.an_tinh_set \
            or guest_hidden_thap_than[0] in {'Chính Quan'} and guest_thap_than in self.an_tinh_set:
                conditions.append((True, 'Khách thể là Quan Ấn tương sinh'))

        if guest_thap_than in {'Thất Sát'} and guest_hidden_thap_than[0] in self.an_tinh_set \
            or guest_hidden_thap_than[0] in {'Thất Sát'} and guest_thap_than in self.an_tinh_set:
                conditions.append((True, 'Khách thể là Sát Ấn tương sinh'))

        if guest_thap_than in self.tai_tinh_set and guest_hidden_thap_than[0] in self.an_tinh_set \
            or guest_hidden_thap_than[0] in self.tai_tinh_set and guest_thap_than in self.an_tinh_set:
                conditions.append((True, 'Khách thể là Tài khắc Ấn'))

        if guest_thap_than in self.tai_tinh_set and guest_hidden_thap_than[0] in self.quan_tinh_set \
            or guest_hidden_thap_than[0] in self.tai_tinh_set and guest_thap_than in self.quan_tinh_set:
                conditions.append((True, 'Khách thể là Tài sinh Quan'))

        if guest_thap_than == 'Thực Thần' and guest_hidden_thap_than[0] == 'Thất Sát' \
            or guest_hidden_thap_than[0] == 'Thực Thần' and guest_thap_than == 'Thất Sát':
                conditions.append((True, 'Khách thể là Thực Thần chế Sát'))

        if guest_thap_than == 'Thương Quan' and guest_hidden_thap_than[0] == 'Chính Quan' \
            or guest_hidden_thap_than[0] == 'Thương Quan' and guest_thap_than == 'Chính Quan':
                conditions.append((True, 'Khách thể là Thương Quan khắc Quan'))

        conditions.append((True, f"Tổ hợp khách thể là {guest_thap_than} {guest_hidden_thap_than[0]}"))

        if guest_data['gan_thap_than'] == guest_data['zhi_thap_than'][0]:
            conditions.append((True, f"Khách thể là {guest_thap_than} song thể lực vượng"))

        # remove duplicate conditions
        conditions = list(set(conditions))

        return conditions

    def find_month_column_conditions(self):
        return self.find_column_conditions('month')

    def find_column_conditions(self, column: str):
        conditions = []
        column_conditions = self.find_all_column_conditions()

        for cond in column_conditions:
            if cond['column'] == column:
                conditions.append(cond)

        return conditions

    def find_all_column_conditions(self):
        guest = self.guest
        guest_data = self.guest_data
        guest_chi = self.guest_data['zhi']

        guest_can_thap_than =  guest_data['gan_thap_than']
        guest_chi_thap_than = guest_data['zhi_thap_than']

        conditions = []

        for column in self.data:
            if column == guest: continue
            can = self.bazi[column][0]
            chi = self.bazi[column][1]
            column_label = self.column_labels[column]
            gan_thap_than = column != 'day' and self.data[column]['gan_thap_than'] or 'Nhật chủ'
            zhi_thap_than = self.data[column]['zhi_thap_than']
            than_sat_list = self.data[column]['than_sat']
            gan_interaction = self.data[column]['gan_interactions']

            condition_item = {
                "group": [],
                "column": column,
                "thap_than": [gan_thap_than],
                "than_sat": [],
                'thap_than_interactor': [],
                "interactions": [],
                "condition": ""
            }

            if TenGodUtil.is_khac(guest_can_thap_than, gan_thap_than):
                new_condition_item = condition_item.copy()
                new_condition_item['group'] = ['thap_than']
                new_condition_item['interactions'] = ['Tương khắc']
                new_condition_item['thap_than_interactor'] = [guest_can_thap_than]
                new_condition_item['condition'] = f"Thiên can trụ {self.column_labels[column]} có {gan_thap_than} gặp khắc"
                conditions.append(new_condition_item)

            if TenGodUtil.is_sinh(guest_can_thap_than, gan_thap_than):
                new_condition_item = condition_item.copy()
                new_condition_item['group'] = ['thap_than']
                new_condition_item['interactions'] = ['Tương sinh']
                new_condition_item['thap_than_interactor'] = [guest_can_thap_than]
                new_condition_item['condition'] = f"Thiên can trụ {self.column_labels[column]} có {gan_thap_than} gặp sinh"
                conditions.append(new_condition_item)

            additions = set([])
            for interaction in self.guest_data['zhi_interactions']:
                if column in interaction['column'] and self.guest in interaction['column']:
                    additions.add(interaction['name'])

            for interaction in self.guest_data['zhi_interactions']:
                if column in interaction['column'] and self.guest in interaction['column']:
                    for z_thap_than in zhi_thap_than:
                        new_condition_item = condition_item.copy()
                        new_condition_item['thap_than'] = [z_thap_than]
                        new_condition_item['group'] = ['zhi_thap_than']
                        new_condition_item['interactions'] = list(additions)
                        new_condition_item['thap_than_interactor'] = self.guest_data['zhi_thap_than']
                        new_condition_item['condition'] = f"Địa chi trụ {column_label} có {z_thap_than} gặp {interaction['name']}"
                        conditions.append(new_condition_item)

            for ts in self.data[column]['than_sat']:
                new_condition_item = condition_item.copy()
                new_condition_item['group'] = ['than_sat']
                new_condition_item['than_sat'] = [ts]
                new_condition_item['interactions'] = list(additions)
                new_condition_item['condition'] = f"Trụ {column_label} có {ts}"
                conditions.append(new_condition_item)

        # remove duplicate conditions
        conditions = self.remove_duplicates(conditions)
        conditions = self.merge_conditions(conditions)

        return conditions

    def merge_conditions(self, items):
        merged_dict = defaultdict(lambda: defaultdict(list))

        for item in items:
            key = (tuple(item['group']), item['column'], tuple(item['thap_than']), tuple(item['than_sat']))
            merged_dict[key]['interactions'].extend(item['interactions'])
            merged_dict[key]['thap_than_interactor'].extend(item['thap_than_interactor'])
            merged_dict[key]['condition'].append(item['condition'])
            # merged_dict[key]['group'].extend(item['group'])

        # Chuyển kết quả về danh sách
        merged_list = []
        for (group, column, thap_than, than_sat), values in merged_dict.items():
            merged_list.append({
                'group': list(group),
                'column': column,
                'thap_than': list(thap_than),
                'than_sat': list(than_sat),
                'thap_than_interactor': values['thap_than_interactor'],
                'interactions': list(set(values['interactions'])),  # Loại bỏ trùng lặp
                'condition': ' và '.join(values['condition']),
            })

        return merged_list

    def find_than_sat_conditions(self):
        guest_data = self.guest_data
        conditions = []

        for column in self.data:
            for ts in self.data[column]['than_sat']:
                conditions.append({
                    'column': column,
                    'condition': f"Trụ {self.column_labels[column]} có {ts}"
                })

        for ts in guest_data['than_sat']:
            conditions.append({
                'column': self.guest,
                'condition': f"Khách thể có {ts}"
            })

        # remove duplicate conditions
        conditions = self.remove_duplicates(conditions)

        return conditions

    def find_thap_than_conditions(self):
        bazi = self.bazi
        day_master = bazi['day'][0]
        guest_zhi_interactions = self.guest_data['zhi_interactions']
        conditions = []

        for column, (can, chi) in bazi.items():
            if column not in ['year', 'month', 'day', 'hour', 'thai_nguyen', 'menh_cung', 'than_cung']:
                continue

            column_gan_thap_than = find_thap_than(can, day_master)
            column_zhi_thap_than = get_hidden_thap_than(chi, day_master)

            if (self.guest_data['gan_thap_than'] in self.quan_tinh_set and column_gan_thap_than in self.an_tinh_set) \
                or (self.guest_data['zhi_thap_than'][0] in self.quan_tinh_set and column_zhi_thap_than[0] in self.an_tinh_set
                    and (is_tuong_xung(self.guest_data['zhi'], chi) or is_tuong_khac(self.guest_data['zhi'], chi))):
                conditions.append((True, 'Quan Ấn tương sinh'))

            if (self.guest_data['gan_thap_than'] in self.tai_tinh_set and column_gan_thap_than in self.an_tinh_set) \
                or (self.guest_data['zhi_thap_than'][0] in self.tai_tinh_set and column_zhi_thap_than[0] in self.an_tinh_set
                    and (is_tuong_xung(self.guest_data['zhi'], chi) or is_tuong_khac(self.guest_data['zhi'], chi))):
                conditions.append((True, 'Tài khắc Ấn'))

            if (self.guest_data['gan_thap_than'] in self.tai_tinh_set and column_gan_thap_than in self.quan_tinh_set) \
                or (self.guest_data['zhi_thap_than'][0] in self.tai_tinh_set and column_zhi_thap_than[0] in self.quan_tinh_set
                    and (is_tuong_xung(self.guest_data['zhi'], chi) or is_tuong_khac(self.guest_data['zhi'], chi))):
                conditions.append((True, 'Tài sinh Quan'))

            if (self.guest_data['gan_thap_than'] == 'Thực Thần' and column_gan_thap_than == 'Thất Sát') \
                or (self.guest_data['zhi_thap_than'][0] == 'Thực Thần' and column_zhi_thap_than[0] == 'Thất Sát'
                    and (is_tuong_xung(self.guest_data['zhi'], chi) or is_tuong_khac(self.guest_data['zhi'], chi))):
                conditions.append((True, 'Thực Thần chế Sát'))

            if (self.guest_data['gan_thap_than'] == 'Thương Quan' and column_gan_thap_than == 'Chính Quan') \
                or (self.guest_data['zhi_thap_than'][0] == 'Thương Quan' and column_zhi_thap_than[0] == 'Chính Quan'
                    and (is_tuong_xung(self.guest_data['zhi'], chi) or is_tuong_khac(self.guest_data['zhi'], chi))):
                conditions.append((True, 'Thương Quan khắc Quan'))

        for x in guest_zhi_interactions:
            if x['name'] == 'Tam hình' or x['name'] == 'Tự hình':
                if self.quan_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Quan tinh gặp hình'))

            if x['name'] == 'Tương hại':
                if self.quan_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Quan tinh gặp hại'))

            if x['name'] == 'Tương phá':
                if self.quan_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Quan tinh gặp phá'))

            if x['name'] == 'Tam hình' or x['name'] == 'Tự hình':
                if self.an_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Ấn tinh gặp hình'))

            if x['name'] == 'Tương hại':
                if self.an_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Ấn tinh gặp hại'))

            if x['name'] == 'Tương phá':
                if self.an_tinh_set & set(x['thap_than']):
                    conditions.append((True, 'Ấn tinh gặp phá'))

        # remove duplicate conditions
        conditions = list(set(conditions))

        return conditions

    def remove_duplicates(self, conditions: list):
        unique_conditions = []
        seen = set()

        for cond in conditions:
            if isinstance(cond, dict) and "column" in cond and "condition" in cond:
                key = (cond["column"], cond["condition"])
                if key not in seen:
                    seen.add(key)
                    unique_conditions.append(cond)
            else:
                print(f"Invalid entry detected and skipped: {cond}")

        return unique_conditions

    def debug(self):
        bazi = self.bazi

        str_columns = []
        str_can = []
        str_chi = []
        for (column, (can, chi)) in bazi.items():
            str_columns.append(f"{column.ljust(10)}")
            str_can.append(f"{can.ljust(10)}")
            str_chi.append(f"{chi.ljust(10)}")

        print(f"{''.join(str_columns)}")
        print(f"{''.join(str_can)}")
        print(f"{''.join(str_chi)}")
        print("\n")

        print('--------- Tương tác với các loại trụ -----------')
        print(*self.find_all_column_conditions(), sep="\n")
        print("\n")

        print('-------- Tổng hợp theo trụ năm ------------')
        print(*self.find_column_conditions('year'), sep="\n")
        print("\n")

        print('-------- Tổng hợp theo trụ tháng ------------')
        print(*self.find_column_conditions('month'), sep="\n")
        print("\n")

        print('-------- Tổng hợp theo trụ ngày ------------')
        print(*self.find_column_conditions('day'), sep="\n")
        print("\n")

        print('-------- Tổng hợp theo trụ giờ ------------')
        print(*self.find_column_conditions('hour'), sep="\n")
        print("\n")

        print('--------- Thập thần tổ hợp -------------------------')
        print(*self.find_thap_than_conditions(), sep="\n")
        print("\n")

        print('--------- Tổ hợp trụ khách -----------------')
        print(*self.find_guest_column_conditions(), sep="\n")
        print("\n")

        print('--------- Thần sát ------------')
        print(*self.find_than_sat_conditions(), sep="\n")
        print("\n")