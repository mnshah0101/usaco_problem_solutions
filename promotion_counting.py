import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

bronze_before, bronze_after = [int(x) for x in input().split()]
silver_before, silver_after = [int(x) for x in input().split()]
gold_before, gold_after = [int(x) for x in input().split()]
platinum_before, platinum_after = [int(x) for x in input().split()]


new = (bronze_after + silver_after + gold_after +
       platinum_after) - (bronze_before + silver_before + gold_before + platinum_before)

#promoted from bronze to silver
promoted_first = (new + bronze_before) - bronze_after
promoted_second = (promoted_first + silver_before) - silver_after
promoted_third = (promoted_second + gold_before) - gold_after

print(promoted_first)
print(promoted_second)
print(promoted_third)





