account_balance_sum = 0.0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    current_sum = float(command)

    if current_sum >= 0:
        print(f'Increase: {current_sum:.2f}')
        account_balance_sum += current_sum
    else:
        print('Invalid operation!')
        break

print(f'Total: {account_balance_sum:.2f}')
