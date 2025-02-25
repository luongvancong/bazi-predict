# -*- encoding: utf-8 -*-

from config.gan import GAN
from util import find_thap_than, get_all_zhi_interaction
from zhi_util import get_hidden_gans


def predict_bazi(bazi: list, thai_nguyen: list, menh_cung: list, than_cung: list, guest_column: list):
    yearGan = bazi[0]
    yearZhi = bazi[1]
    monthGan = bazi[2]
    monthZhi = bazi[3]
    dayGan = bazi[4]
    dayZhi = bazi[5]
    hourGan = bazi[6]
    hourZhi = bazi[7]
    
    
    
    return None


def get_thap_than(host_can: str, guest_can: str):
    print(GAN[host_can]["ten_gods"])
    ten_gods = GAN[host_can]["ten_gods"].items()
    for god, can in ten_gods:
        if can == guest_can:
            return god
    return None
    

bazi = {
    "year": ("Nhâm", "Thân"),
    "month": ("Giáp", "Thìn"),
    "day": ("Bính", "Thìn"),
    "hour": ("Tân", "Mão"),
    "dai_van": ("Canh", "Tý"),
    "luu_nien": ("Ất", "Tị")
}

thai_nguyen = ["Đinh", "Sửu"]
menh_cung = ["Mậu", "Tý"]
than_cung = ["Nhâm", "Ngọ"]
guest_column = ["Mậu", "Dần"]

# print(get_thap_than("Giáp", "Nhâm"))

# print(get_interaction("Tý", ["Thìn", "Mão"]))

# predict_bazi(bazi, thai_nguyen, menh_cung, than_cung, guest_column);


# print(group_pairs(get_zhi_from_bazi(bazi)))
# print(group_three(get_zhi_from_bazi(bazi)))

print('---------------------------------------')
# pairs = group_pairs(bazi)
# for pair in pairs:
#     interaction = get_interaction("Tý", list(pair))
#     if (len(interaction) > 0):
#         print(interaction)
get_all_zhi_interaction(bazi)


# print(check_zhi_interaction_priority(["Thân", "Tị"])

print(find_thap_than("Kỷ", "Canh"))


print('---------START HIDDEN GAN---------')
print(get_hidden_gans("Tý"))
print('---------END HIDDEN GAN-----------')