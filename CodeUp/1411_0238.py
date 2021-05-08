count = int(input())
lost_Card = []
origin_Card = []

for x in range(1, count+1):
    origin_Card.append(x)
for x in range(count-1):
    lost_Card.append(int(input()))

for card in lost_Card:
    origin_Card.remove(card)

print(origin_Card[0])