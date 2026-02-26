#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        if s == "10":
            return 1
        if s == "1":
            return 0
        x = {"1":0, "0":0}
        zf = 0
        for i in s:
            x[i] += 1
        if x["1"] == 1:
            return len(s) - 1
        if x["0"] == 0:
            return len(s) + 1
        for i in s[::-1]:
            if i == "1":
                if x["0"] > 0:
                    x["0"] -= 1
                    steps += 2
                    zf += 1
                else:
                    # this means all left are 1s
                    steps += (x["1"] + 1)
                    break
            else:
                if x["0"] > 0:
                    x["0"] -= 1
                    if zf>0:
                        steps += 2
                        #zf -= 1
                    else:
                        steps += 1
                else:
                    steps += (x["1"] + 1)
                    break
            #  print(steps, x)
        return steps
