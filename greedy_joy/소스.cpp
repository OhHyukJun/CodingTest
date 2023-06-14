#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int n = name.length();
    int direction = n - 1;
    for (int i = 0; i < n; i++) {
        if (name[i] - 'A' < 14)//아스키 코드 A=65 Z=90 최단거리를 고려해서 작성
            answer += name[i] - 'A';
        else answer += 'Z' - name[i] + 1;

        int a = i + 1;
        while (a < n && name[a] == 'A')a++;

        direction = min(direction, i + n - a + min(i, n - a)); //잘 이해가 안됨 더 공부해야 할 듯
    }
    answer += direction;
    return answer;
}