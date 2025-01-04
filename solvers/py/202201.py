def get_totals(ll):
    totals = [0]
    for l in ll:
        if len(l):
            totals[-1] += int(l)
        else:
            totals.append(0)
    totals.sort()
    return totals

def part1(ll: list[str]) -> str:
    totals = get_totals(ll)
    return str(totals[-1])

def part2(ll: list[str]) -> str:
    totals = get_totals(ll)
    return str(sum(totals[-3:]))
