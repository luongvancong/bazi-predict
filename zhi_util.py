# -*- encoding: utf-8 -*-

from config.interaction_config import THREE_COMBINATIONS, TWO_COMBINATIONS, TWO_CLASS, TWO_CONTROL, TWO_HARM, \
    THREE_PUNISHMENT, TWO_PUNISHMENT, HALF_THREE_COMBINATIONS, TWO_DESTRUCTION, THREE_GROUP, THREE_GROUP_DICT, \
    TWO_ZHI_HIDDEN_COMBINATION, THREE_COMBINATION_DICT
from config.zhi import ZHI


def get_interaction(guest: str, host: list):
    interaction = ZHI[guest]["interaction"]
    result = []
    for key, value in interaction.items():
        if len(host) == 1:
            if host[0] in value:
                result.append({
                    "interaction": f"{guest} {key} {host[0]}",
                    "host": host,
                    "host_index": [0],
                    "guest": guest,
                })
                return result
        else:
            if host[0] in value and host[1] in value:
                result.append({
                    "interaction": f"{guest} {key} {host[0]} {host[1]}",
                    "host": host,
                    "host_index": [0, 1],
                    "guest": guest,
                })
                return result
            else:
                for h in host:
                    if h in value:
                        result.append({
                            "interaction": f"{guest} {key} {h}",
                            "host": h,
                            "host_index": [host.index(h)],
                            "guest": guest,
                        })
    return result
    

def check_zhi_interaction_priority(lst: tuple): 
    
    for value in THREE_PUNISHMENT:
        if len(value) == len(lst) and set(value) == set(lst):
            return ["Tam hình"]
    
    result = []
    
            
    for value in TWO_PUNISHMENT:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương hình")
            break
        
    for value in TWO_HARM:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương hại")
            break
        
    for value in TWO_DESTRUCTION:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương phá")
            break
            
    for value in TWO_CLASS:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương xung")
            break
    
    for value in TWO_CONTROL:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương khắc")
            break    
            
    for value in THREE_COMBINATIONS:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tam hợp")
            break
    
    for value in TWO_COMBINATIONS:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Tương hợp")
            break
            
    for value in HALF_THREE_COMBINATIONS:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Bán tam hợp")
            break

    for value in TWO_ZHI_HIDDEN_COMBINATION:
        if len(value) == len(lst) and set(value) == set(lst):
            result.append("Ám hợp")
            break
    
    return result

def is_tam_hoi(a, b, c):
    for value in THREE_GROUP:
        if a in value and b in value and c in value and a != b and b != c and a != c:
            return True
    return False

def is_tam_hop(a, b, c):
    for value in THREE_COMBINATIONS:
        if a in value and b in value and c in value and a != b and b != c and a != c:
            return True
    return False

def is_nhi_hop(a, b):
    for value in TWO_COMBINATIONS:
        if a in value and b in value and a != b:
            return True
    return False

def is_tuong_hai(a, b):
    for value in TWO_HARM:
        if a in value and b in value and a != b:
            return True
    return False

def is_tuong_pha(a, b):
    for value in TWO_DESTRUCTION:
        if a in value and b in value and a != b:
            return True
    return False

def is_tuong_xung(a, b):
    for value in TWO_CLASS:
        if a in value and b in value and a != b:
            return True
    return False

def is_tuong_khac(a, b):
    for value in TWO_CONTROL:
        if a in value and b in value and a != b:
            return True
    return False

def is_tam_hinh(a, b, c):
    for value in THREE_PUNISHMENT:
        if a in value and b in value and c in value and a != b and b != c and a != c:
            return True
    return False

def is_tu_hinh(a, b):
    for value in TWO_PUNISHMENT:
        if a in value and b in value and a == b:
            return True
    return False

def get_zhi_polarity(zhi):
    return ZHI[zhi]["polarity"]

def get_hidden_gans(zhi):
    return ZHI[zhi]["hidden_gans"]

def get_tam_hoi_elemental(zhi):
    for value in THREE_GROUP_DICT:
        zhi_list = value['zhi']
        if zhi in zhi_list:
            return value['elemental']
    return None

def get_tam_hop_elemental(zhi):
    for value in THREE_COMBINATION_DICT:
        zhi_list = value['zhi']
        if zhi in zhi_list:
            return value['elemental']
    return None