#include <stdio.h>


void main() {
    int num = 7;
    int *p = &num;
    *p = 100;
    int **p1 = &p;
    //printf("%d\n", num);
    //printf("%d\n", *p);
    printf("%p\n", p);
    printf("%p\n", *p1);
    printf("%d\n", **p1);
    printf("%d\n", sizeof(p));
}