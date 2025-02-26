# Danh sách các tổ hợp điều kiện và câu luận tương ứng
rule_map = {
    frozenset(["hình", "hại", "phá"]): "Quan tinh gặp hình, hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["hình", "hại"]): "Quan tinh gặp hình, hại, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["hình", "phá"]): "Quan tinh gặp hình, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, cẩn thận giấy tờ, số liệu, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["hại", "phá"]): "Quan tinh gặp hại, phá, công việc dễ gặp thị phi, sai sót, mất tập trung, tiểu nhân quấy phá, nên kiểm tra lại công việc trước khi hoàn thành.",
    frozenset(["hình"]): "Quan tinh gặp hình, có thể bị cản trở trong công việc, cần thận trọng khi ra quyết định.",
    frozenset(["hại"]): "Quan tinh gặp hại, dễ bị kẻ tiểu nhân công kích, cần chú ý lời ăn tiếng nói.",
    frozenset(["phá"]): "Quan tinh gặp phá, công việc dễ bị gián đoạn, nên có kế hoạch dự phòng.",
    frozenset(["Quan Ấn tương sinh"]): "Quan tinh gặp quan ấn tương sinh, công việc thuận lợi, dễ gặp sự giúp đỡ từ người khác.",
    frozenset(["Quan Ấn tương sinh", "có Văn Xương"]): "Quan tinh gặp quan ấn tương sinh, có Văn Xương, công việc thuận lợi, dễ gặp sự giúp đỡ từ người khác.",
    frozenset(["hình", "hại", "phá", "Quan Ấn tương sinh"]): "Quan tinh gặp hình, hại, phá nhưng có Quan Ấn tương sinh, công việc tuy có trở ngại nhưng vẫn có quý nhân giúp đỡ, có thể xoay chuyển tình thế.",
    frozenset(["Quan tinh thấu can gặp xung khắc"]): 'Quan tinh thấu can lại gặp xung, khắc, công việc dễ gặp trở ngại, khó khăn, thị phi nhiều, mâu thuẫn nhiều, cần phải lưu ý chuyện giấy tờ, các thủ tục pháp lý.',
    frozenset(["Quan tinh thấu can gặp xung khắc", "Quan Ấn tương sinh"]): 'Quan tinh tương sinh là tốt tuy nhiên vẫn tồn tại xung, khắc, công việc có sự thuận lợi nhất định nhưng cũng cần phải cẩn thận với những trở ngại, khó khăn.',
}

quan_tinh_in_hinh = False
quan_tinh_in_hai = False
quan_tinh_in_pha = False
quan_tinh_thau_can_gap_xung_khac = True
quan_an_tuong_sinh = True
co_van_xuong = False

column_hidden_thap_than = ['Chính Quan', 'Thất Sát']

# Điều kiện cần kiểm tra
conditions = [
    (quan_tinh_in_hinh, "hình"),
    (quan_tinh_in_hai, "hại"),
    (quan_tinh_in_pha, "phá"),
    (quan_an_tuong_sinh, "Quan Ấn tương sinh"),
    (co_van_xuong, "có Văn Xương"),
    (quan_tinh_thau_can_gap_xung_khac, "Quan tinh thấu can gặp xung khắc"),
]

# Lọc ra các điều kiện đúng
active_conditions = frozenset(name for cond, name in conditions if cond)
print(active_conditions)
predict = []
# Nếu có Chính Quan hoặc Thất Sát và có ít nhất một điều kiện trong số trên
if active_conditions:
    # Lấy câu luận tương ứng từ rule_map
    prediction = rule_map.get(active_conditions) or "Không có dự đoán cho trường hợp này"
    predict.append(prediction)

print(predict)
