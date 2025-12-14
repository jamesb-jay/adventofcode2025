''' Day 1 : this is terrible'''

class Dial:
    position = 50

    def turn(self, amount: int):
        self.position += amount
        self.position = self.position - (100*(self.position//100))

        if self.position < 0: return self.position + 100
        elif self.position > 99: return self.position - 100


def parseday1(lines: list[str]):
    for l in lines:
        value: int = int(l[1:])
        yield value if l.startswith("R") else -value

def day1(rotations):
    dial = Dial()
    zeros = 0
    for r in rotations:
        dial.turn(r)
        if dial.position == 0:
            zeros += 1
    return zeros

def day1part2(rotations):
    dial = Dial()
    zeros = 0
    for r in rotations:
        for _ in range(abs(r)):
            dial.turn(1 if r > 0 else -1)
            if dial.position == 0:
                zeros += 1
    return zeros

if __name__ == "__main__":
    with open("day1.txt") as f:
        rotations = parseday1(f.readlines())
    
    print(f"Day 1 part 1 result: {day1(rotations)}")
    print(f"Day 1 part 2 result: {day1part2(rotations)}")
