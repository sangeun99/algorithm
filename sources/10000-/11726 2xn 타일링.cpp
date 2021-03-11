/*
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
*/

#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	
	int** C;
	C = new int* [n + 1];
	for (int i = 0; i <= n; i++)
		C[i] = new int[n + 1];

	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0 || j == i)
				C[i][j] = 1;
			else
				C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % 10007;
		}
	}
	
	int answer = 0;
	for (int i = 0; i < n / 2 + 1; i++) {
		answer += C[n - i][i] % 10007;
	}
	for (int i = 0; i <= n; i++)
		delete[] C[i];
	delete[] C;
	printf("%d", answer % 10007);
}