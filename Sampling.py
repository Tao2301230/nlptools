import os


def read_in_chunks(filePath, chunk_size=1024*1024):
    file_object = open(filePath, 'r', encoding='utf-8')
    while True:
        chunk_data = file_object.read(chunk_size)
        print(chunk_data[-1])
        if not chunk_data:
            break
        yield chunk_data


if __name__ == "__main__":
    file_Path = os .path.abspath('/home/bantao/pcworkspace/bt_develop/datasets/prediction_pn.csv')
    print(file_Path)
    count = 0
    '''
    for chunk in read_in_chunks(file_Path):
        pass
    '''

    sample = list()
    with open(file_Path, 'r') as f:
        for line in f:
            count += 1
            if count % 2500 == 0:
                sample.append(line.split(',')[0])

    print(len(sample))
    print(sample[50])


