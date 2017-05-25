def flip_to_win(N):

    last_was_zero = False
    current_streak = 0

    all_streaks = []
    current_group = []
    while N:
        if N % 2 == 1:
            current_streak += 1
            last_was_zero = False

        elif last_was_zero and current_group:
            all_streaks.append(current_group)
            current_group = []

        else:
            last_was_zero = True
            current_group.append(current_streak)
            current_streak = 0

        N //= 2

    if current_streak:
        current_group.append(current_streak)
    if current_group:
        all_streaks.append(current_group)

    current_max = 0
    for group in all_streaks:
        if len(group) == 1:
            if current_max < group[0]:
                current_max = group[0]
        else:
            for i in range(len(group) - 1):
                candidate = group[i] + group[i + 1] + 1
                if current_max < candidate:
                    current_max = candidate

    return current_max

print(flip_to_win(0))


