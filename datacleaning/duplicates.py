# data = [10, 20, None, 20, 30, None, 40]

def remove_duplicates(param):
    duplicate = set()
    # print(type(duplicate))

    for i in param:
        if i == None:
            continue
        else:
            duplicate.add(i)

    print(duplicate)

# remove_duplicates()