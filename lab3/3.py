# Формула логіки висловлень задана як функція
def formula(a, b, c):
    return (a or not b) and (not a or b) and (b or c)


# Перебір усіх можливих комбінацій значень змінних A, B, C
satisfied = False
for a in [False, True]:
    for b in [False, True]:
        for c in [False, True]:
            if formula(a, b, c):
                satisfied = True
                print(f"Формула виконується з такими значеннями змінних: A={a}, B={b}, C={c}")
                break
        if satisfied:
            break
    if satisfied:
        break

if not satisfied:
    print("Формула не виконується.")

input("Натисніть Enter, щоб вийти...")
