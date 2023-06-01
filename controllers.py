import pandas as pd
import re
from collections import Counter


def return_excel_file_data(file):
    file_data = pd.read_excel(file)
    
    return file_data

def extract_group_names(string):
    pattern = r'<I>(.*?)<\/I>'
    matches = re.findall(pattern, string)
    
    if matches:
        group_names = matches[0].split(',')
        return [group.strip() for group in group_names]
    
    return []

def get_group_count(lst):
    element_count = Counter(lst)
    count_dict = dict(element_count)
    
    return count_dict