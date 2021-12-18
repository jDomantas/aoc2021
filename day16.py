from helpers import run
from dataclasses import dataclass


class Reader:
    def __init__(self, bits):
        self.bits = bits
        self.idx = 0

    def bit(self):
        if self.idx >= len(self.bits):
            raise Exception('read out of bounds')
        self.idx += 1
        return self.bits[self.idx - 1]

    def num(self, bits):
        if bits == 0:
            return 0
        return (self.bit() << (bits - 1)) + self.num(bits - 1)

    def pos(self):
        return self.idx


@dataclass
class ValuePacket:
    version: str
    value: str


@dataclass
class OpPacket:
    version: str
    op: int
    subpackets: list


def to_bits(x):
    x = int(x, 16)
    return [x // 8, x // 4 % 2, x // 2 % 2, x % 2]


def decode(reader):
    version = reader.num(3)
    kind = reader.num(3)
    if kind == 4:
        idx = 6
        value = 0
        while True:
            cont = reader.bit()
            value = value * 16 + reader.num(4)
            if not cont:
                break
        return ValuePacket(version, value)
    else:
        length_type = reader.bit()
        subs = []
        if length_type == 0:
            end = reader.num(15)
            end += reader.pos()
            while reader.pos() < end:
                subs.append(decode(reader))
        else:
            subpackets = reader.num(11)
            for i in range(subpackets):
                subs.append(decode(reader))
        return OpPacket(version, kind, subs)


def version_sum(packet):
    if type(packet) == ValuePacket:
        return packet.version
    elif type(packet) == OpPacket:
        return packet.version + sum(version_sum(s) for s in packet.subpackets)
    else:
        raise Exception('bad packet type: ' + str(type(packet)))


def product(i):
    p = 1
    for x in i:
        p *= x
    return p


def lt(i):
    a, b = i
    return int(a < b)


def gt(i):
    a, b = i
    return int(a > b)


def eq(i):
    a, b = i
    return int(a == b)


def evaluate(packet):
    if type(packet) == ValuePacket:
        return packet.value
    elif type(packet) == OpPacket:
        if packet.op == 0:
            agg = sum
        elif packet.op == 1:
            agg = product
        elif packet.op == 2:
            agg = min
        elif packet.op == 3:
            agg = max
        elif packet.op == 5:
            agg = gt
        elif packet.op == 6:
            agg = lt
        elif packet.op == 7:
            agg = eq
        else:
            raise Exception('bad op: ' + str(packet.op))
        return agg(evaluate(p) for p in packet.subpackets)
    else:
        raise Exception('bad packet type: ' + str(type(packet)))


def solve(inp):
    bits = [b for c in inp.strip() for b in to_bits(c)]
    packet = decode(Reader(bits))
    print('part 1:', version_sum(packet))
    print('part 2:', evaluate(packet))


run(16, solve)
