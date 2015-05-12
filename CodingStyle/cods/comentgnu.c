/*
Developed: Osandi Augusto
Date: 25/03/2015     
Program: Example of comment
File: example.c
*/
#include <stdio.h>
#include <stdlib.h>

int main () 
{
    int n, num, factor = 2, cont = 0;
    printf("Enter the number to be factored : ");
    scanf ("%d", &n);
    while ( n != 1 ) {
        while (n%factor  == 0) { // count how many times
            cont++;
            n = n / factor;
        }
        if (cont != 0) {
            // the previously tested factor is really a factor n
            printf ("factor  %d x %d\n", factor, cont);
            cont = 0;
        }
        factor ++;
    }    

    return 0;
}
