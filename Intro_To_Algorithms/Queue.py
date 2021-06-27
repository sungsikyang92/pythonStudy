from collections import deque
# 빈 큐 만들기
deque1 = deque()
# 큐에 원소 추가
deque1.append(1)
# 큐에서 원소 삭제
deque1.popleft()
# 큐의 모든 원소 삭제
deque1.clear()
# 큐의 원소수 찾기
deque1.__len__()
len(deque1)