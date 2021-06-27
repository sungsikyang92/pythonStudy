razor = list(input())
answer = 0
st = []

for i in range(len(razor)):
    if razor[i] == '(':
        st.append('(')

    else:
        if razor[i-1] == '('