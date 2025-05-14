#Write a function called `swap_pairs` that swaps adjacent elements in a tuple. If the tuple has an odd length, the last element should remain in place.


def swap_pairs(t):
    l = list(t) 
    for i in range(0, len(l) - 1, 2):
        l[i], l[i+1] = l[i+1], l[i]
    return tuple(l)


# Example usage:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))  # Should return (2, 1, 3)

#------------------------------------------------------------------------------------------------------------
    
#Write a function called `get_stats` that takes a list of numbers and returns a tuple containing the minimum, maximum, sum, and average of the numbers.

def get_stats(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    tot_val = sum(numbers)
    avg_val = tot_val / len(numbers) 
    return (min_val, max_val, tot_val, avg_val)

# Example usage:
print(get_stats([1, 2, 3, 4, 5]))  # Output: (1, 5, 15, 3.0)

# -------------------------------------------------------------------------------------------------------------
#Create a function called count_coordinate_occurrences that takes a list of (x, y) coordinate tuples and returns a dictionary mapping each coordinate to the number of times it appears in the list.

def count_coordinate_occurrences(coords):
    occur = {}
    for i in coords:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    return occur

# Example usage:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
# Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}

#------------------------------------------------------------------------------------------------------------------


#Create a named tuple called Student with fields for name, age, and grades (which should be a tuple of numbers). Then write a function called top_student that takes a list of Student tuples and returns the Student with the highest average grade.



# Example usage:
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))


alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple

