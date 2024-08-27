def max(seq: list[int]) -> int:
    if not seq:
        return "ValueError: max() iterable argument is empty"
    
    ans = seq[0]
    for num in seq[1:]:
        if num > ans:
            ans = num
    
    return ans

seq = [-1, -2, -3, -99, -5, -6, 0]
print(max(seq))