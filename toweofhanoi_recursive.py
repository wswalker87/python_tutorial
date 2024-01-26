NUMBER_OF_DISKS = 5
#Deleted the rods dictionary, made them variable A-C, refactored.
A = list(range(NUMBER_OF_DISKS, 0, -1)) #The list function changes the range function from a range to a list,
B = []
C = []
print(A, B, C, '\n')#added print here to show the beginning
def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        # move the nth disk from source to target
    target.append(source.pop())#had to remove the dictionary refs here
        # move the n-1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)
    # display our progress
    print(A, B, C, '\n')
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
