import os
import chardet


def scan_txt_file(directory):
    """
    :param directory:   user-provided directory
                        (absolute system directory)
    :return:            list of all files ended with '.txt'
                        (ignore layers)
    """
    txt_list = list()
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            if name.__contains__('.txt'):
                txt_list.append(os.path.join(root, name))
    return txt_list


def check_encoding(path):
    """
    :param path:    absolute file path
    :return:        Return file encoding string
    """
    with open(path, 'rb') as f:
        data = f.read()
        f_char_info = chardet.detect(data)
    if f_char_info['encoding'] is "GB2312":
        f_char_info['encoding'] = "GBK"
    return f_char_info['encoding']


def create_utf8_txt(path):
    """
    Replace the file in any encoding to utf-8

    :param: path:   absolute filepath
    :return:        None
    """
    ecd = check_encoding(path)
    result = list()
    with open(path, 'r', encoding=ecd) as f:
        result = f.readlines()

    with open(path[:-4], 'w+', encoding='utf-8') as f:
         f.write(''.join(result))
    os.remove(path)
    os.rename(path[:-4], path)


top_path = os.path.abspath('..')
txt_dir = ''.join(top_path + '/' + 'ContentAudition/ChatCommentsTestCase/宝强离婚目前暂时乱码.txt')

print(check_encoding(txt_dir))
create_utf8_txt(txt_dir)
'''

for i_path in scan_txt_file(txt_dir):
    create_utf8_txt(i_path)
'''
