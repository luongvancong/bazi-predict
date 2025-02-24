# -*- encoding: utf-8 -*-

from career import career_predict_by_guest
from config.gan import GAN
from util import find_thap_than, get_all_zhi_interaction
from zhi_util import get_hidden_gans, check_zhi_interaction_priority

bazi = {
    "year": ("Nhâm", "Thân"),
    "month": ("Giáp", "Thìn"),
    "day": ("Bính", "Thìn"),
    "hour": ("Tân", "Mão"),
    "dai_van": ("Canh", "Tý"),
    "luu_nien": ("Ất", "Tị")
}

print('---------Nhâm Ngọ---------')
guest = ("Nhâm", "Ngọ")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Quý Mùi---------')
guest = ("Quý", "Mùi")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Giáp Thân---------')
guest = ("Giáp", "Thân")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Ất Dậu---------')
guest = ("Ất", "Dậu")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Bính Tuất---------')
guest = ("Bính", "Tuất")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Đinh Hợi---------')
guest = ("Đinh", "Hợi")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Mậu Tý---------')
guest = ("Mậu", "Tý")
print(career_predict_by_guest(bazi, guest))
print("\n")

print('---------Kỷ Sửu---------')
guest = ("Kỷ", "Sửu")
print(career_predict_by_guest(bazi, guest))
print("\n")

# print (check_zhi_interaction_priority(("Thân", "Mão")))