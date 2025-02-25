# -*- encoding: utf-8 -*-
from config.gan import GAN
from config.interaction_config import TWO_ZHI_HIDDEN_COMBINATION
from elemental_util import Elemental
from util import find_gan_interaction, find_thap_than, group_pairs, print_message, get_hidden_thap_than, count_all_thap_than
from zhi_util import is_tam_hinh, is_tam_hoi, get_tam_hoi_elemental, get_hidden_gans, get_interaction, \
    check_zhi_interaction_priority, is_tam_hop, get_tam_hop_elemental, is_nhi_hop, is_tuong_hai, is_tuong_pha, is_tuong_xung, is_tu_hinh, is_tuong_khac
from core.than_sat import ThanSat


def career_predict_by_guest(bazi: dict, guest: str):
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

    guest_has_van_xuong = any(item["column"] == guest for item in van_xuong_items)
    guest_has_tuong_tinh = any(item["column"] == guest for item in tuong_tinh_items)
    guest_has_trach_ma = any(item["column"] == guest for item in trach_ma_items)

    str_van_xuong_tuong_tinh = ''
    if guest_has_van_xuong:
        str_van_xuong_tuong_tinh += 'Văn Xương'
    if guest_has_tuong_tinh:
        str_van_xuong_tuong_tinh += 'Tướng Tinh'

    count_an = count_all_thap_than(bazi, ('Thiên Ấn', 'Chính Ấn'), only_count_primary=True)
    count_quan_sat = count_all_thap_than(bazi, ('Chính Quan', 'Thất Sát'), only_count_primary=True)
    # print(count_an)
    # print(count_quan_sat)

    if count_an > 2 and guest_can in ('Chính Ấn', 'Thiên Ấn'):
        if guest_has_trach_ma:
            predict.append('Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc.')
        else:
            predict.append('Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.')

    if count_quan_sat > 2 and guest_can in ('Chính Quan', 'Thất Sát'):
        predict.append('Quan tinh nhiều, công việc dễ gặp áp lực, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.')

    for column, (can, chi) in bazi.items():
        if column not in ['year', 'month', 'day', 'hour', 'menh_cung']:
            continue
        interaction = find_gan_interaction(guest_can, can)
        zhi_interactions = check_zhi_interaction_priority((guest_chi, chi))
        column_can_thap_than = find_thap_than(can, day_master)
        column_hidden_gans = get_hidden_gans(chi)
        column_hidden_thap_than = []
        for hidden_gan in column_hidden_gans:
            column_hidden_thap_than.append(find_thap_than(hidden_gan, day_master))

        if interaction == 'Tương khắc' and column_can_thap_than == 'Thất Sát':
            if column == 'menh_cung':
                predict.append('Mệnh cung có Thất Sát gặp khắc, công việc dễ có thị phi, cần phải lưu ý.')
            elif column == 'month':
                predict.append('Trụ tháng có Thất Sát gặp khắc, công việc dễ có thị phi, cần phải lưu ý.')

        if interaction == 'Tương khắc' and column_can_thap_than == 'Chính Quan':
            if column == 'menh_cung':
                predict.append('Mệnh cung có Chính Quan gặp khắc, công việc dễ có thị phi, biến động công việc.')
            elif column == 'month':
                predict.append('Trụ tháng có Chính Quan gặp khắc, công việc dễ có thị phi, biến động công việc.')

        if interaction == 'Tương khắc' and column_can_thap_than in ('Thiên Ấn', 'Chính Ấn'):
            if column == 'month':
                predict.append('Trụ tháng có Ấn tinh gặp khắc, công việc dễ gặp xung đột, mâu thuẫn.')
            elif column == 'menh_cung':
                predict.append('Mệnh cung có Ấn tinh gặp khắc, công việc, sự nghiệp dễ gặp xung đột, mâu thuẫn.')
            else:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung.')

        if guest_thap_than == 'Chính Quan' and column == 'day' and interaction == 'Tương hợp':
            if guest_has_van_xuong or guest_has_tuong_tinh:
                if guest_has_van_xuong and guest_has_tuong_tinh:
                    predict.append(f'Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Tướng Tinh, Văn Xương, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.')
                elif guest_has_van_xuong:
                    predict.append(f'Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Văn Xương, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.')
                elif guest_has_tuong_tinh:
                    predict.append(f'Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Tướng Tinh, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.')
            else:
                predict.append('Chính Quan đến hợp với nhật chủ, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, ủng hộ.')

        if guest_thap_than == 'Thất Sát' and column == 'day' and interaction == 'Tương khắc':
            predict.append('Thất Sát đến tương khắc với nhật chủ, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.')

        if ((guest_thap_than in ('Thất Sát', 'Chính Quan') and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn'))
                or (guest_hidden_thap_than[0] in {'Thất Sát', 'Chính Quan'} and column_hidden_thap_than[0] in {'Chính Ấn', 'Thiên Ấn'})):
            if (guest_thap_than == 'Thất Sát' and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn')) or ('Thất Sát' == guest_hidden_thap_than[0] and column_hidden_thap_than in ('Chính Ấn', 'Thiên Ấn')):
                if "Tương hình" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột.')
                else:
                    predict.append('Tương đối thuận lợi, có Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ.')
            elif ((guest_thap_than == 'Chính Quan' and column_can_thap_than in ('Chính Ấn', 'Thiên Ấn')) or ('Chính Quan' == guest_hidden_thap_than[0] and column_hidden_thap_than[0] in {'Chính Ấn', 'Thiên Ấn'}))\
                    and len(check_zhi_interaction_priority((guest_chi, chi))) > 0:
                if "Tương hình" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột.')
                elif "Tương phá" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương phá, vẫn nên đề phòng tiểu nhân phá hoại.')
                elif "Tương hại" in check_zhi_interaction_priority((guest_chi, chi)):
                    predict.append('Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hại, vẫn nên đề phòng lòng dạ tiểu nhân có ý đồ xấu.')
                else:
                    if guest_has_van_xuong or guest_has_tuong_tinh:
                        predict.append(f'ương đối thuận lợi, có Quan Ấn tương sinh, Lại có thêm cát tinh {str_van_xuong_tuong_tinh} tương trợ, cơ hội thăng tiến sẽ tốt hơn.')
                    else:
                        predict.append(f'Tương đối thuận lợi, có Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến.')

        if {guest_thap_than, column_can_thap_than} == {'Thất Sát', 'Chính Quan'}:
            if 'Thương Quan' == guest_hidden_thap_than[0]:
                predict.append('Quan Sát thấu can lại tạp loạn, gặp cách cục Thương Quan khắc Quan lưu ý chuyện thị phi, tranh đấu tại công sở.')
            else:
                predict.append('Quan Sát thấu can lại tạp loạn, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.')

        if ({'Chính Tài', 'Thiên Tài'} & set(guest_hidden_thap_than)
            and {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than)) and (
                guest_chi, chi) in TWO_ZHI_HIDDEN_COMBINATION:
            predict.append('Tài tinh Ám hợp Ấn tinh, công việc dễ gặp sai sót, nhầm lẫn với số liệu, con số, hoặc tài chính, cũng rất dễ mất tập trung.')

        # if {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than) and "Tương khắc" in zhi_interactions:
        #     predict.append(f'Ấn tinh gặp khắc, công việc dễ gặp trở ngại, xung đột, sai sót, mất tập trung, nên kiểm tra lại công việc trước khi hoàn thành.')


        # if {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than) and ("Tương hình" in zhi_interactions or "Tương hại" in zhi_interactions or "Tương phá" in zhi_interactions):
        #     if "Tương hình" in zhi_interactions and "Tương hại" in zhi_interactions and "Tương phá" in zhi_interactions:
        #         predict.append(f'Ấn tinh gặp hình, hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')
        #     if "Tương hình" in zhi_interactions and "Tương hại" in zhi_interactions:
        #         predict.append(f'Ấn tinh gặp hình, hại, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
        #     if "Tương hình" in zhi_interactions and "Tương phá" in zhi_interactions:
        #         predict.append(f'Ấn tinh gặp hình, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
        #     if "Tương hại" in zhi_interactions and "Tương phá" in zhi_interactions:
        #         predict.append(f'Ấn tinh gặp hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')

        if column == 'month':
            if 'Tương phá' in zhi_interactions:
                predict.append(f'{guest_chi} {chi} tương phá, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều. Đề phòng tiểu nhân quấy phá.')
            elif 'Tương xung' in zhi_interactions:
                predict.append(f'{guest_chi} {chi} tương xung, công việc dễ gặp mâu thuẫn, xung đột. Nên dĩ hoà vi quý.')


    guest_zhi_interactions = []
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

        _is_tu_hinh = is_tu_hinh(guest_chi, chi_0) or is_tu_hinh(guest_chi, chi_1)
        _is_nhi_hop = is_nhi_hop(guest_chi, chi_0) or is_nhi_hop(guest_chi, chi_1)
        _is_tuong_hai = is_tuong_hai(guest_chi, chi_0) or is_tuong_hai(guest_chi, chi_1)
        _is_tuong_pha = is_tuong_pha(guest_chi, chi_0) or is_tuong_pha(guest_chi, chi_1)
        _is_tuong_xung = is_tuong_xung(guest_chi, chi_0) or is_tuong_xung(guest_chi, chi_1)
        _is_tuong_khac = is_tuong_khac(guest_chi, chi_0) or is_tuong_khac(guest_chi, chi_1)

        if tam_hinh:
            guest_zhi_interactions.append({
                "column": (guest, pair[0], pair[1]),
                "zhi": (guest_chi, chi_0, chi_1),
                "name": "Tam hình"
            })
        elif _is_tu_hinh:
            guest_zhi_interactions.append({
                "column": is_tu_hinh(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_tu_hinh(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Tự hình"
            })

        if _is_tuong_hai:
            guest_zhi_interactions.append({
                "column": is_tuong_hai(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_tuong_hai(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Tương hại"
            })

        if _is_tuong_pha:
            guest_zhi_interactions.append({
                "column": is_tuong_pha(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_tuong_pha(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Tương phá"
            })

        if _is_tuong_xung:
            guest_zhi_interactions.append({
                "column": is_tuong_xung(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_tuong_xung(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Tương xung"
            })

        if _is_tuong_khac:
            guest_zhi_interactions.append({
                "column": is_tuong_khac(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_tuong_khac(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Tương khắc"
            })

        if _is_nhi_hop:
            guest_zhi_interactions.append({
                "column": is_nhi_hop(guest_chi, chi_0) and (guest, pair[0]) or (guest, pair[1]),
                "zhi": is_nhi_hop(guest_chi, chi_0) and (guest_chi, chi_0) or (guest_chi, chi_1),
                "name": "Nhị hợp"
            })

        tam_hop_zhi_name = ""
        tam_hoi_zhi_name = ""
        if tam_hop:
            if guest_chi in ("Thân", "Tý", "Thìn"):
                tam_hop_zhi_name = "Thân, Tý, Thìn"
            elif guest_chi in ("Tị", "Dậu", "Sửu"):
                tam_hop_zhi_name = "Tị, Dậu, Sửu"
            elif guest_chi in ("Dần", "Ngọ", "Tuất"):
                tam_hop_zhi_name = "Dần, Ngọ, Tuất"
            else:
                tam_hop_zhi_name = "Hợi, Mão, Mùi"

        if tam_hoi:
            if guest_chi in ("Thân", "Dậu", "Tuất"):
                tam_hoi_zhi_name = "Thân, Dậu, Tuất"
            elif guest_chi in ("Tị", "Ngọ", "Mùi"):
                tam_hoi_zhi_name = "Tị, Ngọ, Mùi"
            elif guest_chi in ("Dần", "Mão", "Thìn"):
                tam_hoi_zhi_name = "Dần, Mão, Thìn"
            else:
                tam_hoi_zhi_name = "Hợi, Tý, Sửu"

        # if tam_hinh:
        #     predict.append('Tam hình giữa %s, %s, %s, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều.' % (
        #         guest_chi, chi_0, chi_1))

        # @TODO: Sửa lại đoạn lại, sau khi có các quan hệ tương tác giữa các can chi thì code bên dưới
        if tam_hoi and Elemental.is_sinh(tam_hoi_elemental, day_master_elemental):
            if guest_has_trach_ma:
                predict.append(f'Tam hội {tam_hoi_zhi_name} làm Ấn vượng, lại gặp thêm Trạch Mã, nên công việc nhiều, bận rộn, có thể sẽ phải đi lại công tác nhiều.')
            else:
                predict.append(f'Tam hội {tam_hoi_zhi_name} làm Ấn vượng nên công việc nhiều, bận rộn.')

        if tam_hoi and Elemental.is_khac(tam_hoi_elemental, day_master_elemental):
            predict.append(f'Tam hội {tam_hoi_zhi_name} làm Quan Sát vượng nên công việc gặp nhiều áp lực, bận rộn.')

        if tam_hop and Elemental.is_sinh(tam_hop_elemental, day_master_elemental):
            if guest_has_trach_ma:
                predict.append(f'Tam hợp {tam_hop_zhi_name} làm Ấn vượng, lại gặp thêm Trạch Mã, nên công việc nhiều, bận rộn, có thể sẽ phải đi lại công tác nhiều.')
            else:
                predict.append(f'Tam hợp {tam_hop_zhi_name} làm Ấn vượng nên công việc nhiều, bận rộn.')

        if tam_hop and Elemental.is_khac(tam_hop_elemental, day_master_elemental):
            predict.append(f'Tam hợp {tam_hop_zhi_name} làm Quan Sát vượng nên công việc dễ gặp áp lực, căng thẳng.')

    predict = [s for s in predict if not any(s in other and s != other for other in predict)]

    # print_message(guest_zhi_interactions)

    column_hidden_thap_than = []
    for column, (can, chi) in bazi.items():
        if column == guest:
            continue
        hidden_thap_than = get_hidden_thap_than(chi, day_master)
        for hg in hidden_thap_than:
            column_hidden_thap_than.append(hg)

    guest_have_tam_hinh = any(item["name"] == "Tam hình" for item in guest_zhi_interactions)
    guest_have_tu_hinh = any(item["name"] == "Tự hình" for item in guest_zhi_interactions)
    guest_have_tuong_pha = any(item["name"] == "Tương phá" for item in guest_zhi_interactions)
    guest_have_tuong_hai = any(item["name"] == "Tương hại" for item in guest_zhi_interactions)
    guest_have_tuong_khac = any(item["name"] == "Tương khắc" for item in guest_zhi_interactions)
    guest_have_tuong_xung = any(item["name"] == "Tương xung" for item in guest_zhi_interactions)

    if {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than) and guest_have_tam_hinh:
        if guest_have_tuong_khac or guest_have_tuong_xung:
            predict.append('Ấn tinh gặp tam hình, lại thêm xung, khắc, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, mâu thuẫn nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.')
        else:
            predict.append('Ấn tinh gặp tam hình, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.')
    else:
        if {'Chính Ấn', 'Thiên Ấn'} & set(column_hidden_thap_than) and (guest_have_tu_hinh or guest_have_tuong_hai or guest_have_tuong_pha):
            if guest_have_tu_hinh and guest_have_tuong_hai and guest_have_tuong_pha:
                predict.append(f'Ấn tinh gặp hình, hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tu_hinh and guest_have_tuong_hai:
                predict.append(f'Ấn tinh gặp hình, hại, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tu_hinh and guest_have_tuong_pha:
                predict.append(f'Ấn tinh gặp hình, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tuong_hai and guest_have_tuong_pha:
                predict.append(f'Ấn tinh gặp hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')

    if {'Chính Quan', 'Thất Sát'} & set(column_hidden_thap_than) and guest_have_tam_hinh:
        if guest_have_tuong_khac or guest_have_tuong_xung:
            predict.append('Quan tinh gặp tam hình, lại thêm xung, khắc, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, mâu thuẫn nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.')
        else:
            predict.append('Quan tinh gặp tam hình, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.')
    else:
        if {'Chính Quan', 'Thất Sát'} & set(column_hidden_thap_than) and (guest_have_tu_hinh or guest_have_tuong_hai or guest_have_tuong_pha):
            if guest_have_tu_hinh and guest_have_tuong_hai and guest_have_tuong_pha:
                predict.append(f'Quan tinh gặp hình, hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tu_hinh and guest_have_tuong_hai:
                predict.append(f'Quan tinh gặp hình, hại, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tu_hinh and guest_have_tuong_pha:
                predict.append(f'Quan tinh gặp hình, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.')
            if guest_have_tuong_hai and guest_have_tuong_pha:
                predict.append(f'Quan tinh gặp hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.')

    predict = [s for s in predict if not any(s in other and s != other for other in predict)]

    if len(predict) < 2:
        if 'Chính Ấn' == guest_hidden_thap_than[0]:
            if 'Thương Quan' == guest_thap_than:
                predict.append('Công việc tương đối nhiều và bận rộn, Thương Quan thấu can có nhiều ý tưởng, đầu óc nhạy bén nhưng cũng hay bay bổng.')
            elif 'Chính Quan' == guest_thap_than:
                predict.append('Quan Ấn tương sinh, công việc tương đối nhiều và bận rộn, Chính Quan thấu can dễ được quý nhân tương trợ, ủng hộ.')
            elif 'Chính Tài' == guest_thap_than:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung, dễ vị lợi ích cá nhân mà mất đi cơ hội.')
            elif 'Chính Ấn' == guest_thap_than:
                if guest_has_trach_ma:
                    predict.append('Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc.')
                else:
                    predict.append('Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.')
            elif 'Kiếp Tài' == guest_thap_than:
                predict.append('Kiếp Tài thấu can, lại được Ấn vượng, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.')
            elif 'Thiên Tài' == guest_thap_than:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung. Lưu ý dễ vì lợi ích bên ngoài mà mất đi cơ hội.')
            else:
                predict.append(f'Chưa có dữ liệu cho trường hợp {guest_thap_than} toạ Chính Ấn.')

        if 'Thiên Ấn' == guest_hidden_thap_than[0]:
            if 'Thực Thần' == guest_thap_than:
                predict.append('Công việc tương đối nhiều và bận rộn, Thực Thần thấu can dễ được người khác quý mến.')
            elif 'Thất Sát' == guest_thap_than:
                predict.append('Sát Ấn tương sinh, công việc tương đối nhiều và bận rộn, cũng dễ gặp áp lực từ cấp trên.')
            elif 'Thiên Tài' == guest_thap_than:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung, dễ vị lợi ích bên ngoài mà mất đi cơ hội.')
            elif 'Thiên Ấn' == guest_thap_than:
                if guest_has_trach_ma:
                    predict.append('Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc.')
                else:
                    predict.append('Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.')
            elif 'Tỷ Kiên' == guest_thap_than:
                predict.append('Tỷ Kiên thấu can, lại được Ấn vượng, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.')
            elif 'Thương Quan' == guest_thap_than:
                predict.append('Thiên Ấn và Thương Quan hình hành tổ hợp thích hợp cho học tập, nghiên cứu những lĩnh vực trái ngành hoặc nâng cao kiến thức.')
            else:
                predict.append(f'Chưa có dữ liệu cho trường hợp {guest_thap_than} toạ Thiên Ấn.')

        if 'Chính Quan' == guest_hidden_thap_than[0]:
            if 'Thương Quan' == guest_thap_than:
                predict.append('Tổ hợp Thương Quan khắc Quan, nên chú ý đến công việc, dễ gặp thị phi, xung đột, hạn chế việc tranh cãi.')
            elif 'Chính Quan' == guest_thap_than:
                predict.append('Quan tinh song thể lực lượng vượng tướng, công việc tương đối nhiều và bận rộn, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.')
            elif 'Chính Tài' == guest_thap_than:
                predict.append('Tài sinh Quan, công việc và tài lộc cùng song hành mang lại nhiều cơ hội thăng tiến, phát triển.')
            elif 'Chính Ấn' == guest_thap_than:
                predict.append('Quan Ấn tương sinh, công việc tương đối nhiều và bận rộn, Chính Ấn thấu can dễ được quý nhân tương trợ, ủng hộ.')
            elif 'Kiếp Tài' == guest_thap_than:
                predict.append('Kiếp Tài thấu can, lại có Quan tinh kiểm soát nên công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.')
            else:
                predict.append(f'Chưa có dữ liệu cho trường hợp {guest_thap_than} toạ Chính Quan.')

        if 'Thất Sát' == guest_hidden_thap_than[0]:
            if 'Thực Thần' == guest_thap_than:
                predict.append('Thực Thần chế Sát, Sát tinh được chế hoá, chăm chỉ và kiên trì sẽ đạt được thành quả tốt.')
            elif 'Thất Sát' == guest_thap_than:
                predict.append('Sát tinh quá vượng, công việc tương đối nhiều và bận rộn, cũng dễ gặp áp lực từ cấp trên.')
            elif 'Thiên Tài' == guest_thap_than:
                predict.append('Tài sinh Sát, công việc dễ gặp áp lực, stress, dễ vị lợi ích bên ngoài mà mất đi cơ hội.')
            elif 'Thiên Ấn' == guest_thap_than:
                predict.append('Sát Ấn tương sinh, chăm chỉ làm việc sẽ đạt được thành công, công việc tương đối nhiều và bận rộn.')
            elif 'Tỷ Kiên' == guest_thap_than:
                predict.append('Tỷ Kiên thấu can, toạ Sát, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.')
            else:
                predict.append(f'Chưa có dữ liệu cho trường hợp {guest_thap_than} toạ Thất Sát.')

        if 'Chính Ấn' == guest_thap_than:
            if 'Chính Tài' == guest_hidden_thap_than[0]:
                predict.append('Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung, dễ vì lợi ích cá nhân mà mất đi cơ hội.')

    if len(predict) == 0:
        predict.append('Công việc tương đối bình thường, không có dấu hiệu đặc biệt. Tập trung làm tốt công việc hiện tại. Nếu có thời gian, nên học hỏi thêm kiến thức mới.')

    predict = [s for s in predict if not any(s in other and s != other for other in predict)]

    return "\n".join(list(dict.fromkeys(predict)))
