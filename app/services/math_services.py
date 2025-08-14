from app.utils.redis_cache import get_cached_result, set_cached_result

# Power operation with Redis caching
async def power(base: float, exponent: float) -> float:
    key = f"power:{base}^{exponent}"
    cached = get_cached_result(key)
    if cached is not None:
        print("⚡ Redis HIT for", key)
        return cached

    result = base ** exponent
    set_cached_result(key, result)
    return result

# Factorial with Redis caching
async def factorial(n: int) -> int:
    key = f"factorial:{n}"
    cached = get_cached_result(key)
    if cached is not None:
        print("⚡ Redis HIT for", key)
        return cached

    result = 1
    for i in range(2, n + 1):
        result *= i

    set_cached_result(key, result)
    return result

# Fibonacci helper functions
def multiply(mat1, mat2):
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w

def matrix_power(mat1, n):
    if n == 0 or n == 1:
        return
    mat2 = [[1, 1], [1, 0]]
    matrix_power(mat1, n // 2)
    multiply(mat1, mat1)
    if n % 2 != 0:
        multiply(mat1, mat2)

# Fibonacci with Redis caching
async def fibonacci(n: int):
    key = f"fibonacci:{n}"
    cached = get_cached_result(key)
    if cached is not None:
        print("⚡ Redis HIT for", key)
        return cached

    if n <= 1:
        result = n
    else:
        mat1 = [[1, 1], [1, 0]]
        matrix_power(mat1, n - 1)
        result = mat1[0][0]

    set_cached_result(key, result)
    return result
