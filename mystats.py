# numbers = [10, 20, 30, 40, 50]


def mean(param):
   return "Mean is", sum(param) / len(param)

# print(mean())


def median(param):
    meanIdx = (len(param) + 1) // 2     # '//' <-- removes decimal
    return "Median is", param[meanIdx-1] 

# print(median())


