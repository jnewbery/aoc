from dataclasses import dataclass

@dataclass
class Gate:
    inputs: tuple[str, str]
    output: str
    operation: str
    resolved: int | None = None

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
    if wire.operation == "AND":
        output = input1_val & input2_val
    elif wire.operation == "OR":
        output = input1_val | input2_val
    elif wire.operation == "XOR":
        output = input1_val ^ input2_val

    wire.resolved = output
    return output

def part1(ll: list[str]) -> str:
    wires: dict[str, Gate] = {}
    for l in ll:
        if ":" in l:
            wire, value = l.split(": ")
            wires[wire.strip()] = Gate(inputs=("", ""), output=wire.strip(), operation="", resolved=int(value.strip()))
        elif "->" in l:
            parts = l.split(" ")
            operation = parts[1]
            gate = Gate(inputs=(parts[0], parts[2]), output=parts[4], operation=operation)
            wires[gate.output] = gate

    for wire_name in wires:
        resolve_wire(wire_name, wires)

    wires_list = list(wires.values())
    wires_list.sort(key=lambda x: x.output, reverse=True)
    z_values = "".join([str(wire.resolved) for wire in wires_list if wire.output[0] == "z"])
    return(str(int(z_values, 2)))

def part2(ll: list[str]) -> str:
    gates: list[Gate] = []
    for l in ll:
        if "->" in l:
            parts = l.split(" ")
            operation = parts[1]
            assert operation is not None
            gates.append(Gate(inputs=(parts[0], parts[2]), output=parts[4], operation=operation))

    bad_gates: set[str] = set()
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

