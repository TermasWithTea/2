def solve_ancient_cipher(n):
    result = ""
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

# Тестирование алгоритма
print(solve_ancient_cipher(3))
print(solve_ancient_cipher(4))  
print(solve_ancient_cipher(5))
print(solve_ancient_cipher(6))
print(solve_ancient_cipher(7))
print(solve_ancient_cipher(8))
print(solve_ancient_cipher(9))
print(solve_ancient_cipher(10))
print(solve_ancient_cipher(11))
print(solve_ancient_cipher(12))
print(solve_ancient_cipher(13))
print(solve_ancient_cipher(14))
print(solve_ancient_cipher(15))
print(solve_ancient_cipher(16))
print(solve_ancient_cipher(17))
print(solve_ancient_cipher(18))
print(solve_ancient_cipher(19))
print(solve_ancient_cipher(20))