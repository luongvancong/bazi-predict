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
    frozenset(["Quan tinh thấu can", "Quan tinh gặp xung khắc"]): 'Quan tinh thấu can lại gặp xung, khắc, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, mâu thuẫn nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.',
    frozenset(["Quan tinh thấu can", "Quan tinh gặp xung khắc", "Quan Ấn tương sinh"]): 'Quan ấn tương sinh là tốt tuy nhiên vẫn tồn tại xung, khắc, công việc có sự thuận lợi nhất định nhưng cũng cần phải cẩn thận với những trở ngại, khó khăn.',
    frozenset(["Ấn tinh nhiều", "khách có Trạch Mã"]): "Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc.",
    frozenset(["Ấn tinh nhiều"]): "Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.",
    frozenset(["Quan tinh nhiều"]): "Quan tinh nhiều, công việc dễ gặp áp lực, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.",
    frozenset(["Chính Quan đến hợp nhật chủ", "Khách thể có Văn Xương", "Khách thể có Tướng Tinh"]):
        "Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Văn Xương, Tướng Tinh, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.",
    frozenset(["Chính Quan đến hợp nhật chủ"]): "Chính Quan đến hợp với nhật chủ, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, ủng hộ.",
    frozenset(["Thất Sát đến tương khắc nhật chủ"]): "Thất Sát đến tương khắc với nhật chủ, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.",
    frozenset(["Sát Ấn tương sinh", "Quan tinh gặp hình"]): "Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột",
    frozenset(["Sát Ấn tương sinh", "Ấn tinh gặp hình"]): "Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột",
    frozenset(["Sát Ấn tương sinh"]): "Sát Ấn tương sinh, tuy có áp lực nhưng cơ hội phát triển là không tệ",
    frozenset(["Quan Ấn tương sinh", "Quan tinh gặp hình"]): "Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hình, vẫn nên cẩn thận với các vấn đề thị phi, xung đột",
    frozenset(["Quan Ấn tương sinh", "Quan tinh gặp hình"]): "Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương phá, vẫn nên đề phòng tiểu nhân phá hoại",
    frozenset(["Quan Ấn tương sinh", "Quan tinh gặp hình"]): "Quan Ấn tương sinh, dễ đạt được công danh và cơ hội thăng tiến. Do có tương hại, vẫn nên đề phòng lòng dạ tiểu nhân có ý đồ xấu.",
    frozenset(["Quan Ấn tương sinh", "Khách thể có Văn Xương"]): "Quan Ấn tương sinh, Lại có thêm cát tinh Tướng Tinh tương trợ, cơ hội thăng tiến sẽ tốt hơn",
    frozenset(["Quan Sát hỗn tạp", "Khách thể Thương Quan khắc Quan"]): "Quan Sát thấu can lại tạp loạn, gặp cách cục Thương Quan khắc Quan lưu ý chuyện thị phi, tranh đấu tại công sở.",
    frozenset(["Quan Sát hỗn tạp"]): "Quan Sát thấu can lại tạp loạn, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.",
    frozenset(["Tài tinh ám hợp Ấn tinh"]): "Tài tinh Ám hợp Ấn tinh, công việc dễ gặp sai sót, nhầm lẫn với số liệu, con số, hoặc tài chính, cũng rất dễ mất tập trung.",
    frozenset(["Ấn tinh gặp khắc"]): "Ấn tinh gặp khắc, công việc dễ gặp trở ngại, xung đột, sai sót, mất tập trung, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Ấn tinh gặp hình"]): "Ấn tinh gặp hình, công việc dễ gặp thị phi, sai sót, mất tập trung, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Ấn tinh gặp hại"]): "Ấn tinh gặp hại, công việc dễ gặp tiểu nhân quấy phá, nên chú ý hành động, lời nói giữ gìn hòa khí.",
    frozenset(["Ấn tinh gặp phá"]): "Ấn tinh gặp phá, công việc dễ gặp thị phi, xung đột, đổ vỡ, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["Tam hội Ấn vượng", "Khách thể có Trạch Mã"]): "Tam hội làm Ấn vượng, lại gặp thêm Trạch Mã, nên công việc nhiều, bận rộn, có thể sẽ phải đi lại công tác nhiều.",
    frozenset(["Tam hội Quan Sát vượng"]): "Tam hội làm Quan Sát vượng nên công việc gặp nhiều áp lực, bận rộn.",
    frozenset(["Khách thể có Thất Sát tương khắc nhật chủ"]): "Thất Sát đến tương khắc với nhật chủ, công việc dễ gặp xung đột, mâu thuẫn, cần phải lưu ý.",
}

