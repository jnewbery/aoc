#!/usr/bin/env python3
from utils import BaseSolution
from dataclasses import dataclass

@dataclass
class Gate:
    inputs: tuple[str, str]
    output: str
    operation: str
    resolved: int | None = None
    true_output: str | None = None

def resolve_wire(wire_name: str, wires: dict[str, Gate]) -> int:
    wire = wires[wire_name]
    if wire.resolved is not None:
        return wire.resolved
    input1, input2 = wire.inputs
    if wires[input1].resolved is not None:
        input1_val = wires[input1].resolved
        assert input1_val is not None
    else:
        input1_val = resolve_wire(input1, wires)
    if wires[input2].resolved is not None:
        input2_val = wires[input2].resolved
        assert input2_val is not None
    else:
        input2_val = resolve_wire(input2, wires)

    output = 0
    if wire.output == "AND":
        output = input1_val & input2_val
    elif wire.output == "OR":
        output = input1_val | input2_val
    elif wire.output == "XOR":
        output = input1_val ^ input2_val

    wire.resolved = output
    return output

def get_n_bits(n: int, wires: list[Gate], prefix: str = "") -> str:
    values = "".join([str(w.resolved) for w in wires if w.output.startswith(prefix) and int(w.output[1:]) <= n])
    return values

def get_x_plus_y_n_bits(wires: dict[str, Gate], n: int) -> int:
    xy_wires = [w for w in wires.values() if w.output.startswith('x') or w.output.startswith('y')]
    xy_wires.sort(key=lambda w: w.output, reverse=True)
    x = get_n_bits(n, xy_wires, 'x')
    # print(f"x = {x}")
    y = get_n_bits(n, xy_wires, 'y')
    # print(f"y = {y}")
    # print(f"x + y = {int(x, 2) + int(y, 2)}")
    return int(x, 2) + int(y, 2) & (2**(n+1)-1)

def solve_to_n(wires: dict[str, Gate], n: int) -> str:
    for wire_name in [w for w in wires if (w.startswith("z")) and int(w[1:]) <= n]:
        resolve_wire(wire_name, wires)

    resolved_wires = [w for w in wires.values() if w.resolved is not None]
    resolved_wires.sort(key=lambda w: w.output, reverse=True)

    return get_n_bits(n, resolved_wires, 'z')

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        del ll
        raise NotImplementedError()

    def part2(self, ll) -> str:
        gates: list[Gate] = []
        for l in ll:
            if "->" in l:
                parts = l.split(" ")
                operation = parts[1]
                assert operation is not None
                gates.append(Gate(inputs=(parts[0], parts[2]), output=parts[4], operation=operation))

        # good_wires: dict[str, Gate] = {k: v for k, v in wires.items() if k.startswith("x") or k.startswith("y")}
        # good_wires['z00'] = Gate(inputs=('x00', 'y00'), output='z00', operation=(lambda a, b: a ^ b)) # z bit
        # good_wires['c00'] = Gate(inputs=('x00', 'y00'), output='c00', operation=(lambda a, b: a & b)) # carry
        # for i in range(1, 45):
        #     good_wires[f'o{i:02}'] = Gate(inputs=(f'x{i:02}', f'y{i:02}'), output=f'o{i:02}', operation=(lambda a, b: a ^ b))  # or
        #     good_wires[f'z{i:02}'] = Gate(inputs=(f'o{i:02}', f'c{i-1:02}'), output=f'z{i:02}', operation=(lambda a, b: a ^ b))  # z bit
        #     good_wires[f'a{i:02}'] = Gate(inputs=(f'x{i:02}', f'y{i:02}'), output=f'a{i:02}', operation=(lambda a, b: a & b))  # and
        #     good_wires[f'pc{i:02}'] = Gate(inputs=(f'o{i:02}', f'c{i-1:02}'), output=f'pc{i:02}', operation=(lambda a, b: a & b))  # partial carry
        #     if i < 44:
        #         good_wires[f'c{i:02}'] = Gate(inputs=(f'a{i:02}', f'pc{i:02}'), output=f'c{i:02}', operation=(lambda a, b: a | b))  # carry
        #     else:
        #         good_wires['z45'] = Gate(inputs=(f'a{i:02}', f'pc{i:02}'), output='z45', operation=(lambda a, b: a | b))  # carry
        bad_gates: set[str] = set()
        print(len(gates))
        for gate in gates:
            if gate.output[0] == 'z' and not (gate.output == 'z45' or gate.operation == 'XOR'):
                bad_gates.add(gate.output)
            elif gate.operation == 'XOR' and not (gate.inputs[0][0] == 'x' or gate.inputs[1][0] == 'x' or gate.output[0] == 'z'):
                bad_gates.add(gate.output)
            if gate.operation == "AND" and "x00" not in (gate.inputs[0], gate.inputs[1]):
                for subgate in gates:
                    if (gate.output in subgate.inputs) and subgate.operation != "OR":
                        bad_gates.add(gate.output)
            if gate.operation == "XOR":
                for subgate in gates:
                    if (gate.output in subgate.inputs) and subgate.operation == "OR":
                        bad_gates.add(gate.output)

        return ",".join(sorted(bad_gates))


if __name__ == "__main__":
    Solution()
