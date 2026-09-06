a, b, c, d = map(int, input().split())

# Please write your code here.
if b > d:
    c -= 1
    d += 60

hour_gap = c - a
minute_gap = d - b

answer = hour_gap * 60 + minute_gap
print(answer)