rule_map_by_base_column = {
    frozenset(): "Trụ tháng có Ấn tinh gặp khắc, công việc dễ gặp xung đột, mâu thuẫn.",
    frozenset(): "Trụ tháng có Ấn tinh gặp Tài khắc, công việc dễ gặp xung đột, mâu thuẫn, dễ gặp sai sót liên quan đến số liệu, giấy tờ",
    frozenset(): "Trụ tháng có Quan tinh gặp khắc, dễ mất lòng cấp trên hoặc quản lý trực tiếp, công việc dễ gặp xung đột, mâu thuẫn.",
}

rule_map_by_guest_column = {
    frozenset(): "Trụ khách thể là Ấn tinh, công việc tương đối nhiều và bận rộn, Thương Quan thấu can có nhiều ý tưởng, đầu óc nhạy bén nhưng cũng hay bay bổng.",
    frozenset(): "Trụ khách thể là Quan Ấn tương sinh, công việc tương đối nhiều và bận rộn, Chính Quan thấu can dễ được quý nhân tương trợ, ủng hộ.",
    frozenset(): "Trụ khách thể là Sát Ấn tương sinh, chăm chỉ làm việc sẽ đạt được thành công, công việc tương đối nhiều và bận rộn.",
    frozenset(): "Trụ khách thể là Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung, dễ vì lợi ích cá nhân mà mất đi cơ hội.",
    frozenset(): "Trụ khách thể là Kiếp Tài thấu can, lại được Ấn vượng, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.",
    frozenset(): "Trụ khách thể là Thực Thần thấu can dễ được người khác quý mến.",
    frozenset(): "Trụ khách thể là Tỷ Kiên thấu can, toạ Sát, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.",
    frozenset(): "Trụ khách thể là Tỷ Kiên thấu can, toạ Sát, công việc có sự mở rộng quan hệ, nhưng cũng dễ hao tài.",
    frozenset(): "Quan tinh song thể lực lượng vượng tướng, công việc tương đối nhiều và bận rộn, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.",
    frozenset(): "Tài sinh Quan, công việc và tài lộc cùng song hành mang lại nhiều cơ hội thăng tiến, phát triển."
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
    (True, "Ấn tinh nhiều"),
    (False, "khách có Trạch Mã"),
    (True, "Quan tinh thấu can"),
    # (True, "Quan tinh gặp xung khắc")
]

for bol, name in conditions:
    if name == 'khách có Văn Xương':
        conditions[conditions.index((bol, name))] = (False, name)

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
    """Chỉ lấy các tổ hợp điều kiện lớn nhất, loại bỏ các tổ hợp nhỏ nằm trong tổ hợp lớn."""
    matched_predictions = {}

    # Tìm tất cả các tổ hợp con hợp lệ trong rule_map
    for i in range(len(active_conditions), 0, -1):
        for subset in itertools.combinations(active_conditions, i):
            subset_frozen = frozenset(subset)
            if subset_frozen in rule_map:
                matched_predictions[subset_frozen] = rule_map[subset_frozen]

    # Loại bỏ các tổ hợp nhỏ nếu chúng nằm trong tổ hợp lớn hơn
    filtered_predictions = []
    sorted_keys = sorted(matched_predictions.keys(), key=len, reverse=True)  # Sắp xếp tổ hợp lớn trước

    for i, key in enumerate(sorted_keys):
        if any(key < larger_key for larger_key in sorted_keys[:i]):  # Kiểm tra nếu bị bao phủ bởi tổ hợp lớn hơn
            continue  # Bỏ qua tổ hợp nhỏ hơn
        filtered_predictions.append(matched_predictions[key])

    # Nếu không có kết quả nào khớp, trả về câu mặc định
    if not filtered_predictions:
        return ["Không có dự đoán cho trường hợp này"]

    return filtered_predictions

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
