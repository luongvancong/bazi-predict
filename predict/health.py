# -*- encoding: utf-8 -*-
from config.gan import GAN
from config.interaction_config import TWO_ZHI_HIDDEN_COMBINATION
from elemental_util import Elemental
from util import find_gan_interaction, find_thap_than, group_pairs, print_message, get_hidden_thap_than, count_all_thap_than
from zhi_util import is_tam_hinh, is_tam_hoi, get_tam_hoi_elemental, get_hidden_gans, get_interaction, \
    check_zhi_interaction_priority, is_tam_hop, get_tam_hop_elemental
from core.than_sat import ThanSat


def health_predict_by_guest(bazi: dict, gender, guest: str):
    guest_can = bazi[guest][0]
    guest_chi = bazi[guest][1]

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

    than_sat = ThanSat(bazi)
    van_xuong_items = than_sat.find_van_xuong()
    tuong_tinh_items = than_sat.find_tuong_tinh()
    trach_ma_items = than_sat.find_trach_ma()
    kiep_sat_items = than_sat.find_kiep_sat()
    tai_sat_items = than_sat.find_tai_sat()
    nguyen_than_items = than_sat.find_nguyen_than(gender)
    vong_than_items = than_sat.find_vong_than()

    guest_has_van_xuong = any(item["column"] == guest for item in van_xuong_items)
    guest_has_tuong_tinh = any(item["column"] == guest for item in tuong_tinh_items)
    guest_has_trach_ma = any(item["column"] == guest for item in trach_ma_items)
    guest_has_kiep_sat = any(item["column"] == guest for item in kiep_sat_items)
    guest_has_tai_sat = any(item["column"] == guest for item in tai_sat_items)
    guest_has_nguyen_than = any(item["column"] == guest for item in nguyen_than_items)
    guest_has_vong_than = any(item["column"] == guest for item in vong_than_items)

    str_van_xuong_tuong_tinh = ''
    if guest_has_van_xuong:
        str_van_xuong_tuong_tinh += 'Văn Xương'
    if guest_has_tuong_tinh:
        str_van_xuong_tuong_tinh += 'Tướng Tinh'

    count_an = count_all_thap_than(bazi, ('Thiên Ấn', 'Chính Ấn'), only_count_primary=True)
    count_quan_sat = count_all_thap_than(bazi, ('Chính Quan', 'Thất Sát'), only_count_primary=True)
    # print(count_an)
    # print(count_quan_sat)

    # if count_an > 2:
    #     if guest_has_trach_ma:
    #         predict.append('Ấn tinh nhiều, lại có thêm Trạch Mã, sức khỏe tốt tuy nhiên phải đi lại, di chuyển nhiều, cũng nên cẩn thận')
    #     else:
    #         predict.append('Ấn tinh nhiều, sức khỏe khá tốt')
    #
    # if count_quan_sat > 2:
    #     predict.append('Quan tinh nhiều, sức khỏe nhìn chung là không quá tốt, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.')

    for column, (can, chi) in bazi.items():
        if column not in ['year', 'month', 'day', 'hour', 'thai_nguyen', 'menh_cung', 'than_cung']:
            continue
        interaction = find_gan_interaction(guest_can, can)
        column_can_thap_than = find_thap_than(can, day_master)
        column_hidden_gans = get_hidden_gans(chi)
        column_hidden_thap_than = []
        for hidden_gan in column_hidden_gans:
            column_hidden_thap_than.append(find_thap_than(hidden_gan, day_master))

        if interaction == 'Tương khắc' and column_can_thap_than == 'Thất Sát' and column == 'day':
            predict.append('Nhật can gặp Thất Sát tương khắc, dễ gặp stress, căng thẳng, sức khỏe có phần giảm sút, cần phải lưu ý.')

        if interaction == 'Tương khắc' and column_can_thap_than == 'Chính Quan' and column == 'day':
            predict.append('Nhật can gặp Chính Quan tương khắc, nhìn chung sức khỏe không quá tốt, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.')

        if (column == 'year' and interaction == 'Tương khắc' and 'Tương xung' in check_zhi_interaction_priority((guest_chi, chi))) or (column == 'year' and interaction == 'Tương xung' and 'Tương khắc' in check_zhi_interaction_priority((guest_chi, chi))):
            predict.append('Năm gặp thiên khắc, địa xung, một số bệnh cũ có thể tái phát, nên chú ý giữ gìn sức khỏe bản thân cũng như người lớn tuổi, cha mẹ trong gia đình.')

        if (column == 'thai_nguyen' and interaction == 'Tương khắc' and 'Tương xung' in check_zhi_interaction_priority((guest_chi, chi))) or (column == 'thai_nguyen' and interaction == 'Tương xung' and 'Tương khắc' in check_zhi_interaction_priority((guest_chi, chi))):
            predict.append('Thai Nguyên gặp thiên khắc, địa xung, một số bệnh cũ có thể tái phát, nên chú ý giữ gìn sức khỏe bản thân, hạn chế chất kích thích, nghỉ ngơi đúng giờ.')

        if column == 'thai_nguyen' and ('Tương khắc' or 'Tương xung' in check_zhi_interaction_priority((guest_chi, chi))):
            predict.append('Thai Nguyên gặp xung khắc, một số bệnh cũ có thể tái phát, nên chú ý giữ gìn sức khỏe bản thân, hạn chế chất kích thích, nghỉ ngơi đúng giờ.')

        # if guest_thap_than in ('Chính Tài', 'Thiên Tài') and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn'):
        #     predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung')

    columns = [key for key in bazi.keys() if key != guest]
    two_columns = group_pairs(columns)
    for pair in two_columns:
        chi_0 = bazi[pair[0]][1]
        chi_1 = bazi[pair[1]][1]
        tam_hinh = is_tam_hinh(guest_chi, chi_0, chi_1)
        tam_hoi = is_tam_hoi(guest_chi, chi_0, chi_1)
        tam_hoi_elemental = get_tam_hoi_elemental(guest_chi)
        tam_hop = is_tam_hop(guest_chi, chi_0, chi_1)
        tam_hop_elemental = get_tam_hop_elemental(guest_chi)

        str_health_elemental_by_day_master = ', '.join(list(Elemental.get_health(day_master_elemental)))

        if tam_hinh:
            predict.append('Tam hình giữa %s, %s, %s, sức khỏe nhìn chung là không tốt, nên cẩn thận tổn thương ngoài da, lưu ý các vật sắc nhọn.' % (
                guest_chi, chi_0, chi_1))
            if ('year' or 'month') in pair:
                predict.append(f'Tam hình giữa {guest_chi}, {chi_0}, {chi_1}, sức khỏe nhìn chung là không tốt, nên cẩn thận tổn thương ngoài da, lưu ý các vật sắc nhọn. Sức khỏe của người lớn tuổi, cha mẹ cũng cần được quan tâm nhiều hơn.')
            if 'hour' in pair:
                predict.append(f'Tam hình giữa {guest_chi}, {chi_0}, {chi_1}, sức khỏe nhìn chung là không tốt, nên cẩn thận tổn thương ngoài da, lưu ý các vật sắc nhọn. Cần chú ý đến sức khỏe của con cái, trẻ nhỏ trong gia đình.')

        if tam_hoi and Elemental.is_khac(tam_hoi_elemental, day_master_elemental):
            if guest_has_trach_ma:
                predict.append(f'Tam hội {guest_chi} {chi_0} {chi_1} làm Quan Sát vượng, lại gặp thêm Trạch Mã, nên sức khỏe hết sức lưu ý, đi lại cẩn thận, các vấn đề liên quan đến {str_health_elemental_by_day_master} cần được quan tâm nhiều hơn.')
            else:
                predict.append(f'Tam hội {guest_chi} {chi_0} {chi_1} làm Quan Sát vượng, nên sức khỏe hết sức lưu ý, các vấn đề liên quan đến {str_health_elemental_by_day_master} cần được quan tâm nhiều hơn.')

        if tam_hop and Elemental.is_khac(tam_hop_elemental, day_master_elemental):
            if guest_has_trach_ma:
                predict.append(f'Tam hợp {guest_chi} {chi_0} {chi_1} làm Quan Sát vượng, lại gặp thêm Trạch Mã, nên sức khỏe hết sức lưu ý, đi lại cẩn thận, các vấn đề liên quan đến {str_health_elemental_by_day_master} cần được quan tâm nhiều hơn.')
            else:
                predict.append(f'Tam hợp {guest_chi} {chi_0} {chi_1} làm Quan Sát vượng, nên sức khỏe hết sức lưu ý, các vấn đề liên quan đến {str_health_elemental_by_day_master} cần được quan tâm nhiều hơn.')

    if guest_has_kiep_sat and guest_has_vong_than:
        predict.append('Kiếp Sát và Vong Thần đều là hung tinh, gặp phải sức khỏe không tốt, dễ chấn thương hoặc tai nạn, cần phải cẩn thận.')
    elif guest_has_kiep_sat:
        predict.append('Kiếp Sát là hung tinh, gặp phải sức khỏe không tốt, dễ chấn thương hoặc tai nạn, cần phải cẩn thận.')
    elif guest_has_vong_than:
        predict.append('Vong Thần là hung tinh, gặp phải sức khỏe không tốt, dễ chấn thương hoặc tai nạn, cần phải cẩn thận.')

    if guest_has_tai_sat:
        predict.append('Tai Sát là hung tinh, gặp phải sức khỏe không tốt, dễ chấn thương hoặc tai nạn, bệnh tật, cần phải cẩn thận.')

    if guest_has_nguyen_than:
        predict.append('Gặp Đại Hao sức khỏe dễ gặp suy nhược, mệt mỏi, cần phải nghỉ ngơi, chăm sóc sức khỏe.')

    predict = [s for s in predict if not any(s in other and s != other for other in predict)]

    if len(predict) == 0:
        predict.append('Sức khỏe tương đối bình thường, không có dấu hiệu gì đáng lo ngại. Cần duy trì chế độ ăn uống, sinh hoạt hợp lý, tập thể dục đều đặn.')

    return "\n".join(list(dict.fromkeys(predict)))
