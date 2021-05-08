
##이진 탐색과 반복문 불변식
#코드 5.1 이진 탐색

#필수 조건: A는 오름차순으로 정렬되어 있다.
#결과: A[i - 1] < x <= A[i]인 i를 반환한다.
#이 때 A[-1] = 음의 무한대, A[n] = 양의 무한대라고 가정한다.
int binsearch(const vector<int>& A, int x){
    int n = A.size();
    int lo = -1, hi = n;

}