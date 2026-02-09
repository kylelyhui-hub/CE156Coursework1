def fun1(s):
    # Convert to lowercase to handle case-insensitivity
    # Spaces are preserved, so "red er" != "re der"
    s_lower = s.lower()
    # Slicing [::-1] creates a reversed version of the string
    return s_lower == s_lower[::-1]

# --- TEST CASES (Remove before submission) ---

# Testing fun1: Palindromes
print("Testing fun1:")
print(f"  'Dad' -> {fun1('Dad')}")          # Expected: True
print(f"  'red er' -> {fun1('red er')}")    # Expected: False
print(f"  'Racecar' -> {fun1('Racecar')}")  # Expected: True
print(f"  'hello' -> {fun1('hello')}")      # Expected: False


def fun2(s):
    # Convert to lowercase and filter out everything except letters
    letters = [char for char in s.lower() if char.isalpha()]

    # Return None if no letters exist in the string
    if not letters:
        return None

    # Use a dictionary to count occurrences of each letter
    counts = {}
    for char in letters:
        counts[char] = counts.get(char, 0) + 1

    # Find the letter with the highest count
    return max(counts, key=counts.get)

# Testing fun2: Most Frequent Letter
print("\nTesting fun2:")
print(f"  'Banana' -> {fun2('Banana')}")          # Expected: 'a' (or 'n')
print(f"  '123!!' -> {fun2('123!!')}")            # Expected: None
print(f"  'Apples and Oranges' -> {fun2('Apples and Oranges')}") # Expected: 'a' (or 'e', 's', 'n')

def fun3(s):
    letters = 0
    digits = 0
    spaces = 0

    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    return (letters, digits, spaces)

# Testing fun3: Counts (Letters, Digits, Spaces)
print("\nTesting fun3:")
print(f"  '100 Days of Code' -> {fun3('100 Days of Code')}")
# Letters: 10, Digits: 3, Spaces: 3 -> Expected: (10, 3, 3)

print(f"  'Python 3.10' -> {fun3('Python 3.10')}")
# Letters: 6, Digits: 3, Spaces: 1 ('.' is ignored) -> Expected: (6, 3, 1)
