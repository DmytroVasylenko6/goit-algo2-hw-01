from colorama import Fore, init

init(autoreset=True)


def colored(text, color_code):
    return f"\033[{color_code}{text}\033[0m"


def find_min_max(arr, depth=0, branch="ROOT"):
    indent = "│  " * depth + ("├─ " if depth > 0 else "")
    print(f"{colored(f"{indent}{branch} (Обробка підмасиву):", Fore.CYAN)} {arr}")

    if len(arr) == 1:
        print(
            f"{indent}➡ Один елемент: {colored(f"min={arr[0]}", Fore.GREEN)}, {colored(f"max={arr[0]}", Fore.GREEN)}"
        )
        return arr[0], arr[0]

    elif len(arr) == 2:
        min_val = min(arr[0], arr[1])
        max_val = max(arr[0], arr[1])
        print(
            f"{indent}➡ Два елементи: {colored(f"min={min_val}", Fore.GREEN)}, {colored(f"max={max_val}", Fore.GREEN)}"
        )
        return min_val, max_val

    else:
        mid = len(arr) // 2
        print(f"{indent}✂ Розділяємо на {arr[:mid]} і {arr[mid:]}")

        left_min, left_max = find_min_max(arr[:mid], depth + 1, "LEFT")
        right_min, right_max = find_min_max(arr[mid:], depth + 1, "RIGHT")

        overall_min = min(left_min, right_min)
        overall_max = max(left_max, right_max)

        print(
            f"{indent}⬅ З обох частин {arr[:mid]} і {arr[mid:]}: {colored(f"min={overall_min}", Fore.GREEN)}, {colored(f"max={overall_max}", Fore.GREEN)}"
        )
        return overall_min, overall_max


array = [3, 5, -3, 1, 8, -2, 7, 4, 10]
min_val, max_val = find_min_max(array)
print(f"\n✅ Результат: Мінімум = {min_val}, Максимум = {max_val}")
