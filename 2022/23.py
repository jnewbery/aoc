#!/usr/bin/env python3
def part1(ll):
    raise NotImplementedError

def part2(ll):
    raise NotImplementedError

TEST_INPUT = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

TEST_SOL = [110]

FULL_INPUT = """...##..#.##.#..####....###..#.#..#.###.######.###...#...#.....###..##.#
..##.##.######.#.###.#.......#...####..####.###...#....#.##..#.#####.##
###.#.###.#.#..#.#.#..#.#.#####.#....#..###..#..#......####.#..####..##
.##...#.#..#.#..#.#.#.#....#.####...#..#..##.#...##.#..#.#.#.#......###
##..#.#.#.#.#.##.##.#.#...#.###.#...####...##..##..#.###.##.######..#.#
#.#.#....##.###....#.......######.....##.####.#.###...###.#.#...#####..
.##.....######.#......###.###.....#####...#..#####.#.#.##....#.#....##.
#...##.#....#.#.###.##.#..###.#...##...#.##.##.#..#.####.#.#.#.#.#...#.
.#.#.####.#...#..####.#...##.#.#.###.##..###..#.#.#.####.#.....#.##..#.
.#..#.#..##..######..#.##.##.##.#....#..#..#.##..###.#.#....###......#.
.####...#.##..##....#...#####.##.###......#.......#..##.#....###.......
.....#.#####...####.###..#.#.###.#..#.......#..........##.#####.#...#..
.....##..####...#.#...#.###...#..##.###......#.#..#....##...####....##.
.####..#.#.####.##.##..###..#...#.#.##.#..####.....####.#.#.##...#.....
..#..#..##..#.#....##..#####...#...#####....#....#..###.###.####.#...#.
.###.#.#####.###...#.#.##.##..###.#.##.##.####.###..#.......##...###...
####.#.#....#.###.#.##..###.#.##..##.#..##..###.####...###....#####..##
.##.#####..#.#.#.#...#......###.###.#....####.....#..#......##...###...
#.##.###.####.##.#..#.#...#..##..##....####.#..#..####...#.##.##.#.#..#
.....##.#####..#..#.##.......#######..##.##.....#..###...#####.....##..
..#..###...####.#.#.......###...##..#.######...#....#...#..##...###...#
##.#...###..#.###.##...#.#..#.#.##..#.###..#..#.####......##.#.#.####..
.###...###..#.#.##.###.##..##.#.#...###....#..##.#..###..##..####.#..#.
#..#.#....#...#.###.#....##..#....##.#...#.....#..#......#.#...#.#.###.
.##.#....##.##..###..#.#..####.###...##.#.##.####..#.####..#..##.##....
#.#.####..#...#.#.####....#..###..#..##....##...#.#.#.#.##.#...#.###...
######..#.#####.###..##.#####.#..#.#.#.#.......##.#.#..#....##.#.#...##
####....##.#..###....###.....#..#...##.##...#......#..##..#.#...####..#
.##..#####.#..##..##...#.#.#..#....#.####..##.......#.##.#.###.#.#..##.
.##...####..#..##..##.###....#....#..##.#.#.##......#.#.##...##.#####..
....#..###.##..##...###.##.##...#....#..####.#####.###..#.###.#.#.#..##
##.#.#.#.#...#######..#.##..#.#.#.####.#.###...##.######.##.....##.#..#
...###..#.##.#..#.###.....#####.##.##.#.##.#.#..##..###.#........#.#.##
.#....#.#.#..####....#.###.#.#.#..##..####..#..#.#...####..#..#..#.##..
##...#.#.##.##.#.###.#.#...######.###.....####.##..######..#..##.......
#.##.#.###..#....##....#.##.##...#####.##.######.....##.#...#.##..#.###
#..#....##.###..####..#..##.###....#..###....########...#..##.######...
##..####..##.#.###..#..####.##.##......##...###.##.###.###..#.###.#####
##.#.#..#.#.###.....#.#.#..####.#.##########...##.#.#.###.#.##..#.##.#.
#.##########.#.#.#..#######....#..##.#.###..##.....#.#..##..###.#.....#
#.##.##..##.##.########..#.#.###.#..##...#######.######.#.#.###..#..##.
...#.#..###...#.#..#.#.#.######...####.#..######.######...#.#...#.#.##.
#######.####.###.....##.#..#####.#....####....##.#.##..##.##..#....#.#.
.#.#.#..##.#.#....##.###.......##...#..##..####....####.#.#.#.###..##..
.#..####.#...#..#.##...#####.##..##.###......#.#..#.#.#.#..####.#.##..#
.###.#.####.####.####..#..#..#.#...#...#####....##.#..#.#####.##..###..
.#..#.##..#...##.##......#.#.#......##.#..#...####...##.#.##.#.#.####..
###.#.##.#.#########..##.#..##.#.#..#.#.#...##.##.#.#...#.#####.......#
..###...#..#..#.##.#.#.#.###....##..#..###.#.#.#........#.#...#..##.#.#
.###....##.########..##.#.##..#.##...##.###.#...#..#..##..##...##...#.#
##...#..##.#.#.##.#.#....##....###.##...###.#####..##.....##........#.#
..#...#.######..#.....#.#.##.#.#.###..##...##.#..#..#.#......#.##..#...
#...........#..##.####.###.#.....##....##.#.##..#...#..#####...##...#.#
....#..####...##..###..#####.#..####.###..#.##..###..#.#.##.#.########.
..#.#......####..#.##..#.###.##.#.###..#..#.###.#....#.##.##..#..##..#.
####.##.#.###.#.#######.###.......##..####.#.....##...##...###..###..#.
#....#..####.#..#.#.#.###.##........##.#..##.#..#.#..##..#...##.#...##.
#...###.###.#.#..##......#..###..##.#....###...#...##..#..#####.####.#.
######..####...####.##.....###..#...###.##......#..#.##.##.###.##.####.
..##......#......##.####..#..###....#..#..#.....#..##.....###.####..#.#
#####.###..##.....#....#...##.#.##...#.#.#.#..##.#..#...#..####...##...
.##..#.#...##..##..#.###.#.#.#...#####..#.####..###..##....##.####..#..
##...#####....#.#.##.###.#.#..##.#...#.#.#.####.....#.#..##.#...#......
#......###.###.###......##.####.#.####...##..#.#.#......######.#.#.#..#
..##.###.##.#.#.###.#.###.####..#..###########.##.##.#..#......##.#.###
..#.###....##.....###......##.##...##.#..###..#..#.#..###....######.##.
#####.#####.#.#.####...#########....#.....#...##..#.....###..###.######
.##.#####.#....#.#.#......##..##.#####...#.####.#.##..#..##..####...#..
####.##.###.#..#...##...##.#..##.....#..##..#####...........##..#..###.
##.##.####.#.#.....#.#.#..#..###..###.........#..#.#..####.##........##
.#.###......#...#..##.##...#..#..#.#..#.##.#.#.####..###.....#.###.#..#"""

FULL_SOL = []
