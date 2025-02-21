# -*- encoding: utf-8 -*-

from config.zhi import ZHI
from config.interaction_config import THREE_COMBINATIONS, TWO_COMBINATIONS, TWO_CLASS, TWO_CONTROL, TWO_HARM, THREE_PUNISHMENT, TWO_PUNISHMENT, HALF_THREE_COMBINATIONS, TWO_DESTRUCTION

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
    
    result = [];
    
            
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
    
    return result       