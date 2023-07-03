def solution(data, n): 
    # Your code here
    new_data = set(data)
    for num in new_data:
        if data.count(num) > n:
            result = []
            for curr in data:
                if curr != num:
                    result.append(curr)
            data = result
    return data