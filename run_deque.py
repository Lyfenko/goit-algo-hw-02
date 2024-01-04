from collections import deque


def is_palindrome(input_str):
    clean_str = ''.join(input_str.lower().split())

    char_deque = deque(clean_str)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


input_string = "козак з казок"
result = is_palindrome(input_string)

print(f"Рядок '{input_string}' є паліндромом: {result}")
