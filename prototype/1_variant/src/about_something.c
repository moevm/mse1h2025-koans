// #include "c_koans.h"
#include <stdio.h>

#ifndef C_VAL
#define C_VAL 'C'
#endif

#ifndef INT_VAL
#define INT_VAL 5
#endif

int main() {
    // Выводим переданные параметры
    printf("From C file\nC_VAL: %c \nINT_VAL: %d\n", C_VAL, INT_VAL);
}
