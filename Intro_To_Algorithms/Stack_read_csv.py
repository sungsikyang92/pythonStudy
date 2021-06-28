import pandas as pd

data = pd.read_csv(r"../venv/sample_data_50.csv")

selectdata = pd.DataFrame(data, columns=['가입자 ID', '연령대코드(5세단위)', '신장(5Cm단위)', '흡연상태'])

print(selectdata)
print("**********")
sd = selectdata.drop(columns='흡연상태') # column 열 삭제
# 행 삭제는?
print(sd)
print("****************************************")
sd2 = sd[25:50]
print(sd2)

# sd2.to_csv('/Users/sikkky/ESD/test3.csv', index = False)