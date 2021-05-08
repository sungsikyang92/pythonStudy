hrs, mins = map(int, input().split())
a = (hrs*60)+mins-30
print('%d %d' %(((a//60)+24)%24,(a%60)))