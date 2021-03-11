#include <iostream>
using namespace std;

int main() {
	int a, b, t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> a >> b;
		cout << "Case #" << i << ": " << a << " + " << b << " = " << a + b << endl;
	}
}

/* scanf, printf 이용
#include <stdio.h>

int main() {
	int a, b, t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d\n", i, a, b, a + b);
	}
}
*/