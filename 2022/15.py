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

def part1(ll):
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

    return sum([cover[1] - cover[0] + 1 for cover in covers])

def tuning_freq(coord):
    return coord[0] * 4_000_000 + coord[1]

def part2(ll):
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
                return(tuning_freq(p))

TEST_INPUT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

TEST_SOL = [26, 56000011]

FULL_INPUT = """Sensor at x=545406, y=2945484: closest beacon is at x=772918, y=2626448
Sensor at x=80179, y=3385522: closest beacon is at x=772918, y=2626448
Sensor at x=2381966, y=3154542: closest beacon is at x=2475123, y=3089709
Sensor at x=2607868, y=1728571: closest beacon is at x=2715626, y=2000000
Sensor at x=746476, y=2796469: closest beacon is at x=772918, y=2626448
Sensor at x=911114, y=2487289: closest beacon is at x=772918, y=2626448
Sensor at x=2806673, y=3051666: closest beacon is at x=2475123, y=3089709
Sensor at x=1335361, y=3887240: closest beacon is at x=2505629, y=4282497
Sensor at x=2432913, y=3069935: closest beacon is at x=2475123, y=3089709
Sensor at x=1333433, y=35725: closest beacon is at x=1929144, y=529341
Sensor at x=2289207, y=1556729: closest beacon is at x=2715626, y=2000000
Sensor at x=2455525, y=3113066: closest beacon is at x=2475123, y=3089709
Sensor at x=3546858, y=3085529: closest beacon is at x=3629407, y=2984857
Sensor at x=3542939, y=2742086: closest beacon is at x=3629407, y=2984857
Sensor at x=2010918, y=2389107: closest beacon is at x=2715626, y=2000000
Sensor at x=3734968, y=3024964: closest beacon is at x=3629407, y=2984857
Sensor at x=2219206, y=337159: closest beacon is at x=1929144, y=529341
Sensor at x=1969253, y=890542: closest beacon is at x=1929144, y=529341
Sensor at x=3522991, y=3257032: closest beacon is at x=3629407, y=2984857
Sensor at x=2303155, y=3239124: closest beacon is at x=2475123, y=3089709
Sensor at x=2574308, y=111701: closest beacon is at x=1929144, y=529341
Sensor at x=14826, y=2490395: closest beacon is at x=772918, y=2626448
Sensor at x=3050752, y=2366125: closest beacon is at x=2715626, y=2000000
Sensor at x=3171811, y=2935106: closest beacon is at x=3629407, y=2984857
Sensor at x=3909938, y=1033557: closest beacon is at x=3493189, y=-546524
Sensor at x=1955751, y=452168: closest beacon is at x=1929144, y=529341
Sensor at x=2159272, y=614653: closest beacon is at x=1929144, y=529341
Sensor at x=3700981, y=2930103: closest beacon is at x=3629407, y=2984857
Sensor at x=3236266, y=3676457: closest beacon is at x=3373823, y=4223689
Sensor at x=3980003, y=3819278: closest beacon is at x=3373823, y=4223689
Sensor at x=1914391, y=723058: closest beacon is at x=1929144, y=529341
Sensor at x=474503, y=1200604: closest beacon is at x=-802154, y=776650
Sensor at x=2650714, y=3674470: closest beacon is at x=2505629, y=4282497
Sensor at x=1696740, y=586715: closest beacon is at x=1929144, y=529341
Sensor at x=3818789, y=2961752: closest beacon is at x=3629407, y=2984857"""

FULL_SOL = [5367037, 11914583249288]
