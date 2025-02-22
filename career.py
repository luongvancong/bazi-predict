# -*- encoding: utf-8 -*-

from util import find_gan_interaction, find_thap_than


CAREER_PREDICTION = [
    {
        "condition": "Ấn tinh nhiều",
        "description": "Công việc có nhiều bận rộn, có thể làm nhiều việc một lúc"
    },
    {
        "condition": "Ấn tinh gặp khắc",
        "description": "Công việc dễ gặp xung đột, mâu thuẫn",
        "modifier": {
            "Tài khắc": "Công việc dễ gặp xung đột, mâu thuẫn liên quan đến các vấn đề số liệu, tài chính, kế toán"
        }
    }
]

def career_predict_by_guest(bazi, guest: tuple):
    guest_can = guest[0]
    guest_chi = guest[1]
    
    predict = []
    
    for column, (can, chi) in bazi.items():
        day_master = bazi['day'][0]
        
        guest_thap_than = find_thap_than(guest_can, day_master)
        interaction = find_gan_interaction(guest_can, can)
        column_can_thap_than = find_thap_than(can, day_master)
        
        print(column, interaction, column_can_thap_than)
        
        if interaction == 'Tương khắc' and column_can_thap_than == 'Thất Sát' and column == 'month' :
            predict.append('Trụ tháng có Thất Sát gặp khắc, công việc dễ có thị phi, cần phải lưu ý')
            
        if interaction == 'Tương khắc' and column_can_thap_than == 'Chính Quan' and column == 'month' :
            predict.append('Trụ tháng có Chính Quan gặp khắc, công việc dễ có thị phi, biến động công việc') 
            
    
    return predict