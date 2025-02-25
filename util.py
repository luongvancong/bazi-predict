import inspect
from itertools import combinations
from config.zhi import ZHI
from config.gan import GAN
from zhi_util import check_zhi_interaction_priority, get_hidden_gans


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

def get_hidden_thap_than(zhi, day_master):
    hidden_gans = get_hidden_gans(zhi)
    hidden_thap_than = []
    for gan in hidden_gans:
        thap_thap = find_thap_than(gan, day_master)
        hidden_thap_than.append(thap_thap)
    return hidden_thap_than

def count_all_thap_than(bazi: dict, thap_than_to_count: tuple = (), only_count_primary: bool = False):
    if len(thap_than_to_count) > 0:
        count = 0
        day_master = bazi['day'][0]
        for column, (can, chi) in bazi.items():
            if column == 'day':
                hidden_thap_than = get_hidden_thap_than(chi, day_master)
                if only_count_primary:
                    hidden_thap_than = [hidden_thap_than[0]]
                for h in hidden_thap_than:
                    if h in thap_than_to_count:
                        count += 1
                continue
            can_thap_than = find_thap_than(can, day_master)
            hidden_thap_than = get_hidden_thap_than(chi, day_master)
            if only_count_primary:
                hidden_thap_than = [hidden_thap_than[0]]
            if can_thap_than in thap_than_to_count:
                count += 1
            for h in hidden_thap_than:
                if h in thap_than_to_count:
                    count += 1
        return count
    return 0

def is_many_thap_than(bazi: dict, thap_than_to_count: tuple = (), only_count_primary: bool = False, count: int = 2):
    return count_all_thap_than(bazi, thap_than_to_count, only_count_primary) > count

def print_message(message):
    frame = inspect.currentframe().f_back
    file_name = frame.f_code.co_filename
    line_number = frame.f_lineno
    print('-----------------------------------------------------------------------------------------------------')
    print(f"{message} | (Line: {line_number}, File: {file_name})")
    print('-----------------------------------------------------------------------------------------------------')
