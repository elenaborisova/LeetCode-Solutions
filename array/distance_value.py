def find_distance_value(arr1, arr2, d):
    count = 0

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            dis = abs(arr1[i] - arr2[j])
            if dis <= d:
                break
        else:
            count += 1

    return count


print(find_distance_value(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
print(find_distance_value(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))
print(find_distance_value(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))
