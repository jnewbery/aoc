def part1(ll: list[str]) -> str:
    fresh_ranges: list[tuple[int, int]] = []
    while (l := ll.pop(0)) != "":
        start, end = [int(n) for n in l.split('-')]
        fresh_ranges.append((start, end))
    fresh_ranges.sort()

    ingredients = [int(l) for l in ll]
    ingredients.sort()

    fresh: set[int] = set()
    for ing in ingredients:
        for fr in fresh_ranges:
            if fr[0] > ing:
                break
            elif fr[1] < ing:
                continue
            else:
                fresh.add(ing)

    return str(len(fresh))

def part2(ll: list[str]) -> str:
    fresh_ranges: list[tuple[int, int]] = []
    while (l := ll.pop(0)) != "":
        start, end = [int(n) for n in l.split('-')]
        fresh_ranges.append((start, end))
    fresh_ranges.sort()

    # Merge overlapping ranges
    i = 0
    while i < len(fresh_ranges) - 1:
        if fresh_ranges[i][1] >= fresh_ranges[i + 1][0] - 1:
            # merge ranges
            fresh_ranges[i] = (fresh_ranges[i][0], max(fresh_ranges[i][1], fresh_ranges[i + 1][1]))
            fresh_ranges.pop(i + 1)
        else:
            i += 1

    return str(sum([fr[1] - fr[0] + 1 for fr in fresh_ranges]))
