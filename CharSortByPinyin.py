"""
    char_sort_by_pinyin

    Input:      char_list
    Output:     char_list ordered by pinyin
"""
from pypinyin import lazy_pinyin, NORMAL


def char_sort_by_pinyin(char_list):
    pinyin_list = [''.join(lazy_pinyin(_, strict=False, style=NORMAL)) for _ in char_list]
    zip_list = list(zip(pinyin_list, char_list))
    return [ch for py, ch in sorted(zip_list, key=lambda _: _[0])]


'''
    *******************************************************
    Test    
    *******************************************************
'''

a = ['中共的罪恶\n', '邓矮子\n', '胡jt\n', '亲共媒体\n']
print(char_sort_by_pinyin(a))
