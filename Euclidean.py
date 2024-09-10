def Euclidean_algorithm(a: int, b: int) -> int:
    min_num = min(a, b)
    max_num = max(a, b)
    while min_num > 0:
        max_num += max_num % min_num
        
    
    return a

print(Euclidean_algorithm(18, 24))