import heapq

def d_squared(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

def get_relays(ll: list[str]) -> list[tuple[int, int, int]]:
    relays: list[tuple[int, int, int]] = []
    for l in ll:
        dims = l.split(',')
        relay = (int(dims[0]), int(dims[1]), int(dims[2]))
        relays.append(relay)

    return relays

def get_d_squared_to_relays(relays: list[tuple[int, int, int]]) -> list[tuple[int, tuple[int, int]]]:
    # (distance squared, relays). We order them in this way
    # so we can heapify and pop of the front to get the shortest
    # vertices
    d_squared_relays: list[tuple[int, tuple[int, int]]] = []
    for i in range(len(relays)):
        for j in range(i + 1, len(relays)):
            d_squared_relays.append((d_squared(relays[i], relays[j]), (i, j)))

    heapq.heapify(d_squared_relays)
    return d_squared_relays

def part1(ll: list[str]) -> str:
    if len(ll) == 20:
        # test input
        generations = 10
    else:
        generations = 1000
    relays = get_relays(ll)

    d_squared_relays = get_d_squared_to_relays(relays)

    relay_to_circuit: dict[int, set[int]] = {}
    for i in range(generations):
        _, relay_ij = heapq.heappop(d_squared_relays)
        i, j = relay_ij
        if i not in relay_to_circuit and j not in relay_to_circuit:
            # i and j are not in circuits. Create a new circuit connecting them.
            relay_to_circuit[i] = {i, j}
            relay_to_circuit[j] = relay_to_circuit[i]
        elif i not in relay_to_circuit:
            # add i to j's circuit
            relay_to_circuit[j].add(i)
            relay_to_circuit[i] = relay_to_circuit[j]
        elif j not in relay_to_circuit:
            # add j to i's circuit
            relay_to_circuit[i].add(j)
            relay_to_circuit[j] = relay_to_circuit[i]
        else:
            # merge i and j circuits
            relay_to_circuit[j] |= relay_to_circuit[i]
            connected_relays = relay_to_circuit[i]
            for k in connected_relays:
                relay_to_circuit[k] = relay_to_circuit[j]

    circuit_id_to_len = {id(c): len(c) for c in relay_to_circuit.values()}
    lens = list(reversed(sorted(circuit_id_to_len.values())))
    return str(lens[0] * lens[1] * lens[2])

def part2(ll: list[str]) -> str:
    relays = get_relays(ll)

    d_squared_relays = get_d_squared_to_relays(relays)

    relay_to_circuit: dict[int, set[int]] = {}
    while(True):
        _, relay_ij = heapq.heappop(d_squared_relays)
        i, j = relay_ij
        if i not in relay_to_circuit and j not in relay_to_circuit:
            # i and j are not in circuits. Create a new circuit connecting them.
            relay_to_circuit[i] = {i, j}
            relay_to_circuit[j] = relay_to_circuit[i]
        elif i not in relay_to_circuit:
            # add i to j's circuit
            relay_to_circuit[j].add(i)
            relay_to_circuit[i] = relay_to_circuit[j]
        elif j not in relay_to_circuit:
            # add j to i's circuit
            relay_to_circuit[i].add(j)
            relay_to_circuit[j] = relay_to_circuit[i]
        else:
            # merge i and j circuits
            relay_to_circuit[j] |= relay_to_circuit[i]
            connected_relays = relay_to_circuit[i]
            for k in connected_relays:
                relay_to_circuit[k] = relay_to_circuit[j]
        if len(relay_to_circuit[i]) == len(relays):
            return str(relays[i][0] * relays[j][0])
