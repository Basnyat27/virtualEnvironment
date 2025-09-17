# data = [10, 20, None, 20, 30, None, 40]

def fill_missing_with_mean(param):
    numbers = []    #for calc mean after removing 'None'
    for i in param:
        if i != None:
            numbers.append(i)

    meanValue = sum(numbers) // len(numbers)    # '//' <-- removes decimal
    # print(meanValue)

    replace = []    #for replacing 'None' value with mean
    for j in param:
        if j == None:
            j = meanValue
        replace.append(j)

    print(replace)

# fill_missing_with_mean(data)
    
### Need to know use of decorator for easy solving! 