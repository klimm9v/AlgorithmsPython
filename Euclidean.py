def Euclidean_algorithm(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    
    return a + b

print(Euclidean_algorithm(2, 3))