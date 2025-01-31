#include <stdio.h>

int main() {
    char str[] = "!@#$%^&*(\\'\"<>?:;";
    int i;

    for (i = 0; str[i] != '\0'; i++) {
        printf("%c", str[i]);
    }

    printf("\n");

    return 0;
}