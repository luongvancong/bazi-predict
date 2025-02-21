# -*- encoding: utf-8 -*-

# Tam hợp
THREE_COMBINATIONS = (
    ("Thân", "Tý", "Thìn"),
    ("Dần", "Ngọ", "Tuất"),
    ("Hợi", "Mão", "Mùi"),
    ("Tị", "Dậu", "Sửu")
)

# Bán tam hợp
HALF_THREE_COMBINATIONS = (
    ("Thân", "Tý"),
    ("Tý", "Thìn"),
    ("Dần", "Ngọ"), 
    ("Ngọ", "Tuất"),
    ("Hợi", "Mão"), 
    ("Mão", "Mùi"),
    ("Tị", "Dậu"), 
    ("Dậu", "Sửu")
)

# Tương hợp
TWO_COMBINATIONS =(
    ("Tý", "Sửu"),
    ("Dần", "Hợi"),
    ("Thân", "Tị"),
    ("Ngọ", "Mùi"),
    ("Thìn", "Dậu"),
    ("Mão", "Tuất")
)

# Tương xung
TWO_CLASS = (
    ("Ngọ", "Tý"),
    ("Mão", "Dậu"),
    ("Dần", "Thân"),
    ("Tị", "Hợi"),
    ("Tuất", "Thìn"),
    ("Mùi", "Sửu")
)

# Tương khắc
TWO_CONTROL = (
    ("Tý", "Ngọ"),
    ("Dậu", "Mão"),
    ("Thân", "Dần"),
    ("Hợi", "Tị"),
    ("Thìn", "Tuất"),
    ("Sửu", "Mùi")
)

# Tương hại
TWO_HARM = (
    ("Tý", "Mùi"),
    ("Mão", "Thìn"),
    ("Dần", "Tị"),
    ("Thân", "Hợi"),
    ("Dậu", "Tuất"),
    ("Sửu", "Ngọ")
)

# Tam hình
THREE_PUNISHMENT = (
    ("Dần", "Tị", "Thân"),
    ("Sửu", "Tuất", "Mùi")
)

# Tương hình
TWO_PUNISHMENT = (
    ("Tý", "Mão"),
    ("Thìn", "Thìn"),
    ("Ngọ", "Ngọ"),
    ("Dậu", "Dậu"),
    ("Hợi", "Hợi")
)

# Tương phá
TWO_DESTRUCTION = (
    ("Tý", "Dậu"),
    ("Mão", "Ngọ"),
    ("Dần", "Hợi"),
    ("Thân", "Tị"),
    ("Tuất", "Mùi"),
    ("Sửu", "Thìn")
)

# Kiểm tra theo thứ tự: Tam hình, nhị hình, hại, phá, khắc, xung, tam hợp, nhị hợp