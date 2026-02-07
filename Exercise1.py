def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def non_primes_between(a, b):
    low = min(a, b)
    high = max(a, b)
    result = []
    for num in range(low, high + 1):
        if not is_prime(num):
            result.append(num)
    return result


# Main program
try:
    x = int(input("Enter the first positive integer: "))
    y = int(input("Enter the second positive integer: "))

    if x < 0 or y < 0:
        print("Error: both numbers must be positive.")
    else:
        nums = non_primes_between(x, y)

        # Print 10 numbers per line
        for i in range(0, len(nums), 10):
            line = nums[i:i+10]
            print(" ".join(str(n) for n in line))

except ValueError:
    print("Error: you must enter valid integers.")
