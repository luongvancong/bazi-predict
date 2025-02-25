# -*- encoding: utf-8 -*-

from career import career_predict_by_guest
from config.gan import GAN
from util import find_thap_than, get_all_zhi_interaction
from zhi_util import get_hidden_gans, check_zhi_interaction_priority

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
bazi = {
    "year": ("Mậu", "Thìn"),
    "month": ("Quý", "Hợi"),
    "day": ("Canh", "Ngọ"),
    "hour": ("Giáp", "Thân"),
    "dai_van": ("Kỷ", "Mùi"),
    "luu_nien": ("Ất", "Tị"),
    "luu_nguyet": ("Mậu", "Dần")
}

print('---------Mậu Dần---------')
guest = ("Mậu", "Dần")
print(career_predict_by_guest(bazi, "luu_nguyet"))
print("\n")

# print (check_zhi_interaction_priority(("Thân", "Mão")))
