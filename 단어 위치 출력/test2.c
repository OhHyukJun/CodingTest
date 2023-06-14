#include <stdio.h>
#pragma warning(disable : 4996)

int main(void) {
	/*
		최대 길이가 30인 소문자로 이루어진 단어S를 입력받고 
		각 알파벳의 위치를 출력 해당되지 않으면 -1 출력 초기 위치는 0
		소문자로만 이루어진 단어 S
		S의 길이는 30을 넘지 않게 설정 S.length<=30
		구현을 어떻게 할 것인가
		S는 0으로 초기화 -> 배열로 설정?
		
	*/
	char S[30] = { 0 };//배열을 0으로 초기화
	scanf("%s",S);
	for (int i = 97; i <= 122; i++) {
		//아스키 코드 97~122가 소문자 알파벳
		int j = 0;
		while (S[j] != 0) {
			if (S[j] == (char)i)break;
			j++;
		}
		if (S[j] == (char)i) 
			printf("%d ", j);
		else 
			printf("-1 ");
	}
}	