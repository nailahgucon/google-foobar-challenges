from itertools import combinations

def solution(l):
    # sort l in desc order
    l.sort(reverse = True)
    # Iterate over different lengths of combinations in descending order
    for lengths in range(len(l), 0, -1):
        # Generate combinations of the elements in the list
        # the largest combination is checked first
        for combo in combinations(l,lengths):
            # empty list to store the elements as strings
            num_list = []
            # Iterate over each element in the combination c
            for lengths in combo:
                num_list.append(str(lengths))
            # Join the elements of num_list into a single string
            largest_number = ''.join(num_list)
            # check if the resulting number is divisible by 3
            if int(largest_number) % 3 == 0:
                return largest_number
    return 0