#include<iostream>
using namespace std;

int main()
{
    double t;
    double ph;
    double h;

    cin >> t >> ph >> h;

    if (t < 10 or t > 30) {
        cout << "Loi input" << endl;
        return -1;

    }
    if (ph < 4 or ph > 7) {
        cout << "Loi input" << endl;
        return -1;
    }

    if (h < 0 or h > 5.5) {
        cout << "Loi input" << endl;
        return -1;
    }

    if (t >= 27 and ph >= 6.5 and h >= 4.5) {
        cout << "Tha bachtuoc" << endl;
    }

    else if (t >= 25 and ph >= 5.5 and h >= 4.5) {
        cout << "Tha ca" << endl;
    }

    else if (t >= 25 and ph >= 4 and h >= 3) {
        cout << "Tha tom" << endl;
    }

    else {
        cout << "nothing!" << endl;
    }
    return 0;
}