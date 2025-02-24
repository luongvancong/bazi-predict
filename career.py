# -*- encoding: utf-8 -*-
from config.gan import GAN
from config.interaction_config import TWO_ZHI_HIDDEN_COMBINATION
from elemental_util import Elemental
from util import find_gan_interaction, find_thap_than, group_pairs
from zhi_util import is_tam_hinh, is_tam_hoi, get_tam_hoi_elemental, get_hidden_gans, get_interaction, \
    check_zhi_interaction_priority, is_tam_hop, get_tam_hop_elemental

CAREER_PREDICTION = [
    {
        "condition": "Ấn tinh nhiều",
        "description": "Công việc có nhiều bận rộn, có thể làm nhiều việc một lúc"
    },
    {
        "condition": "Ấn tinh gặp khắc",
        "description": "Công việc dễ gặp xung đột, mâu thuẫn",
        "modifier": {
            "Tài khắc": "Công việc dễ gặp xung đột, mâu thuẫn liên quan đến các vấn đề số liệu, tài chính, kế toán"
        }
    }
]


def career_predict_by_guest(bazi, guest: tuple):
    guest_can = guest[0]
    guest_chi = guest[1]

    column_labels = {
        "year": "Năm",
        "month": "Tháng",
        "day": "Ngày",
        "hour": "Giờ",
        "dai_van": "Đại vận",
        "luu_nien": "Lưu niên"
    }

    predict = []

    count_an = 0
    count_quan_sat = 0
    day_master = bazi['day'][0]
    day_master_elemental = GAN[day_master]['element']

    guest_thap_than = find_thap_than(guest_can, day_master)
    guest_hidden_gans = get_hidden_gans(guest_chi)
    guest_hidden_thap_than = []
    for hidden_gan in guest_hidden_gans:
        guest_hidden_thap_than.append(find_thap_than(hidden_gan, day_master))

    for column, (can, chi) in bazi.items():
        column_can_thap_than = find_thap_than(can, day_master)
        if column_can_thap_than in ('Thiên Ấn', 'Chính Ấn'):
            count_an += 1

        if column_can_thap_than in ('Chính Quan', 'Thất Sát'):
            count_quan_sat += 1

    if guest_thap_than in ('Thiên Ấn', 'Chính Ấn'):
        count_an += 1

    if count_an > 2:
        predict.append('Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.')

    if count_quan_sat > 2:
        predict.append('Quan tinh nhiều, công việc dễ gặp áp lực, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.')

    for column, (can, chi) in bazi.items():
        interaction = find_gan_interaction(guest_can, can)
        column_can_thap_than = find_thap_than(can, day_master)
        column_hidden_gans = get_hidden_gans(chi)
        column_hidden_thap_than = []
        for hidden_gan in column_hidden_gans:
            column_hidden_thap_than.append(find_thap_than(hidden_gan, day_master))

        if interaction == 'Tương khắc' and column_can_thap_than == 'Thất Sát' and column == 'month':
            predict.append('Trụ tháng có Thất Sát gặp khắc, công việc dễ có thị phi, cần phải lưu ý.')

        if interaction == 'Tương khắc' and column_can_thap_than == 'Chính Quan' and column == 'month':
            predict.append('Trụ tháng có Chính Quan gặp khắc, công việc dễ có thị phi, biến động công việc.')

        if interaction == 'Tương khắc' and column_can_thap_than in ('Thiên Ấn', 'Chính Ấn'):
            if column == 'month':
                predict.append('Trụ tháng có Ấn tinh gặp khắc, công việc dễ gặp xung đột, mâu thuẫn.')
            else:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung')

        if guest_thap_than == 'Chính Quan' and column == 'day' and interaction == 'Tương hợp':
            predict.append('Chính Quan đến hợp với nhật chủ, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, ủng hộ.')

        if guest_thap_than == 'Thất Sát' and column == 'day' and interaction == 'Tương khắc':
            predict.append('Thất Sát đến tương khắc với nhật chủ, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.')

        if ((guest_thap_than in ('Thất Sát', 'Chính Quan') and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn'))
                or {'Thất Sát', 'Chính Quan'} & set(guest_hidden_thap_than) and {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)):
            if (guest_thap_than == 'Thất Sát' and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn')) or (
                    'Thất Sát' in guest_hidden_thap_than and {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)):
                if "Tương hình" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột.')
                else:
                    predict.append('Tương đối thuận lợi, có Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ.')
            elif ((guest_thap_than == 'Chính Quan' and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn')) or ('Chính Quan' in guest_hidden_thap_than and {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)))\
                    and len(check_zhi_interaction_priority((guest_chi, chi))) > 0:
                if "Tương hình" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột.')
                elif "Tương phá" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương phá, vẫn nên đề phòng tiểu nhân phá hoại.')
                elif "Tương hại" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hại, vẫn nên đề phòng lòng dạ tiểu nhân có ý đồ xấu.')
                else:
                    predict.append(f'Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến.')

        if {guest_thap_than, column_can_thap_than} == {'Thất Sát', 'Chính Quan'}:
            if 'Thương Quan' in guest_hidden_thap_than:
                predict.append('Quan Sát thấu can lại tạp loạn, gặp cách cục Thương Quan khắc Quan lưu ý chuyện thị phi, tranh đấu tại công sở.')
            else:
                predict.append('Quan Sát thấu can lại tạp loạn, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.')

        if ({'Chính Tài', 'Thiên Tài'} & set(guest_hidden_thap_than)
            and {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)) and (
                guest_chi, chi) in TWO_ZHI_HIDDEN_COMBINATION:
            predict.append('Tài tinh Ám hợp Ấn tinh, công việc dễ gặp sai sót, nhầm lẫn với số liệu, con số, hoặc tài chính, cũng rất dễ mất tập trung')

        if ({'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)
            and {'Thiên Tài', 'Chính Tài'} & set(
                    guest_hidden_thap_than)) and "Tương khắc" in check_zhi_interaction_priority((guest_chi, chi)):
            predict.append(f'Ấn tinh gặp khắc, công việc dễ gặp trở ngại, xung đột, sai sót, mất tập trung, nên kiểm tra lại công việc trước khi hoàn thành.')

        # if guest_thap_than in ('Chính Tài', 'Thiên Tài') and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn'):
        #     predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung')

    columns = bazi.keys()
    two_columns = group_pairs(columns)
    for pair in two_columns:
        chi_0 = bazi[pair[0]][1]
        chi_1 = bazi[pair[1]][1]
        tam_hinh = is_tam_hinh(guest_chi, chi_0, chi_1)
        tam_hoi = is_tam_hoi(guest_chi, chi_0, chi_1)
        tam_hoi_elemental = get_tam_hoi_elemental(guest_chi)
        tam_hop = is_tam_hop(guest_chi, chi_0, chi_1)
        tam_hop_elemental = get_tam_hop_elemental(guest_chi)
        if tam_hinh:
            predict.append('Tam hình giữa %s, %s, %s, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều.' % (
                guest_chi, chi_0, chi_1))

        if tam_hoi and Elemental.is_sinh(tam_hoi_elemental, day_master_elemental):
            predict.append('Tam hội %s %s %s làm Ấn vượng nên công việc nhiều, bận rộn' % (guest_chi, chi_0, chi_1))

        if tam_hoi and Elemental.is_khac(tam_hoi_elemental, day_master_elemental):
            predict.append('Tam hội %s %s %s làm Quan Sát vượng nên công việc nhiều, bận rộn' % (guest_chi, chi_0, chi_1))

        if tam_hop and Elemental.is_sinh(tam_hop_elemental, day_master_elemental):
            predict.append('Tam hợp %s %s %s làm Ấn vượng nên công việc nhiều, bận rộn' % (guest_chi, chi_0, chi_1))

        if tam_hop and Elemental.is_khac(tam_hop_elemental, day_master_elemental):
            predict.append('Tam hợp %s %s %s làm Quan Sát vượng nên công việc dễ gặp áp lực, căng thẳng' % (guest_chi, chi_0, chi_1))

    predict = [s for s in predict if not any(s in other and s != other for other in predict)]

    return "\n".join(list(dict.fromkeys(predict)))
