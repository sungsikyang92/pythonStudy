inp = int(input())
dist = list(map(int, (input().split())))
price = list(map(int, (input().split())))
# print(dist)
# print(price)
cost = 0
comp = price[0]
for i in range(inp-1):
    if price[i] < comp:
        comp = price[i]
    cost += comp * dist[i]
print(cost)