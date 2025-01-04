from typing import Generator

def head_generator(ll: list[str]) -> Generator[list[int], None, None]:
    h = [0, 0]
    for l in ll:
        direction, repeat = l.split()
        for _ in range(int(repeat)):
            match direction:
                case "U":
                    h = [h[0], h[1] + 1]
                case "R":
                    h = [h[0] + 1, h[1]]
                case "D":
                    h = [h[0], h[1] - 1]
                case "L":
                    h = [h[0] - 1, h[1]]
            yield h

def solve(ll: list[str], tail_len):
    tail = [[0, 0] for _ in range(tail_len + 1)]
    t_visited = set([tuple(tail[-1])])
    for h in head_generator(ll):
        tail[0] = h
        for i in range(1, len(tail)):
            if abs(tail[i][0] - tail[i - 1][0]) <= 1 and abs(tail[i][1] - tail[i - 1][1]) <= 1:
                # tail doesn't move
                pass
            else:
                # tail moves towards head
                for coord in [0, 1]:
                    if tail[i - 1][coord] > tail[i][coord]:
                        tail[i][coord] += 1
                    elif tail[i - 1][coord] < tail[i][coord]:
                        tail[i][coord] -= 1
        t_visited.add(tuple(tail[-1]))

    return len(t_visited)

def part1(ll: list[str]) -> str:
    return str(solve(ll, 1))

def part2(ll: list[str]) -> str:
    return str(solve(ll, 9))
