#include <stdio.h>

int mccathy(int n) {
    if (n > 100) {return n - 10;}
    else {return mccathy(mccathy(n + 11));}
}

int main() {
    printf("%d\n", mccathy(0));
}