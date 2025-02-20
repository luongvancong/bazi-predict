# -*- encoding: utf-8 -*-

from gan import GAN

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
    

bazi = ["Canh", "Ngọ", "Bính", "Tuất", "Nhâm", "Tuất", "Đinh", "Mùi"]
thai_nguyen = ["Đinh", "Sửu"]
menh_cung = ["Mậu", "Tý"]
than_cung = ["Nhâm", "Ngọ"]
guest_column = ["Canh", "Dần"]

print(get_thap_than("Giáp", "Nhâm"))

predict_bazi(bazi, thai_nguyen, menh_cung, than_cung, guest_column);