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


def towerOfHanoiSolution(fromRod, toRod, middleRod, numOfDisks=None, rods=None):
    if numOfDisks is None:
        inputNumOfDisks = int(input("Enter number of disks: "))
        rods = [list(range(1, inputNumOfDisks + 1).__reversed__()), [], []]
        numOfDisks = inputNumOfDisks
    if numOfDisks == 1:
        print("Move disk 1 from rod", fromRod, "to rod", toRod)
        moveDisk(rods, 1, fromRod, toRod)
        return "Done"
    towerOfHanoiSolution(fromRod, middleRod, toRod, numOfDisks - 1, rods)
    print("Move disk", numOfDisks, "from rod", fromRod, "to rod", toRod)
    moveDisk(rods, numOfDisks, fromRod, toRod)
    towerOfHanoiSolution(middleRod, toRod, fromRod, numOfDisks - 1, rods)


# inputNumOfDisks = int(input("Enter number of disks: ")) towerOfHanoiSolution(fromRod=0, toRod=2, middleRod=1,
# numOfDisks=inputNumOfDisks, rods=[list(range(1, inputNumOfDisks + 1).__reversed__()), [], []])
towerOfHanoiSolution(fromRod=0, toRod=2, middleRod=1)