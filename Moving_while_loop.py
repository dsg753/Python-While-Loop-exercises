width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
used_volume = 0

while True:
    command = input()

    if command == "Done":

        remaining_volume = total_volume - used_volume
        print(f"{remaining_volume} Cubic meters left.")
        break


    boxes = int(command)
    used_volume += boxes


    if used_volume > total_volume:
        needed_volume = used_volume - total_volume
        print(f"No more free space! You need {needed_volume} Cubic meters more.")
        break
