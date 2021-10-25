def can_form_array(arr, pieces):
    for piece in pieces:
        first_num = piece[0]
        n = len(piece)

        if first_num not in arr:
            return False

        if n == 1:
            continue

        num_idx = arr.index(first_num)
        if not arr[num_idx:num_idx + n] == piece:
            return False

    return True


print(can_form_array(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]))
print(can_form_array(arr=[49, 18, 16], pieces=[[16, 18, 49]]))
print(can_form_array(arr=[85], pieces=[[85]]))
print(can_form_array(arr=[15, 88], pieces=[[88], [15]]))
print(can_form_array(arr=[1, 3, 5, 7], pieces=[[2, 4, 6, 8]]))
