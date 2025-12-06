DIAL_SIZE = 100

def part1(ll: list[str]) -> str:
    pos = 50
    count = 0
    for l in ll:
        direction, steps = l[0], int(l[1:])
        if direction == 'R':
            pos = (pos + steps) % DIAL_SIZE
        else:
            pos = (pos - steps) % DIAL_SIZE
        if pos == 0:
            count += 1
    return str(count)

def part2(ll: list[str]) -> str:
    pos = 50
    count = 0
    for l in ll:
        direction, steps = l[0], int(l[1:])
        if direction == 'R':
            # rots is how many rotations we made past 0
            rots, pos = divmod(pos + steps, DIAL_SIZE)
            count += rots
        else:
            if pos == 0:
                # If we stopped on 0 last time, we need to make sure we don't
                # double count when we go backwards
                count -= 1
            rots, pos = divmod(pos - steps, DIAL_SIZE)
            count += abs(rots)
            if pos == 0:
                # If we land on 0, we need to count that as passing it (even
                # though rots hasn't reduced)
                count += 1
    return str(count)
