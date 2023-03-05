#include <stdio.h>
void main() {
    int value = 0;
    char orbital[5] = {'s', 'p', 'd', 'f', 'g'};
    printf("The Maximum Number of Electrons in Each Orbital Shells\n");
    for(value = 0; value<=4; value++) {
        printf("%c = %d\n", orbital[value], 2*(value*2+1));
    }
}