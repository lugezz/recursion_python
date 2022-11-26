

# Recursive Python function to solve the tower of hanoi


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return

    tower_of_hanoi(n-1, source, auxiliary, destination)

    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)


# Driver code
n = 4
tower_of_hanoi(n, 'Stick 1', 'Stick 2', 'Stick 3')
