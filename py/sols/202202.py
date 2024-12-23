#!/usr/bin/env python3
from utils import BaseSolution

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        offset = ord('X') - ord('A')
        # print(offset)

        pts = 0
        for l in ll:
            # print(l.rstrip())
            them, me = l.rstrip().split(' ')
            # print(f"them: {them}, me: {me}")
            diff = (ord(me) - (ord(them) - offset)) % 3
            # print(diff)
            game_pts = diff * 3
            me_pts = ord(me) - ord('W')
            # print(f"game: {game_pts}, me: {me_pts}, total: {game_pts + me_pts}")
            pts += game_pts + me_pts

        return str(pts)

    def part2(self, ll) -> str:
        pts = 0
        for l in ll:
            # print(l.rstrip())
            them, win = l.rstrip().split(' ')
            # print(f"them: {them}, me: {me}")
            me_pts = ((ord(them) - ord('A')) + (ord(win) - ord('Y'))) % 3 + 1
            # print(diff)
            win_pts = (ord(win) - ord('X')) * 3
            # print(f"me: {me_pts}, win: {win_pts}, total: {me_pts + win_pts}")
            pts += me_pts + win_pts

        return str(pts)

if __name__ == "__main__":
    Solution()
