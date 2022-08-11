
# visualize the solution

def printTowerOfHanoi(rods):
    height = sum(map(len, rods))
    for r in reversed(range(height)):
        for peg in rods:
            disk = "-" * (0 if r >= len(peg) else peg[r])
            print(f"{disk:>{height}}|{disk:{height}}", end=" ")
        print()
    invalid = any(p[::-1] != sorted(p) for p in rods)
    print("=" * (height * 6 + 5), "INVALID" * invalid)
    print()


def moveDisk(rods, diskNum, fromRod, toRod):
    rods[toRod].append(diskNum)
    rods[fromRod].pop()
    printTowerOfHanoi(rods)
    print()

# only for more then 3
# if its only 3 we can use:
# rods = [[3, 2, 1], [], []]
def makeRods(fromRod, numOfDisks, numOfRods):
    x = []
    for i in range(numOfRods):
        x.append([])
    rods = x
    for i in range(numOfDisks):
        rods[fromRod].append(numOfDisks - i)
    return rods

def towerOfHanoiSolution(fromRod, toRod, middleRod, numOfDisks=None, rods=None, numOfRods=3):
    if numOfDisks is None:
        inputNumOfDisks = int(input("Enter number of disks: "))
        # make the rods variable according to the order of the rods
        numOfDisks = inputNumOfDisks
        rods = makeRods(fromRod, numOfDisks, numOfRods)
        printTowerOfHanoi(rods)
    if numOfDisks == 1:
        print("Move disk 1 from rod", fromRod, "to rod", toRod)
        moveDisk(rods, 1, fromRod, toRod)
        return "Done"
    towerOfHanoiSolution(fromRod, middleRod, toRod, numOfDisks - 1, rods)
    print("Move disk", numOfDisks, "from rod", fromRod, "to rod", toRod)
    moveDisk(rods, numOfDisks, fromRod, toRod)
    towerOfHanoiSolution(middleRod, toRod, fromRod, numOfDisks - 1, rods)



towerOfHanoiSolution(fromRod=2, toRod=0, middleRod=1)