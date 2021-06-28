from Stack import Stack
import pandas as pd

data = Stack()
# #test.csv
# data = {
#     '번호':[1,2,3,4],
#     '이름':['수지','예지','구지','화질구지'],
#     '성별':['여자','외계인','남자','자웅동체'],
#     '비고':['1','2','1','2']
# }

#test2.csv
df = pd.DataFrame(columns=['num', 'name', 'region'])
for x in range(10000):
    df.loc[x] = [str(x), '연습'+str(x), '지역'+str(x)]
#test2에서 10000개의 데이터를 생성해보았다.

# test4.csv
# data = pd.DataFrame([])

df.to_csv('/Users/sikkky/ESD/test5.csv', index = False)