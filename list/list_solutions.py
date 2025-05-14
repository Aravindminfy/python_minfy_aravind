# Write a function called filter_even_numbers that takes a list of integers and returns a new list containing only the even numbers.

def filter_even_numbers(num):
    return [i for i in num if i%2==0]

# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []

#---------------------------------------------------------------------------------------------------------------------
#Write a function called merge_sorted_lists that takes two sorted lists and returns a new sorted list containing all elements from both lists.

def merge_sorted_lists(lis1,lis2):
    return sorted(lis1 + lis2)

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]


#Write a function called generate_matrix that takes dimensions n and m, and returns an n×m matrix where each element at position (i,j) is calculated as i*j.

def generate_matrix(x,y):
    full_list = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i*j) # create a row
        full_list.append(row) # append the above row in full_list
    return full_list


# Example usage:
print(generate_matrix(3, 3))
# Should return:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]

# ------------------------------------------------------------------------------------------------------------------

#Write a function called transpose_matrix that takes a matrix (list of lists) and returns its transpose (rows become columns and vice versa).

def transpose_matrix(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    transpose = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        transpose.append(new_row)
    return transpose

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Output:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
