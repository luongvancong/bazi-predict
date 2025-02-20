# -*- encoding: utf-8 -*-

GAN = {
    "Giáp": {
        "name": "Giáp",
        "polarity": "Dương",
        "element": "Mộc",
        "ten_gods": {
            "Thiên Ấn": "Nhâm",
            "Chính Ấn": "Quý",
            "Thiên Tài": "Mậu",
            "Chính Tài": "Kỷ",
            "Thất Sát": "Canh",
            "Chính Quan": "Tân",
            "Tỷ Kiên": "Giáp",
            "Kiếp Tài": "Ất",
            "Thực Thần": "Bính",
            "Thương Quan": "Đinh"
        },
        "generation_cycle": ("Bính", "Đinh"),
        "control_cycle": ("Mậu", "Kỷ"),
        "combination": ("Kỷ")
    },
    "Ất": {
        "name": "Ất",
        "polarity": "Âm",
        "element": "Mộc",
        "ten_gods": {
            "Thiên Ấn": "Quý",
            "Chính Ấn": "Nhâm",
            "Thiên Tài": "Kỷ",
            "Chính Tài": "Mậu",
            "Thất Sát": "Tân",
            "Chính Quan": "Canh",
            "Tỷ Kiên": "Ất",
            "Kiếp Tài": "Giáp",
            "Thực Thần": "Đinh",
            "Thương Quan": "Bính"
        },
        "generation_cycle": ("Bính", "Đinh"),
        "control_cycle": ("Mậu", "Kỷ"),
        "combination": ("Canh")
    },
    "Bính": {
        "name": "Bính",
        "polarity": "Dương",
        "element": "Hỏa",
        "ten_gods": {
            "Thiên Ấn": "Giáp",
            "Chính Ấn": "Ất",
            "Thiên Tài": "Canh",
            "Chính Tài": "Tân",
            "Thất Sát": "Nhâm",
            "Chính Quan": "Quý",
            "Tỷ Kiên": "Bính",
            "Kiếp Tài": "Đinh",
            "Thực Thần": "Mậu",
            "Thương Quan": "Kỷ"
        },
        "generation_cycle": ("Mậu", "Kỷ"),
        "control_cycle": ("Canh", "Tân"),
        "combination": ("Tân")
    },
    "Đinh": {
        "name": "Đinh",
        "polarity": "Âm",
        "element": "Hỏa",
        "ten_gods": {
            "Thiên Ấn": "Ất",
            "Chính Ấn": "Giáp",
            "Thiên Tài": "Tân",
            "Chính Tài": "Canh",
            "Thất Sát": "Quý",
            "Chính Quan": "Giáp",
            "Tỷ Kiên": "Đinh",
            "Kiếp Tài": "Bính",
            "Thực Thần": "Kỷ",
            "Thương Quan": "Mậu"
        },
        "generation_cycle": ("Mậu", "Kỷ"),
        "control_cycle": ("Canh", "Tân"),
        "combination": ("Nhâm")
    }
}