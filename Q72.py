# Write a recursive solution to the Tower of Hanoi puzzle for n disks
n = 3
source = 'A'
auxiliary = 'B'
target = 'C'

def move_disks(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    move_disks(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    move_disks(n - 1, auxiliary, source, target)

move_disks(n, source, auxiliary, target)