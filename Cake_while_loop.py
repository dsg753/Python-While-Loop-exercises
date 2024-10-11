width = int(input())
length = int(input())


total_pieces = width * length
pieces_taken = 0

while True:
    command = input()

    if command == "STOP":

        remaining_pieces = total_pieces - pieces_taken
        print(f"{remaining_pieces} pieces are left.")
        break


    pieces = int(command)
    pieces_taken += pieces


    if pieces_taken > total_pieces:
        needed_pieces = pieces_taken - total_pieces
        print(f"No more cake left! You need {needed_pieces} pieces more.")
        break
