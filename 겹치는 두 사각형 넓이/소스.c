#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>



int main(void) {
	/*
		좌표값을 입력받고 두 개의 사각형을 만들어 겹치는 영역의 넓이 구하기
		겹치지 않으면 -1 출력
		2. 입력받은 두 사각형이 겹치는 경우를 생각하고 코드 작성
		a. x1,y1,x2,y2 -> 왼쪽 오른쪽 위 아래 값 구하기


		넓이 0이 출력되는 경우를 포함해서 구현
		박스 내에 박스가 있는 경우
	*/



	int x1, y1, x2, y2;
	int x3, y3, x4, y4;

	printf("");
	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
	printf("");
	scanf("%d %d %d %d", &x3, &y3, &x4, &y4);
	0 <= x1, y1, x2, y2, x3, y3, x4, y4 <= 256;

	int a, b;

	if ((x1 <= x3 && x3 <= x2 && x2 <= x4) || (x2 <= x3 && x3 <= x1 && x1 <= x4)) {
		if (x1 <= x2)
			a = x2 - x3;
		else
			a = x1 - x3;
	}
	else if ((x1 <= x4 && x4 <= x2 && x2 <= x3) || (x2 <= x4 && x4 <= x1 && x1 <= x3)) {
		if (x1 <= x2)
			a = x2 - x4;
		else
			a = x1 - x4;
	}
	else if ((x3 <= x1 && x1 <= x4 && x4 <= x2) || (x4 <= x1 && x1 <= x3 && x3 <= x2)) {
		if (x3 <= x4)
			a = x4 - x1;
		else
			a = x3 - x1;
	}
	else if ((x3 <= x2 && x2 <= x4 && x4 <= x1) || (x4 <= x2 && x2 <= x3 && x3 <= x1)) {
		if (x3 <= x4)
			a = x4 - x2;
		else
			a = x3 - x2;
	}
	else if ((x1 <= x3 && x3 <= x4 && x4 <= x2) || (x1 <= x4 && x4 <= x3 && x3 <= x2)) {
		if (x3 <= x4)
			a = x4 - x3;
		else
			a = x3 - x4;
	}
	else if ((x2 <= x3 && x3 <= x4 && x4 <= x1) || (x2 <= x4 && x4 <= x3 && x3 <= x1)) {
		if (x3 <= x4)
			a = x4 - x3;
		else
			a = x3 - x4;
	}
	else {
		a = -1;
		switch (a) {
		case -1:
			printf("%d", -1);
			break;
		}
	}

	if (a != -1) {
		if ((y1 <= y3 && y3 <= y2 && y2 <= y4) || (y2 <= y3 && y3 <= y1 && y1 <= y4)) {
			if (y1 <= y2)
				b = y2 - y3;
			else
				b = y1 - y3;
		}
		else if ((y1 <= y4 && y4 <= y2 && y2 <= y3) || (y2 <= y4 && y4 <= y1 && y1 <= y3)) {
			if (y1 <= y2)
				b = y2 - y4;
			else
				b = y1 - y4;
		}
		else if ((y3 <= y1 && y1 <= y4 && y4 <= y2) || (y4 <= y1 && y1 <= y3 && y3 <= y2)) {
			if (y3 <= y4)
				b = y4 - y1;
			else
				b = y3 - y1;
		}
		else if ((y3 <= y2 && y2 <= y4 && y4 <= y1) || (y4 <= y2 && y2 <= y3 && y3 <= y1)) {
			if (y3 <= y4)
				b = y4 - y2;
			else
				b = y3 - y2;
		}
		else if ((y1 <= y3 && y3 <= y4 && y4 <= y2) || (y1 <= y4 && y4 <= y3 && y3 <= y2)) {
			if (y3 <= y4)
				b = y4 - y3;
			else
				b = y3 - y4;
		}
		else if ((y2 <= y3 && y3 <= y4 && y4 <= y1) || (y2 <= y4 && y4 <= y3 && y3 <= y1)) {
			if (y3 <= y4)
				b = y4 - y3;
			else
				b = y3 - y4;
		}
		else {
			b = -1;
			switch (b) {
			case -1:
				printf("%d", -1);
				break;
			}
		}
	}

	if (a != -1 && b != -1) {
		if (a * b == 0) {
			printf("%d", -1);
		}
		else printf("%d", (a * b));
	}



}