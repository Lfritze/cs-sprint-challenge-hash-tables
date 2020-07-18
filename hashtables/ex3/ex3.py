def intersection(arrays):
    count_int = {}
    for arr in arrays:
        for x in arr:
            if x not in count_int:
                count_int[x] = 0
            
            count_int[x] += 1

    result = []

    for key,value in count_int.items():
        if value == len(arrays):
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
