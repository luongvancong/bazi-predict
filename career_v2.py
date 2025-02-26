# Danh sách các tổ hợp điều kiện và câu luận tương ứng
import itertools

rule_map = {
    frozenset(["Quan tinh gặp hình", "Quan tinh gặp hại", "Quan tinh gặp phá"]): "Quan tinh gặp hình, hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Quan tinh gặp hình", "Quan tinh gặp hại"]): "Quan tinh gặp hình, hại, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Quan tinh gặp hình", "Quan tinh gặp phá"]): "Quan tinh gặp hình, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Quan tinh gặp hại", "Quan tinh gặp phá"]): "Quan tinh gặp hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Quan tinh gặp hình"]): "Quan tinh gặp hình, có thể bị cản trở trong công việc, cần thận trọng khi ra quyết định.",
    frozenset(["Quan tinh gặp hại"]): "Quan tinh gặp hại, dễ bị kẻ tiểu nhân công kích, cần chú ý lời ăn tiếng nói.",
    frozenset(["Quan tinh gặp phá"]): "Quan tinh gặp phá, công việc dễ bị gián đoạn, nên có kế hoạch dự phòng.",
    frozenset(["Quan Ấn tương sinh"]): "Quan ấn tương sinh, công việc thuận lợi, dễ gặp sự giúp đỡ từ người khác.",
    frozenset(["Quan Ấn tương sinh", "khách có Văn Xương"]): "Quan ấn tương sinh, có Văn Xương, công việc thuận lợi, dễ gặp sự giúp đỡ từ người khác.",
    frozenset(["Quan Ấn tương sinh, có hình, hại, phá"]): "Quan tinh gặp hình, hại, phá nhưng có Quan Ấn tương sinh, công việc tuy có trở ngại nhưng vẫn có quý nhân giúp đỡ, có thể xoay chuyển tình thế.",
    frozenset(["Quan tinh thấu can gặp xung khắc"]): 'Quan tinh thấu can lại gặp xung, khắc, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, mâu thuẫn nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.',
    frozenset(["Quan tinh thấu can gặp xung khắc", "Quan Ấn tương sinh"]): 'Quan tinh tương sinh là tốt tuy nhiên vẫn tồn tại xung, khắc, công việc có sự thuận lợi nhất định nhưng cũng cần phải cẩn thận với những trở ngại, khó khăn.',
    frozenset(["Ấn tinh nhiều", "khách có Trạch Mã"]): "Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc."
    # frozenset(["khách có Văn Xương"]): None,
    # frozenset(['Quan tinh gặp hình', 'khách có Văn Xương', 'Quan Ấn tương sinh']): '123'
}

thap_than_in_can_interactions = {
    "Tương xung": [],
    "Tương khắc": []
}
thap_than_in_zhi_interactions = {
    "Tam hình": [],
    "Tự hình": []
}

quan_tinh_in_hinh = ({'Chính Quan', 'Thất Sát'} in thap_than_in_zhi_interactions['Tam hình']
                     or {'Chính Quan', 'Thất Sát'} in thap_than_in_zhi_interactions['Tự hình'])
quan_tinh_in_hai = False
quan_tinh_in_pha = False
quan_tinh_thau_can_gap_xung_khac = ({'Chính Quan', 'Thất Sát'} in thap_than_in_can_interactions['Tương xung']
                                    or {'Chính Quan', 'Thất Sát'} in thap_than_in_can_interactions['Tương khắc'])
quan_an_tuong_sinh = True
co_van_xuong = False

quan_tinh_gap_hinh = True
quan_tinh_gap_hai = False
quan_tinh_gap_pha = False
# quan_an_tuong_sinh_co_van_xuong = True
quan_an_tuong_sinh_gap_hinh_hai_pha = False
quan_tinh_gap_hinh_hai_pha = False
guest_have_van_xuong = True
guest_have_trach_ma = True
an_tinh_nhieu = True

column_hidden_thap_than = ['Chính Quan', 'Thất Sát']

# Điều kiện cần kiểm tra
conditions = [
    (guest_have_van_xuong, "khách có Văn Xương"),
    (quan_tinh_gap_hinh_hai_pha, "Quan tinh gặp hình, hại, phá"),
    (quan_tinh_in_hai, "Quan tinh gặp hình, phá"),
    (quan_tinh_in_pha, "Quan tinh gặp hại, phá"),
    (quan_tinh_gap_hinh, "Quan tinh gặp hình"),
    (quan_tinh_gap_hai, "Quan tinh gặp hại"),
    (quan_tinh_gap_pha, "Quan tinh gặp phá"),
    # (quan_an_tuong_sinh_co_van_xuong, "Quan Ấn tương sinh, có Văn Xương"),
    (quan_an_tuong_sinh_gap_hinh_hai_pha, "Quan Ấn tương sinh, có hình, hại, phá"),
    (quan_an_tuong_sinh, "Quan Ấn tương sinh"),
    (quan_tinh_thau_can_gap_xung_khac, "Quan tinh thấu can gặp xung khắc"),
    (an_tinh_nhieu, "Ấn tinh nhiều"),
    (guest_have_trach_ma, "khách có Trạch Mã")
]


def find_best_match(active_conditions, rule_map):
    """Tìm câu luận gần nhất nếu không có kết quả chính xác"""
    if active_conditions in rule_map:
        return rule_map[active_conditions]

    # Thử loại bỏ dần từng điều kiện để tìm tổ hợp gần nhất
    for i in range(len(active_conditions), 0, -1):
        for subset in itertools.combinations(active_conditions, i):
            subset_frozen = frozenset(subset)
            if subset_frozen in rule_map:
                return rule_map[subset_frozen]

    return 'Không có dự đoán cho trường hợp này'


def find_best_match_multi(active_conditions, rule_map):
    """Tìm tất cả các tổ hợp con hợp lệ trong rule_map, ưu tiên tổ hợp có nhiều điều kiện nhất"""
    matched_predictions = []
    max_condition_count = 0  # Số điều kiện lớn nhất trong rule_map khớp

    # Thử tất cả các tổ hợp con của active_conditions (từ lớn đến nhỏ)
    for i in range(len(active_conditions), 0, -1):
        for subset in itertools.combinations(active_conditions, i):
            subset_frozen = frozenset(subset)
            if subset_frozen in rule_map:
                # Nếu tổ hợp này có nhiều điều kiện hơn tổ hợp trước đó, reset danh sách
                if len(subset) > max_condition_count:
                    max_condition_count = len(subset)
                    matched_predictions = [rule_map[subset_frozen]]  # Chỉ lấy tổ hợp có điều kiện lớn nhất
                elif len(subset) == max_condition_count:
                    matched_predictions.append(rule_map[subset_frozen])  # Thêm nếu cùng mức ưu tiên

    # Nếu không có kết quả nào khớp, trả về câu mặc định
    if not matched_predictions:
        return ["Không có dự đoán cho trường hợp này"]

    return matched_predictions

# Lọc ra các điều kiện đúng
active_conditions = frozenset(name for cond, name in conditions if cond)
print(active_conditions)
predict = []
# Nếu có Chính Quan hoặc Thất Sát và có ít nhất một điều kiện trong số trên
if active_conditions:
    # Lấy câu luận tương ứng từ rule_map
    # prediction = rule_map.get(active_conditions) or "Không có dự đoán cho trường hợp này"
    prediction = find_best_match_multi(active_conditions, rule_map)
    predict.extend(prediction)

print(predict)
