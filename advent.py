


''' Day 1 '''

class Dial:
    position = 50

    def get_effective_turn(amount: int) -> int:
        # Correct for 0 > amount > 100
        delta = abs(amount)
        effective = delta - (delta % 100)
        amount += effective if amount < 0 else -effective
        return amount
    
    def correct_position(p):
        if p < 0: return p + 100
        elif p > 99: return p - 100
        return p

    def turn(self, amount: int):
        newpos = self.position

        newpos += Dial.get_effective_turn(amount)
        newpos = Dial.get_effective_turn(newpos)
        newpos = Dial.correct_position(newpos)

        # print(f"At {self.position}, turning {amount} ({Dial.get_effective_turn(amount)}) to {newpos}")

        self.position = newpos

def day1():
    with open("day1.txt") as f:
        rotations = parsePuzzleinput(f.readlines())
    
    dial = Dial()

    zeros = 0
    for r in rotations:
        dial.turn(r)
        if dial.position == 0:
            zeros += 1

    return zeros

def day1part2():
    with open("day1.txt") as f:
        rotations = parsePuzzleinput(f.readlines())
    
    dial = Dial()

    zeros = 0
    for r in rotations:

        for _ in range(abs(r)):
            c = 1 if r > 0 else -1

            dial.turn(c)

            if dial.position == 0:
                zeros += 1

    return zeros
    


''' Go from e.g "R50 L40" to "50, -40'''
def parsePuzzleinput(lines: list[str]) -> list[int]:
    for l in lines:
        value: int = int(l[1:])
        yield value if l.startswith("R") else -value


if __name__ == "__main__":
    print(f"Day 1 part 1 result: {day1()}")
    print(f"Day 1 part 2 result: {day1part2()}")
