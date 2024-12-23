#!/usr/bin/env python3
from utils import BaseSolution

import re
import itertools

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_sensor_beacon_radius(ll):
    for l in ll:
        sb = [int(i) for i in re.findall(r'-?\d+', l)]
        r = distance((sb[0], sb[1]), (sb[2], sb[3]))
        yield ((sb[0], sb[1]), (sb[2], sb[3]), r)

def row_cover(row, sensor, beacon, radius):
    if abs(sensor[1] - row) > radius:
        return []
    elif sensor[0] == beacon[0] and beacon[1] == row:
        return []
    low_x = sensor[0] - (radius - abs(sensor[1] - row))
    high_x = sensor[0] + (radius - abs(sensor[1] - row))
    if low_x == beacon[0]:
        low_x += 1
    if high_x == beacon[0]:
        high_x -= 1
    return [low_x, high_x]

def merge_covers(covers):
    if len(covers) == 1:
        return
    covers.sort()
    i = 0
    while i + 1 < len(covers):
        if covers[i + 1][0] <= covers[i][1] + 1:
            covers[i][1] = max(covers[i][1], covers[i + 1][1])
            del covers[i + 1]
        else:
            i += 1

def tuning_freq(coord):
    return coord[0] * 4_000_000 + coord[1]


class Solution(BaseSolution):
    def part1(self, ll) -> str:
        if len(ll) == 14:
            ROW = 10  # test input
        else:
            ROW = 2_000_000  # full input

        sbrs = [sbr for sbr in get_sensor_beacon_radius(ll)]

        covers = []
        for sbr in sbrs:
            cover = row_cover(ROW, sbr[0], sbr[1], sbr[2])
            if cover:
                covers.append(cover)
        merge_covers(covers)

        return str(sum([cover[1] - cover[0] + 1 for cover in covers]))

    def part2(self, ll) -> str:
        if len(ll) == 14:
            MAX_X = 20  # test input
        else:
            MAX_X = 4_000_000  # full input

        sbrs = [sbr for sbr in get_sensor_beacon_radius(ll)]

        # Each sensor sweep zone is defined by 4 perimeter lines. Two with gradient of +1:
        # - y = x + (sy-sx+r+1)
        # - y = x + (sy-sx-r-1)
        #
        # and two of gradient -1:
        # - y = -x + (sx+sy+r+1)
        # - y = -x + (sx+sy-r-1)
        #
        # (where (sx, sy) are the sensor's coordinates and r is the sensor's sweep radius
        acoeffs, bcoeffs = set(), set()
        for sbr in sbrs:
            acoeffs.add(sbr[0][1] - sbr[0][0] + sbr[2] + 1)
            acoeffs.add(sbr[0][1] - sbr[0][0] - sbr[2] - 1)
            bcoeffs.add(sbr[0][1] + sbr[0][0] + sbr[2] + 1)
            bcoeffs.add(sbr[0][1] + sbr[0][0] - sbr[2] - 1)

        # The solution coordinate must lie on the intersection of an "a" line and a "b" line
        for a, b in itertools.product(acoeffs, bcoeffs):
            p = ((b-a)//2, (a+b)//2)
            if all(0 < c and c < MAX_X for c in p):
                if all(distance(p, sbr[0]) > sbr[2] for sbr in sbrs):
                    return(str(tuning_freq(p)))

        assert False, "No solution found"

if __name__ == "__main__":
    Solution()
