#include <stdio.h>
#include <math.h>
void main() {
    float a;
    float b;
    float c;
    printf("Enter the First Side of the Triangle  : ");
    scanf("%f", &a);
    printf("Enter the Second Side of the Triangle : ");
    scanf("%f", &b);
    c = pow(a, 2);
    c = c + pow(b, 2);
    printf("The Hypotenuse Value is %0.2f", c);
}
