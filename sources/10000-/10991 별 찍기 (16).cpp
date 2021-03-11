/*
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제
4
   *
  * *
 * * *
* * * *
*/

#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N - i; j++)
			printf(" ");
		for (int j = 1; j <= i; j++) {
			printf("* ");
		}
		printf("\n");
	}
}