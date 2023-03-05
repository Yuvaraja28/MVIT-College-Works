#include <stdio.h>
#include <math.h>
float Degree_Radian(float degree) {
    degree = degree * 3.14; degree = degree / 180;
    return degree;
}
void main() {
    float Degree_Radian(float);
    float degree;
    int inp;
    printf("This is a Simple Program to Calculate Trigonometric Values\n");
    printf("Made by Yuvaraja.M CSE-B Ist Year");
    printf("\nSelect an Option to Calculate\n1] Sin\t2] Cos\t3] Tan\n> ");
    scanf("%d", &inp);
    if (inp == 1) {
        printf("Enter Sin Degree : "); scanf("%f", &degree);
        printf("The Sin Value is : %.2f\n", sin(Degree_Radian(degree)));
    } else if (inp == 2) {
        printf("Enter Cos Degree : "); scanf("%f", &degree);
        printf("The Cos Value is : %.2f\n", cos(Degree_Radian(degree)));
    } else if (inp == 3) {
        printf("Enter Tan Degree : "); scanf("%f", &degree);
        printf("The Tan Value is : %.2f\n", tan(Degree_Radian(degree)));
    } else {
        printf("There's no Choice with that Input\n");
    }
}