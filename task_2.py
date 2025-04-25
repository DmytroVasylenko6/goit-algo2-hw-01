from colorama import Fore, init

init(autoreset=True)


def quick_select(arr, k, depth=0):
    indent = "  " * depth

    if len(arr) == 1:
        print(f"{indent}{Fore.CYAN}Базовий випадок: єдиний елемент {arr[0]}")
        return arr[0]

    pivot = arr[len(arr) // 2]

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    print(f"{indent}{Fore.MAGENTA}Виклик quick_select(arr={arr}, k={k})")
    print(f"{indent}{Fore.YELLOW}→ Pivot: {pivot}")
    print(f"{indent}{Fore.GREEN}  lows: {lows}")
    print(f"{indent}{Fore.BLUE}  pivots: {pivots}")
    print(f"{indent}{Fore.RED}  highs: {highs}")

    if k <= len(lows):
        print(f"{indent}{Fore.CYAN}🔽 k={k} в lows — рекурсія вниз")
        return quick_select(lows, k, depth + 1)
    elif k <= len(lows) + len(pivots):
        print(
            f"{indent}{Fore.CYAN}✅ k={k} знаходиться серед pivots — повертаємо {pivot}"
        )
        return pivot
    else:
        new_k = k - len(lows) - len(pivots)
        print(f"{indent}{Fore.CYAN}🔼 k={k} в highs (нове k={new_k}) — рекурсія вниз")
        return quick_select(highs, new_k, depth + 1)


arr = [7, 10, 4, 3, 20, 15, 1, -1, 33, -3, 33]
k = 3
k2 = 5
result = quick_select(arr, k)
result2 = quick_select(arr, k2)
print(f"{k}-й найменший елемент: {result}")
print(f"{k2}-й найменший елемент: {result2}")
