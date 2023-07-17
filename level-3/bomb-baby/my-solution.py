def solution(x, y):
    # initial number of Mach and Facula bombs
    M = long(x)
    F = long(y)
    
    # Initialize the total number of generations
    total_generations = 0
    
    # loop until both M and F are equal to 1
    while not (M == 1 and F == 1):
        # If either M or F becomes negative, impossible to generate the required num of bombs
        if F <= 0 or M <= 0:
            return "impossible"
        
        # If F == 1, we can generate the required number of bombs in M-1 generations
        if F == 1:
            return str(total_generations + M - 1)
        else:
            # Calculate the number of times M can retrieve a sync unit from F
            # rep number of Facula bombs created in this generation
            generations = long(M/F)
            
            # Update the total num of generations required
            total_generations += generations
            
            # represents the remaining Mach bombs in the next generation
            M %= F
            
            # Swap the values of M and F, as Mach bombs retrieve sync units from Facula bombs in the next generation
            M, F = F, M
    
    # Return the total number of generations
    return str(total_generations)