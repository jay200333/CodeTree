n = int(input())
weather = []


for _ in range(n):
    d, dy, w = input().split()
    weather.append((d, dy, w))

# Please write your code here.
weather = sorted([info for info in weather if info[2] == 'Rain'], key=lambda x: x[0])
print(f"{weather[0][0]} {weather[0][1]} {weather[0][2]}")