from gan_util import GanUtil
from util import is_many_thap_than


def rule_func(variables: dict):
    bazi: dict = variables['bazi']
    result = []

    # menh_cung.have(("Chính Ấn", "Thiên Ấn")) and guest_can.is_khac(menh_cung)

    an_tinh_nhieu = is_many_thap_than(bazi, thap_than_to_count=("Chính Ấn", "Thiên Ấn"), only_count_primary=True)
    quan_tinh_nhieu = is_many_thap_than(bazi, thap_than_to_count=("Chính Quan", "Thiên Quan"), only_count_primary=True)

    if an_tinh_nhieu and variables["guest_have_trach_ma"]:
        result.append("Ấn tinh nhiều, lại có thêm Trạch Mã công việc có nhiều bận rộn, đi lại công tác nhiều, có thể làm nhiều việc một lúc.")

    if variables["guest_chi_in_hinh"] and variables["an_tinh_in_hinh"] and variables["an_tinh_in_pha"]:
        result.append("Ấn tinh gặp hình phá, công việc dễ g��p thị phi, xung đột, đổ vỡ, nên kiểm tra lại công việc trước khi hoàn thành.")

    if quan_tinh_nhieu:
        result.append("Quan tinh nhiều, công việc dễ gặp áp lực, cần phải lưu ý giữ gìn sức khỏe, tinh thần, biết cân bằng công việc và cuộc sống.")

    if variables["an_tinh_nhieu"]:
        result.append("Ấn tinh nhiều, công việc có nhiều bận rộn, có thể làm nhiều việc một lúc.")

    if variables["an_tinh_gap_khac"]:
        result.append("Ấn tinh gặp khắc, công việc dễ gặp trở ngại, xung đột, sai sót, mất tập trung, nên kiểm tra lại công việc trước khi hoàn thành.")

    if variables["an_tinh_gap_pha"]:
        result.append("Ấn tinh gặp phá, công việc dễ gặp thị phi, xung đột, đổ vỡ, nên kiểm tra lại công việc trước khi hoàn thành.")

    if variables["tru_thang_have_that_sat_gap_khac"]:
        result.append("Trụ tháng có Thất Sát gặp khắc, công việc dễ có thị phi, cần phải lưu ý.")

    if variables["tru_thang_have_chinh_quan_gap_khac"]:
        result.append("Trụ tháng có Chính Quan gặp khắc, công việc dễ có thị phi, biến động công việc.")

    if variables["tru_thang_have_an_tinh_gap_khac"]:
        result.append("Trụ tháng có Ấn tinh gặp khắc, công việc dễ gặp xung đột, mâu thuẫn.")

    if variables["month_thap_than"] in ("Chính Ấn", "Thiên Ấn") and GanUtil.is_khac(variables["guest_can"], variables["month_can"]):
        result.append("Tháng có Ấn tinh gặp khắc, công việc dễ gặp xung đột, mâu thuẫn.")

    if variables["guest_can"] in ("Chính Tài", "Thiên Tài") and variables["day_master"] in ("Chính Ấn", "Thiên Ấn"):
        result.append("Tài khắc Ấn, công việc dễ gặp sai sót, mất tập trung.")

    if variables["guest_can"] == "Chính Quan" and GanUtil.is_hop(variables["guest_can"], variables["day_master"]) and (variables["guest_have_tuong_tinh"] or variables["guest_have_van_xuong"]):
        if variables["guest_have_tuong_tinh"] and variables["guest_have_van_xuong"]:
            result.append("Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Văn Xương, Tướng Tinh, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.")
        elif variables["guest_have_tuong_tinh"]:
            result.append("Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Tướng Tinh, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.")
        elif variables["guest_have_van_xuong"]:
            result.append("Chính Quan đến hợp với nhật chủ, lại gặp được cát tinh Văn Xương, công việc gặp được thuận lợi, hợp tác vui vẻ, cấp trên quý mến, có cơ hội thăng tiến.")

    return None
