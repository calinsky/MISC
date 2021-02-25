#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rebecca Calinsky
# Time complexity:  O(N)
# Space complexity: O(N)
#                   Storage of number in list is no larger than
#                   max(len(a), len(b)) +1


class LargeInt:
    def __init__( self, str_int = "" ):
        self.sign = -1  if len(str_int) > 1 and str_int[0] == "-" else  +1
        if self.sign < 0:  str_int = str_int[1:]
        self.str_int = str_int.lstrip("0")
        
    def __repr__( self ):
        sign = "-"  if self.sign < 0 and self.str_int else  ""
        val = self.str_int or "0"
        return sign + val

    
    # a.add(b)
    def add( self, b ):
        # ensure |a| > |b|
        a, b = (self, b)  if len(self.str_int) > len(b.str_int) else  (b, self)
        # init output array with reversed 'a' digits (extra zero for final carry)
        result_list = [d  for d in a.str_int[::-1]] + [0]

        s = 0
        for i, d in enumerate(result_list):
            s += int(d)
            if i < len(b.str_int):  s += int(b.str_int[-1 - i]) *(a.sign * b.sign)
            result_list[i] = str(s % 10)
            s //= 10

        # reverse array and join as string
        result = LargeInt("".join(result_list[::-1]))
        result.sign = a.sign

        return result
    

# %% test cases (raise error if incorrect)

A = [                            "10000000000000000000000000000000000",   "0008", "-107", "107", "-107", "107",   "-1",    "1",    "-1",    "1",  "-111",  "111",  "-111",  "111",   "100", "-0",  "", "00234"]
B = [ "99999999999999999999999999990000000000000000000000000000000000",  "-0009",   "69",  "69",  "-69", "-69",  "999",  "999",  "-999", "-999",   "999",  "999",  "-999", "-999",  "-100", "-0",  "", "00345"]
C = ["100000000000000000000000000000000000000000000000000000000000000",     "-1",  "-38", "176", "-176",  "38",  "998", "1000", "-1000", "-998",   "888", "1110", "-1110", "-888",     "0",  "0", "0",   "579"]

for a,b,c in zip(A, B, C):
    a = LargeInt(a)
    b = LargeInt(b)
    a_plus_b = a.add(b)
    print(f"{a_plus_b} = {a} + {b}")
    print(c)
    assert(str(a_plus_b) == c)
    print()
