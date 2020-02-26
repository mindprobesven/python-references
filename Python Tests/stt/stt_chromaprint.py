#!/usr/bin/env python3

import numpy 

# seconds to sample audio file for
# sample_time = 500
# number of points to scan cross correlation over
span = 2
# step size (in points) of cross correlation
step = 1
# minimum number of points that must overlap in cross correlation
# exception is raised if this cannot be met
min_overlap = 5
# report match when cross correlation has a peak exceeding threshold
threshold = 0.5

def correlation(list_x, list_y):
    if len(list_x) > len(list_y):
        list_x = list_x[:len(list_y)]
    elif len(list_x) < len(list_y):
        list_y = list_y[:len(list_x)]

    covariance = 0
    for i in range(len(list_x)):
        covariance += 32 - bin(list_x[i] ^ list_y[i]).count("1")
    covariance = covariance / float(len(list_x))

    return covariance/32

# return cross correlation, with listy offset from listx
def cross_correlation(listx, listy, offset):
    if offset > 0:
        listx = listx[offset:]
        listy = listy[:len(listx)]
    elif offset < 0:
        offset = -offset
        listy = listy[offset:]
        listx = listx[:len(listy)]
    if min(len(listx), len(listy)) < min_overlap:
        # Error checking in main program should prevent us from ever being
        # able to get here.
        # return
        raise Exception('Overlap too small: %i' % min(len(listx), len(listy)))
    return correlation(listx, listy)

def compare(listx, listy, span, step):
    if span > min(len(listx), len(listy)):
        # Error checking in main program should prevent us from ever being
        # able to get here.
        raise Exception('span >= sample size: %i >= %i\n'
                        % (span, min(len(listx), len(listy)))
                        + 'Reduce span, reduce crop or increase sample_time.')
    corr_xy = []
    for offset in numpy.arange(-span, span + 1, step):
        corr_xy.append(cross_correlation(listx, listy, offset))
    return corr_xy

# return index of maximum value in list
def max_index(listx):
    max_index = 0
    max_value = listx[0]
    for i, value in enumerate(listx):
        if value > max_value:
            max_value = value
            max_index = i
    return max_index

def get_max_corr(corr, source, target):
    max_corr_index = max_index(corr)
    max_corr_offset = -span + max_corr_index * step
    print("max_corr_index = ", max_corr_index, "max_corr_offset = ", max_corr_offset)
# report matches
    if corr[max_corr_index] > threshold:
        print('%s and %s match with correlation of %.4f at offset %i'
        % (source, target, corr[max_corr_index], max_corr_offset))

if __name__ == "__main__":
    # fingerprint1 = list(map(int, "442874111,442874111,157662718,174439934,174438910,442874110,443399422,439202046,438661374,438644862,439824766,454177327,406987308,411050540,411051548,142622220,142613324,142612812,142744908,142744908,142755149".split(',')))
    fingerprint2 = list(map(int, "157662718,157662718,174439934,174438910,442874111,443399422,439202046,438661374,438644862,439824766,454177327,406987308,411050540,411051548,142622220,142613324,142612812,142744908,142744908,142755149".split(',')))
    # fingerprint2 = list(map(int, "1227366444,1210589228,1211637772,137965324,137969164,148584972,144326220,146419276,146437964,167397197,158187903,224776575,224784767,224784767,224784767,224784767,224784767,224784767,224784767".split(',')))
    # Guten Tag
    fingerprint3 = list(map(int, "422424818,455979250,439267538,439267538,439005395,438964464,439038048,455751008,418070048,414723620,1488465444,1488465436,146290188,146540108,229377613,233046623,224784767,224784767,224784767".split(',')))
    #3print(fingerprint1)
    # result = correlation(fingerprint1, fingerprint2)
    # print(result)

    corr = compare(fingerprint2, fingerprint3, span, step)
    print(corr)
    get_max_corr(corr, 'fingerprint1', 'fingerprint3')
