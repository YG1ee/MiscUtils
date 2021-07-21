#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main() {
    int rnum;
    srand(time(NULL));
    for (int i = 0; i < 25; i++) {
        rnum = rand() % 123;
        if (rnum < '0') rnum = (rnum % 9) + '0';
        else if ('9' < rnum && rnum < 'A') rnum += 'A' - ':';

        printf("%c", rnum);
    }
    printf("salt!");
}
