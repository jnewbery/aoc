def part1(ll: list[str]) -> str:
    pos = 50
    ret = 0
    for l in ll:
        if l[0] == 'R':
            pos = (pos + int(l[1:])) % 100
        else:
            pos = (pos - int(l[1:])) % 100
        if pos == 0:
            ret += 1
    return str(ret)

def part2(ll: list[str]) -> str:
    pos = 50
    ret = 0
    for l in ll:
        if l[0] == 'R':
            rots, pos = divmod(pos + int(l[1:]), 100)
            ret += rots
            # print(int(l[1:]), pos, rots)
            # print(f"{ret=}")
        else:
            if pos == 0:
                ret -= 1
            rots, pos = divmod(pos - int(l[1:]), 100)
            ret += abs(rots)
            # print(int(l[1:]), pos, rots)
            # print(f"{ret=}")
            if pos == 0:
                ret += 1
    return str(ret)
