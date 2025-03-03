from career_conditions_collector import CareerConditionCollector

bazi = {
    "year": ("Ất", "Hợi"),
    "month": ("Nhâm", "Thân"),
    "day": ("Nhâm", "Tuất"),
    "hour": ("Canh", "Thân"),
    # "thai_nguyen": ("Đinh", "Sửu"),
    # "menh_cung": ("Đinh", "Hợi"),
    # "than_cung": ("Quý", "Mùi"),
    # "dai_van": ("Quý", "Mùi"),
    "luu_nien": ("Ất", "Tị"),
    "luu_nguyet": ('Mậu', 'Dần')
}

collector = CareerConditionCollector(bazi, guest='luu_nguyet')
# print(bazi['year'][0])
# print(f"{bazi['year'][0].ljust(8)}    {bazi['month'][0].ljust(8)}   {bazi['day'][0].ljust(8)}    {bazi['hour'][0].ljust(8)}  {bazi['luu_nguyet'][0].ljust(8)}")
# print(f"{bazi['year'][1].ljust(8)}    {bazi['month'][1].ljust(8)}   {bazi['day'][1].ljust(8)}    {bazi['hour'][1].ljust(8)}  {bazi['luu_nguyet'][1].ljust(8)}")

print('----------------DEBUG----------------------')
collector.debug()