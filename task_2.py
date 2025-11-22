from collections import deque

def is_palindrome(text):
    # Підготовка рядка: лише букви/цифри, без пробілів, у нижньому регістрі
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    # Додаємо символи до deque
    d = deque(cleaned)

    # Порівнюємо символи з обох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


# ----------------- Тестування -----------------

tests = [
    "A man a plan a canal Panama",
    "racecar",
    "Hello",
    "Was it a car or a cat I saw",
    "123321",
    "not a palindrome"
]

for t in tests:
    print(f"{t!r}: {is_palindrome(t)}")
