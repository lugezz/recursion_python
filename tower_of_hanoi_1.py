

"""
Tower of Hanoi is a mathematical game, which has three rules. Before we set the rules,
let's see how our universe looks like.

Rules:

1. You can only move one disk at the time.
2. You can only take the top disk and place on top of another tower (rod).
3. You cannot place a bigger disk on top of a smaller disk.

Solution:

Move subproblem of n - 1 disks from start_tower to aux_tower.
Move disk n to dest_tower.
Move subproblem of n - 1 disk from aux_tower to dest_tower.
"""


class Towers:
    def __init__(self, disks=3):
        self.disks = disks
        self.towers = [[]]*3
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def __str__(self):
        output = ""
        for i in range(self.disks, -1, -1):
            for j in range(3):
                if len(self.towers[j]) > i:
                    output += " " + str(self.towers[j][i])
                else:
                    output += "  "
            output += "\n"
        return output + "-" * 8

    def move(self, from_tower, dest_tower):
        disk = self.towers[from_tower].pop()
        self.towers[dest_tower].append(disk)


def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    # Base case - do nothing
    if n == 0:
        return

    # Move subproblem of n - 1 disks from start_tower to aux_tower.
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)

    # Move disk n to dest_tower.
    towers.move(start_tower, dest_tower)
    print(towers)

    # Move subproblem of n - 1 disk from aux_tower to dest_tower.
    solve_tower_of_hanoi(towers, n - 1, aux_tower, dest_tower, start_tower)


t = Towers()
print(t)
solve_tower_of_hanoi(t, t.disks, 0, 2, 1)

# Tower of 5 disks
print('-' * 100)
print('-' * 100)
t2 = Towers(5)
solve_tower_of_hanoi(t2, t2.disks, 0, 2, 1)

# Tower of 10 disks
print('-' * 100)
print('-' * 100)
t3 = Towers(10)
solve_tower_of_hanoi(t3, t3.disks, 0, 2, 1)
