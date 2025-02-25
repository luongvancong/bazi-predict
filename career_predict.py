# -*- encoding: utf-8 -*-

from predict.career import career_predict_by_guest

print('---- RECORD 39-----')
bazi = {
    "year": ("Nhâm", "Thân"),
    "month": ("Giáp", "Thìn"),
    "day": ("Bính", "Thìn"),
    "hour": ("Tân", "Mão"),
    "dai_van": ("Canh", "Tý"),
    "luu_nien": ("Ất", "Tị")
}

# print('---------Mậu Dần---------')
# guest = ("Mậu", "Dần")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Kỷ Mão---------')
# guest = ("Kỷ", "Mão")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Canh Thìn---------')
# guest = ("Canh", "Thìn")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Tân Tị---------')
# guest = ("Tân", "Tị")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Nhâm Ngọ---------')
# guest = ("Nhâm", "Ngọ")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Quý Mùi---------')
# guest = ("Quý", "Mùi")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Giáp Thân---------')
# guest = ("Giáp", "Thân")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Ất Dậu---------')
# guest = ("Ất", "Dậu")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Bính Tuất---------')
# guest = ("Bính", "Tuất")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Đinh Hợi---------')
# guest = ("Đinh", "Hợi")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Mậu Tý---------')
# guest = ("Mậu", "Tý")
# print(career_predict_by_guest(bazi, guest))
# print("\n")
#
# print('---------Kỷ Sửu---------')
# guest = ("Kỷ", "Sửu")
# print(career_predict_by_guest(bazi, guest))
# print("\n")

print('----- RECORD 38----')


months = (
    ("Mậu", "Dần"),
    ("Kỷ", "Mão"),
    ("Canh", "Thìn"),
    ("Tân", "Tị"),
    ("Nhâm", "Ngọ"),
    ("Quý", "Mùi"),
    ("Giáp", "Thân"),
    ("Ất", "Dậu"),
    ("Bính", "Tuất"),
    ("Đinh", "Hợi"),
    ("Mậu", "Tý"),
    ("Kỷ", "Sửu")
)

# for month in months:
#     bazi = {
#         "year": ("Mậu", "Thìn"),
#         "month": ("Quý", "Hợi"),
#         "day": ("Canh", "Ngọ"),
#         "hour": ("Giáp", "Thân"),
#         "dai_van": ("Kỷ", "Mùi"),
#         "luu_nien": ("Ất", "Tị"),
#         "luu_nguyet": month
#     }
#     print(f'---------{" ".join(month)}---------')
#     print(career_predict_by_guest(bazi, "luu_nguyet"))
#     print("\n")

# bazi = {
#         "year": ("Ất", "Hợi"),
#         "month": ("Bính", "Tuất"),
#         "day": ("Giáp", "Tý"),
#         "hour": ("Nhâm", "Thân"),
#     }
# than_sat = ThanSat(bazi)
# print_message(than_sat.find_luc_giap_khong_vong())

print('----- RECORD 25----')
for month in months:
    bazi = {
        "year": ("Ất", "Hợi"),
        "month": ("Bính", "Tuất"),
        "day": ("Giáp", "Tuất"),
        "hour": ("Nhâm", "Thân"),
        "thai_nguyen": ("Đinh", "Sửu"),
        "menh_cung": ("Đinh", "Hợi"),
        "than_cung": ("Quý", "Mùi"),
        "dai_van": ("Quý", "Mùi"),
        "luu_nien": ("Ất", "Tị"),
        "luu_nguyet": month
    }
    print(f'---------{" ".join(month)}---------')
    print(career_predict_by_guest(bazi, "luu_nguyet"))
    print("\n")

# print (check_zhi_interaction_priority(("Thân", "Mão")))
