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
        "combination": ("Kỷ"),
        "interactions": {
            "Tương khắc": "Mậu",
            "Tương hợp": "Kỷ",
            "Tương xung": "Canh"
        }
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
        "combination": ("Canh"),
        "interactions": {
            "Tương khắc": "Kỷ",
            "Tương hợp": "Canh",
            "Tương xung": "Tân"
        }
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
        "combination": ("Tân"),
        "interactions": {
            "Tương khắc": "Canh",
            "Tương hợp": "Tân",
            "Tương xung": "Nhâm"
        }
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
        "combination": ("Nhâm"),
        "interactions": {
            "Tương khắc": "Tân",
            "Tương hợp": "Nhâm",
            "Tương xung": "Quý"
        }
    },
    "Mậu": {
        "name": "Mậu",
        "polarity": "Dương",
        "element": "Thổ",
        "ten_gods": {
            "Thiên Ấn": "Bính",
            "Chính Ấn": "Đinh",
            "Thiên Tài": "Nhâm",
            "Chính Tài": "Quý",
            "Thất Sát": "Giáp",
            "Chính Quan": "Ất",
            "Tỷ Kiên": "Mậu",
            "Kiếp Tài": "Kỷ",
            "Thực Thần": "Canh",
            "Thương Quan": "Tân"
        },
        "generation_cycle": ("Canh", "Tân"),
        "control_cycle": ("Nhâm", "Quý"),
        "combination": ("Quý"),
        "interactions": {
            "Tương khắc": "Nhâm",
            "Tương hợp": "Quý",
            "Tương xung": None
        }
    },
    "Kỷ": {
        "name": "Kỷ",
        "polarity": "Âm",
        "element": "Thổ",
        "ten_gods": {
            "Thiên Ấn": "Đinh",
            "Chính Ấn": "Bính",
            "Thiên Tài": "Quý",
            "Chính Tài": "Nhâm",
            "Thất Sát": "Ất",
            "Chính Quan": "Giáp",
            "Tỷ Kiên": "Kỷ",
            "Kiếp Tài": "Mậu",
            "Thực Thần": "Tân",
            "Thương Quan": "Canh"
        },
        "generation_cycle": ("Canh", "Tân"),
        "control_cycle": ("Nhâm", "Quý"),
        "combination": ("Giáp"),
        "interactions": {
            "Tương khắc": "Quý",
            "Tương hợp": "Giáp",
            "Tương xung": None
        }
    },
    "Canh": {
        "name": "Canh",
        "polarity": "Dương",
        "element": "Kim",
        "ten_gods": {
            "Thiên Ấn": "Mậu",
            "Chính Ấn": "Kỷ",
            "Thiên Tài": "Giáp",
            "Chính Tài": "Ất",
            "Thất Sát": "Bính",
            "Chính Quan": "Đinh",
            "Tỷ Kiên": "Canh",
            "Kiếp Tài": "Tân",
            "Thực Thần": "Nhâm",
            "Thương Quan": "Quý"
        },
        "generation_cycle": ("Nhâm", "Quý"),
        "control_cycle": ("Giáp", "Ất"),
        "combination": ("Ất"),
        "interactions": {
            "Tương khắc": "Giáp",
            "Tương hợp": "Ất",
            "Tương xung": "Giáp"
        }
    },
    "Tân": {
        "name": "Tân",
        "polarity": "Âm",
        "element": "Kim",
        "ten_gods": {
            "Thiên Ấn": "Kỷ",
            "Chính Ấn": "Mậu",
            "Thiên Tài": "Ất",
            "Chính Tài": "Giáp",
            "Thất Sát": "Đinh",
            "Chính Quan": "Bính",
            "Tỷ Kiên": "Tân",
            "Kiếp Tài": "Canh",
            "Thực Thần": "Quý",
            "Thương Quan": "Nhâm"
        },
        "generation_cycle": ("Nhâm", "Quý"),
        "control_cycle": ("Giáp", "Ất"),
        "combination": ("Bính"),
        "interactions": {
            "Tương khắc": "Ất",
            "Tương hợp": "Bính",
            "Tương xung": "Ất"
        }
    },
    "Nhâm": {
        "name": "Nhâm",
        "polarity": "Dương",
        "element": "Thuỷ",
        "ten_gods": {
            "Thiên Ấn": "Canh",
            "Chính Ấn": "Tân",
            "Thiên Tài": "Bính",
            "Chính Tài": "Đinh",
            "Thất Sát": "Mậu",
            "Chính Quan": "Kỷ",
            "Tỷ Kiên": "Nhâm",
            "Kiếp Tài": "Quý",
            "Thực Thần": "Giáp",
            "Thương Quan": "Ất"
        },
        "generation_cycle": ("Giáp", "Ất"),
        "control_cycle": ("Bính", "Đinh"),
        "combination": ("Đinh"),
        "interactions": {
            "Tương khắc": "Bính",
            "Tương hợp": "Đinh",
            "Tương xung": "Bính"
        }
    },
    "Quý": {
        "name": "Quý",
        "polarity": "Âm",
        "element": "Thuỷ",
        "ten_gods": {
            "Thiên Ấn": "Tân",
            "Chính Ấn": "Canh",
            "Thiên Tài": "Đinh",
            "Chính Tài": "Bính",
            "Thất Sát": "Kỷ",
            "Chính Quan": "Mậu",
            "Tỷ Kiên": "Quý",
            "Kiếp Tài": "Nhâm",
            "Thực Thần": "Ất",
            "Thương Quan": "Giáp"
        },
        "generation_cycle": ("Giáp", "Ất"),
        "control_cycle": ("Bính", "Đinh"),
        "combination": ("Mậu"),
        "interactions": {
            "Tương khắc": "Đinh",
            "Tương hợp": "Mậu",
            "Tương xung": "Đinh"
        }
    }
}