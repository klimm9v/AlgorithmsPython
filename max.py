def max(seq: list[int]) -> int:
    ans = seq[0]
    for num in seq[1:]:
        if num > ans:
            ans = num
    
    return ans

seq = [1, 2, 3, 99, 5, 6, 3]
print(max(seq))