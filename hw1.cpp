#include<iostream>
using namespace std;

int main()
{
    double t;
    double ph;
    double h;

    cin >> t >> ph >> h;

    if (t < 20 or t > 30) {
        cout << "Lỗi đầu vào, vui lòng thử lại!";
        return -1;

    }

    if (ph < 4 or ph > 7) {
        cout << "Lỗi đầu vào, vui lòng thử lại!";
        return -1;
    }

    if (h < 0 or h > 5.5) {
        cout << "Lỗi đầu vào, vui lòng thử lại!";
        return -1;
    }

    if (t >= 27 and ph >= 6.5 and h >= 4.5) {
        cout << "Thả bạch tuộc" << endl;
    }

	else if (t >= 25 and ph >= 5.5 and h >= 4.5) {
        cout << "Thả cá" << endl;
    }

    else if (t >= 25 and ph >= 4 and h >= 3) {
        cout << "Thả tôm" << endl;
    }

    else {
        cout << "Không thả gì cả!" << endl;
    }

    return 0;
}
