/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
*/

/* string을 이용한 풀이
#include <iostream>
#include <string>
using namespace std;

int main() {
	int T;
	cin >> T;
	string str, aa, bb;
	for (int i = 0; i < T; i++) {
		cin >> str;
		aa = str.substr(0, 1);
		bb = str.substr(2, 1);
		int a, b;
		a = stoi(aa);
		b = stoi(bb);
		cout << a + b << endl;
	}
}
*/

#include <stdio.h>

int a, b, t;
int main() {
	scanf("%d", &t);
	while (t--) {
		scanf("%d,%d", &a, &b);
		printf("%d\n", a + b);
	}
}