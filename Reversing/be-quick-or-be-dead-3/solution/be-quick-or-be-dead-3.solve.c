#include <stdio.h>
#define X 0x186b5

int calculated[X];

int _calc(int x) {
    if (x < 5)
        return x*x+0x2345;
    int x_1 = calculated[x-1];
    int x_2 = calculated[x-2];
    int x_3 = calculated[x-3];
    int x_4 = calculated[x-4];
    int x_5 = calculated[x-5];
    return (x_1-x_2)+(x_3-x_4)+(x_5*0x1234);
}

int calc(int x) {
    for (int i = 0; i <= x; i++)
        calculated[i] = _calc(i);
    return calculated[x];
}

int main(void) {
    printf("%d", calc(X));
}