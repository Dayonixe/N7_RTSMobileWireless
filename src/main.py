import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    # read file
    tr_file = open('out.tr', 'r')
    content = tr_file.read()

    # close file
    tr_file.close()

    # split file
    lines = content.split('\n')

    data = []

    # print file
    for line in lines:
        # split string i by space
        split = line.split(' ')
        if split[0] == 'r' and split[2] == '_1_' and split[3] == 'AGT':
            data.append({
                'time': float(split[1]),
                'size': int(split[8])
            })

    values = []

    # sum size in data by values of the same round time
    print("time;volume")
    sum_size = 0
    for i in range(len(data)):
        if i == 0:
            sum_size += data[i]['size']
        else:
            if math.floor(data[i]['time']) == math.floor(data[i-1]['time']):
                sum_size += data[i]['size']
            else:
                print('{0};{1}'.format(math.floor(data[i-1]['time']), sum_size))
                values.append(sum_size)
                sum_size = data[i]['size']

    # remove first value
    # we remove the firt two values as they are not accurate
    # it must be the time for the engine to warm up
    values.pop(0)
    values.append(sum_size)

    print('{0};{1}'.format(math.floor(data[len(data)-1]['time']), sum_size))

    xpoints = np.arange(2, 200, 1)
    ypoints = values

    plt.figure(figsize=(7, 5))
    line = plt.plot(xpoints, ypoints)
    # fill below the line
    plt.fill_between(xpoints, ypoints, 98000, color='blue', alpha=0.5)

    plt.title('Data transferred (bytes) by second | RTSThreshold = 10000')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Data transferred (bytes)')
    plt.show()

if __name__ == '__main__':
    main()
