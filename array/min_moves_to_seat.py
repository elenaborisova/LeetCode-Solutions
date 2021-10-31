def min_moves_to_seat(seats, students):
    seats.sort()
    students.sort()
    moves_count = 0

    for i in range(len(seats)):
        moves_count += abs(seats[i] - students[i])

    return moves_count


print(min_moves_to_seat(seats=[3, 1, 5], students=[2, 7, 4]))
print(min_moves_to_seat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(min_moves_to_seat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
