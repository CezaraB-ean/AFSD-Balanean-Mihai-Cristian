#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
int n;
void meniu_optiuni()
{
    printf("Alegeti una din problemele la care doriti rezolvarea.\n");
    printf("Optiunea: \n");
    printf("1. Se citește de la tastatură un numar natural n şi apoi n numere ȋntregi. Să se afişeze valoarea maximă dintre numerele citite şi frecvenṭa acesteia.\n");
    printf("2. Se citesc de la tastatură numerele naturale m si n. Să se afiseze cel mai mare divizor comun si cel ma mic multiplu comun ale acestor două numere.\n");
    printf("3. Se citesc doua numere naturale n si b (b<10) ). Sa se reprezinte numarul n in baza b.\n");
    printf("4. Sa se afiseze primele n numere din sirul lui Fibbonacci. (f1=0, f2=1)\n");
    printf("5. Iesire\n");
}
void cautare_maxim()
{
    printf("Introduceți o valoare urmată de un șir de valori cu lungimea egală cu prima valoare.\n");
    scanf("%d",&n);
    int x,frecventa = 0,maxim = -1;
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&x);
        if(maxim<x)
            {
            maxim = x;
            frecventa = 1;
            }
        else if (maxim == x)
            frecventa++;
    }
    printf("%d %d",maxim,frecventa);
}
void em_si_en()
{
    printf("Introduceți două valori, separate printr-un spațiu.\n");
    int m,divizor,multiplu;
    scanf("%d %d",&m,&n);
    for(int i = min(m,n);i>=1;i--)
    {
        if(m%i == 0 && n%i == 0)
        {
            divizor = i;
            break;
        }
    }
    multiplu = m * n / divizor;
    printf("%d %d",divizor,multiplu);
}
void n_in_baza_b()
{
    printf("Introduceți un număr și baza în care îl doriți (baza poate fi maxim 9).\n");
    int b = 0;
    long long int numar_nou = 0, p = 1;
    scanf("%d %d",&n,&b);
    while(n>=1)
    {
        numar_nou = numar_nou + n%b*p;
        printf("%d\n",numar_nou);
        n = n / b;
        p = p * 10;
    }
    printf("%d",numar_nou);
}
int main()
{
    SetConsoleOutputCP(CP_UTF8);
    meniu_optiuni();
    int s;
    scanf("%d",&s);
    switch(s)
    {
        case(1):
            cautare_maxim();
            break;
        case(2):
            em_si_en();
            break;
        case(3):
            n_in_baza_b();
            break;
        default:
            printf("Alegeți o opțiune validă!");
            break;
    }
    return 0;
}
