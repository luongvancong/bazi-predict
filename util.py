from itertools import combinations

from config.zhi import ZHI
from gan import GAN
from zhi_util import check_zhi_interaction_priority

def get_gan_from_bazi(bazi: list):
    return bazi[0], bazi[2], bazi[4], bazi[6]

def get_zhi_from_bazi(bazi: list):
    return bazi[1], bazi[3], bazi[5], bazi[7]

def group_pairs(lst: list):
    return list(combinations(lst, 2))

def group_three(lst: list):
    return list(combinations(lst, 3))

def zhi_group_pairs(bazi):
    result = []
    columns = []
    for column in bazi.keys():
        columns.append(column)
    pairs = group_pairs(columns)
    
    for pair in pairs:
        zhiList = []
        for column in pair:
            zhiList.append(bazi[column][1])
        result.append({
            "columns": pair,
            "zhi": zhiList
        })
    
    return result


def get_all_zhi_interaction(bazi):
    
    result = []
    
    threes = group_three(bazi.keys())
    for three in threes:
        zhiList = []
        for column in three:
            zhiList.append(bazi[column][1])
        result.append({
            "columns": three,
            "zhi": zhiList
        })
    
    pairs = group_pairs(bazi.keys())
    for pair in pairs:
        zhiList = []
        for column in pair:
            zhiList.append(bazi[column][1])
                    
        result.append({
            "columns": pair,
            "zhi": zhiList
        })
        

    for rs in result:
        interaction = check_zhi_interaction_priority(rs["zhi"])
        if len(interaction) > 0:
            print({
                "columns": rs["columns"],
                "zhi": rs["zhi"],
                "priority": check_zhi_interaction_priority(rs["zhi"])
            })
        
    return result

def find_thap_than(guest_can, host_can):
    ten_gods = GAN[host_can]["ten_gods"]
    for thap_than, can in ten_gods.items():
        if can == guest_can:
            return thap_than
    
    return None

def find_gan_interaction(guest_can, host_can):
    interactions = GAN[guest_can]["interactions"]
    for interaction, gan in interactions.items():
        if host_can == gan:
            return interaction
    return None

def get_hidden_gans(zhi):
    return ZHI[zhi]["hidden_gans"]