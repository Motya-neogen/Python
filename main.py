"""Програма для обчислення факторіала та перевірки паліндрома."""


def calculate_factorial(number: int) -> int:
    """Повертає факторіал невід’ємного цілого числа."""
    if number < 0:
        raise ValueError("Факторіал визначений лише для невід’ємних чисел.")

    # Починає з 1: це також правильне значення для 0! і 1!.
    result = 1

    # Послідовно множимо число на кожне ціле від 2 до number.
    for multiplier in range(2, number + 1):
        result *= multiplier

    return result


def is_palindrome(text: str) -> bool:
    """Перевіряє, чи читається текст однаково зліва направо і справа наліво.

    Регістр, пробіли та розділові знаки не враховуються.
    """
    # Залишаємо лише літери й цифри та приводимо їх до нижнього регістру.
    normalized_text = "".join(
        character.casefold()
        for character in text
        if character.isalnum()
    )

    # Текст є паліндромом, якщо він збігається зі своєю перевернутою версією.
    return normalized_text == normalized_text[::-1]


def main() -> None:
    """Запитує в користувача, яку операцію виконати."""
    print("Оберіть операцію:")
    print("1 — обчислити факторіал")
    print("2 — перевірити паліндром")

    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        try:
            number = int(input("Введіть невід’ємне ціле число: "))
            print(f"{number}! = {calculate_factorial(number)}")
        except ValueError as error:
            print(f"Помилка: {error}")

    elif choice == "2":
        text = input("Введіть текст: ")
        if is_palindrome(text):
            print("Це паліндром.")
        else:
            print("Це не паліндром.")

    else:
        print("Невірний вибір. Введіть 1 або 2.")


if __name__ == "__main__":
    main()
