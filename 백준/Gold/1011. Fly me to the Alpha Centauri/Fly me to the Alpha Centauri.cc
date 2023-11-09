#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) {
		int x, y;
		cin >> x >> y;
		int leng = y - x;
		int result = 0;
		for (int i = 1; leng > 0; i++) {
			leng -= i;
			result++;
			if (leng <= 0)
				break;
			leng -= i;
			result++;
		}
		cout << result << endl;
	}
	return 0;
}