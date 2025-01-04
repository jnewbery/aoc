import hashlib
def register_generator(ll):
    reg = 1
    yield reg
    for l in ll:
        match l.split():
            case ['noop']:
                yield reg
            case 'addx', size:
                yield reg
                reg += int(size)
                yield reg

def part1(ll: list[str]) -> str:
    # print([(i,n) for i,n in enumerate(register_generator(ll))])
    # print([((i+1), n) for i,n in enumerate(register_generator(ll)) if i in range(19, 220, 40)])
    return str(sum(((i+1) * n for i, n in enumerate(register_generator(ll)) if i in range(19, 220, 40))))

def part2(ll: list[str]) -> str:
    screen = ''
    for (t, x) in enumerate(register_generator(ll)):
        # print(x)
        if not t % 40 and t > 0:
            screen += '\n'
        if abs((t % 40) - x) <= 1:
            screen += '#'
        else:
            screen += '.'

    # The solution is a string rendering of an image, so return
    # the hash to check correctness.
    return hashlib.sha256(screen.encode("utf-8")).hexdigest()[0:8]
