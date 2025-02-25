import re

from zhi_util import check_zhi_interaction_priority


def load_rules_from_text(file_path):
    """
    Đọc quy tắc từ file text và chuyển đổi thành danh sách có cấu trúc, đồng thời sắp xếp theo số lượng tham số giảm dần.
    :param file_path: Đường dẫn đến file text chứa các quy tắc.
    :return: Danh sách quy tắc dạng {"condition": ..., "result": ...}, sắp xếp theo số lượng tham số.
    """
    rules = []
    pattern = re.compile(r"(.+?)\s*then\s*(.+)")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                condition = match.group(1).strip()
                result = match.group(2).strip()
                param_count = condition.count(" ") + 1  # Đếm số lượng tham số dựa trên dấu cách
                rules.append({"condition": condition, "result": result, "param_count": param_count})

    # Sắp xếp rule theo số lượng tham số giảm dần
    rules.sort(key=lambda r: r["param_count"], reverse=True)

    return rules

def evaluate_rules(rule_file, variables):
    """
    Kiểm tra các quy tắc từ file text và trả về kết quả nếu điều kiện đúng.
    :param rule_file: Đường dẫn đến file text chứa các quy tắc.
    :param variables: Dictionary chứa giá trị của các biến (x, y, a, b,...).
    :return: Kết quả nếu thỏa mãn, None nếu không có quy tắc nào khớp.
    """
    rules = load_rules_from_text(rule_file)

    result = []
    for rule in rules:
        try:
            if eval(rule["condition"], {}, variables):
                result.append(rule["result"])
        except Exception as e:
            print(f"Lỗi khi đánh giá điều kiện '{rule['condition']}': {e}")

    return result

# Ví dụ: Giá trị biến hiện có
variables = {
    "column": 'year',
    "thien_khac": True,
    "dia_xung": False,
    "column_hidden_thap_than": ['Chính Ấn', 'Thiên Ấn'],
    "guest_chi": 'Mão',
    "chi": "Tý",
    "check_zhi_interaction_priority": check_zhi_interaction_priority,
    "an_tinh_gap_pha": True,
    "an_tinh_gap_hinh": True
}

# Kiểm tra quy tắc
result = evaluate_rules("rules.txt", variables)
print("Kết quả:", result)
