#!/usr/bin/env python3

def part1():
    offset = ord('X') - ord('A')
    # print(offset)

    f = open('02.txt', 'r')
    pts = 0
    for l in f.readlines():
        # print(l.rstrip())
        them, me = l.rstrip().split(' ')
        # print(f"them: {them}, me: {me}")
        diff = (ord(me) - (ord(them) - offset)) % 3
        # print(diff)
        game_pts = diff * 3
        me_pts = ord(me) - ord('W')
        # print(f"game: {game_pts}, me: {me_pts}, total: {game_pts + me_pts}")
        pts += game_pts + me_pts

    print(f"Part 1: {pts}")

def part2():
    offset = ord('X') - ord('A')

    f = open('02.txt', 'r')
    pts = 0
    for l in f.readlines():
        # print(l.rstrip())
        them, win = l.rstrip().split(' ')
        # print(f"them: {them}, me: {me}")
        me_pts = ((ord(them) - ord('A')) + (ord(win) - ord('Y'))) % 3 + 1
        # print(diff)
        win_pts = (ord(win) - ord('X')) * 3
        # print(f"me: {me_pts}, win: {win_pts}, total: {me_pts + win_pts}")
        pts += me_pts + win_pts

    print(f"Part 2: {pts}")

if __name__ == "__main__":
    part1()
    part2()
