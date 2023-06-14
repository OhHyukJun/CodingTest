#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

/*n원을 계산하는 최소 동전의 수
int n;
int coin[4] = {500,100,50,10};
int ans;
int main() {
	cin >> n;
	for (int i = 0; i < 4; i++) {
		ans += (n / coin[i]);
		n = n % coin[i];
		i++;
	}cout << ans;
}
*/

/*
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여
가장 큰 수를 만들어야함 단,특정 인덱스에 해당하는 수가 연속으로
k번 초과해서 더해질 수 없음
*/

/*
체육복을 도난당함
여벌 체육복이 있는 학생이 빌려줘야함(앞뒤 번호의 사람만 빌려줄 수 잇음
체격 순-오름차순
전체 학생의 수:n
도난 당한 학생 배열:lost
여벌이 있는 학생의 번호가 담긴 배열: reverse
체육 수업을 들을 수 있는 학생의 최댓값
*/

int solution(int n, vector<int> lost, vector<int> reserve) {
	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j]) {
				lost.erase(lost.begin() + i);//시작부터 i번 쨰의 값을 삭제한다
				reserve.erase(reserve.begin() + j);
				i = -1;
				break;
			}
		}
	}//입력받은 잃어버린 사람 배열과 빌려주는 사람 배열이 같은 경우 이를 삭제하는 절차
	
	int answer = n-lost.size();
	//정답의 초기값 정의

	sort(lost.begin(), lost.end());//시작부터 끝까지 정렬한다
	sort(reserve.begin(), reserve.end());
	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j] - 1 || lost[i] == reserve[j] + 1) 
			{
				answer++;
				reserve.erase(reserve.begin() + j);
				break;
			}//앞 뒤 번호의 사람일 경우 빌려주는 절차
		}
	}
	return answer;
}

