def part1(ll: list[str]) -> str:
    ll = [int(l) for l in ll]
    pairs = [ll[i:i+2] for i in range(len(ll) - 1)]
    # print(pairs)
    return str(len([p for p in pairs if p[1] > p[0]]))

def part2(ll: list[str]) -> str:
    ll = [int(l) for l in ll]
    pairs = [[sum(ll[i:i+3]), sum(ll[i+1:i+4])] for i in range(len(ll) - 3)]
    # print(pairs)
    return str(len([p for p in pairs if p[1] > p[0]]))
