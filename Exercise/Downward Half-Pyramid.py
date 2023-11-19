def downward_half_pyramid(index):
    for i in range(index, 0, -1):
        for x in range(0, i):
            print("*", end="")
        print("")

num_row = int(input("Enter a number: "))
downward_half_pyramid(num_row)