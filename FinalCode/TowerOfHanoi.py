# visualize the Tower of Hanoi




def printHanoi(pegs):
    height = sum(map(len,pegs))
    for r in reversed(range(height)):
        for peg in pegs:
            disc = "-" * (0 if r>=len(peg) else peg[r])
            print(f"{disc:>{height}}|{disc:{height}}", end=" ")
        print()
    invalid = any(p[::-1]!=sorted(p) for p in pegs)
    print("="*(height*6+5),"INVALID"*invalid)
    print()



def move(discNum, fromRod, toRod):
    pegs[toRod].append(discNum)
    pegs[fromRod].pop()
    printHanoi(pegs)
    print()





def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        move(1, from_rod, to_rod)
        return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    move(n, from_rod, to_rod)
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)


towerOfHanoi(3, from_rod=0, to_rod=2, aux_rod=1)