#include <stdio.h>
void main() {
    int input;
    printf("Describe your Illness:-\n1) Fever\t2) Cold\t\t3) Headache\n4) Diarrhea\t5) Vomiting\t6) Dizziness\nSelect the Illness that you are Facing > "); 
    scanf("%d", &input);
    switch(input) {
        case 1: printf("You should to take [ Paracetamol ] to cure your illness\n"); break;
        case 2: printf("You should to take [ Antihistamine ] to cure your illness\n"); break;
        case 3: printf("You should to take [ Aspirin ] to cure your illness\n"); break;
        case 4: printf("You should to take [ Imodium A-D ] to cure your illness\n"); break;
        case 5: printf("You should to take [ Bismuth Subsalicylate ] to cure your illness\n"); break;
        case 6: printf("You should to take [ Meclizine ] to cure your illness\n"); break;
        default: printf("You have Entered the Wrong Input\n"); break;
    }
}