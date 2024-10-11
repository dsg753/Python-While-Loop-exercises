GOAL_STEPS = 10000

sum_steps = 0

while sum_steps < GOAL_STEPS:
    steps = input()

    if steps == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break


    sum_steps += int(steps)

if sum_steps >= GOAL_STEPS:
    print(f'Goal reached! Good job!\n{sum_steps - GOAL_STEPS} steps over the goal!')

else:
    print(f'{GOAL_STEPS - sum_steps} more steps to reach goal.')