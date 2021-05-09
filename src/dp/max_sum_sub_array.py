import itertools
def maxsum_subArray(array):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(array):
        min_sum = min(min_sum,running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

print (maxsum_subArray([904,40,523,12,-355,-342,-124,481,-31]))
