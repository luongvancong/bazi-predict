# -*- encoding: utf-8 -*-

# Tam hội
THREE_GROUP = (
    ("Thân", "Dậu", "Tuất"),
    ("Dần", "Mão", "Thìn"),
    ("Hợi", "Tý", "Sửu"),
    ("Tị", "Ngọ", "Mùi")
)

THREE_GROUP_DICT = (
    {"name": "Tam hội Kim", "elemental": "Kim", "zhi": ("Thân", "Dậu", "Tuất")},
    {"name": "Tam hội Mộc", "elemental": "Mộc", "zhi": ("Dần", "Mão", "Thìn")},
    {"name": "Tam hội Thủy", "elemental": "Thủy", "zhi": ("Hợi", "Tý", "Sửu")},
    {"name": "Tam hội Hỏa", "elemental": "Hỏa", "zhi": ("Tị", "Ngọ", "Mùi")}
)

# Tam hợp
THREE_COMBINATIONS = (
    ("Thân", "Tý", "Thìn"),
    ("Dần", "Ngọ", "Tuất"),
    ("Hợi", "Mão", "Mùi"),
    ("Tị", "Dậu", "Sửu")
)

THREE_COMBINATION_DICT = (
    {"name": "Tam hợp Kim", "elemental": "Kim", "zhi": ("Tị", "Dậu", "Sửu")},
    {"name": "Tam hợp Mộc", "elemental": "Mộc", "zhi": ("Hợi", "Mão", "Mùi")},
    {"name": "Tam hợp Thủy", "elemental": "Thủy", "zhi": ("Thân", "Tý", "Thìn")},
    {"name": "Tam hợp Hỏa", "elemental": "Hỏa", "zhi": ("Dần", "Ngọ", "Tuất")}
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

# Ám hợp
TWO_ZHI_HIDDEN_COMBINATION = (
    ("Thân", "Mão"),
    ("Dần", "Sửu"),
    ("Hợi", "Ngọ")
)

# Kiểm tra theo thứ tự: Tam hình, nhị hình, hại, phá, khắc, xung, tam hợp, nhị hợp