/*
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
*/

#include <stdio.h>

int find(int index) {
	int* trial = new int[index + 1];
	for (int i = 0; i <= index; i++) {
		if (i == 0 || i == 1)
			trial[i] = 0;
		else if (i % 6 == 0) {
			trial[i] = (((trial[i / 3] < trial[i - 1]) ? trial[i / 3] : trial[i - 1]) < trial[i / 2] ?
				((trial[i / 3] < trial[i - 1]) ? trial[i / 3] : trial[i - 1]) : trial[i / 2]) + 1;
		}
		else if (i % 3 == 0) 
			trial[i] = ((trial[i / 3] < trial[i - 1]) ? trial[i / 3] : trial[i - 1]) + 1;
		else if (i % 2 == 0)
			trial[i] = ((trial[i / 2] < trial[i - 1]) ? trial[i / 2] : trial[i - 1]) + 1;
		else
			trial[i] = trial[i - 1] + 1;
	}
	int result = trial[index];
	delete[] trial;
	return result;
}

int main() {
	int n;
	scanf("%d", &n);	
	printf("%d", find(n));
}