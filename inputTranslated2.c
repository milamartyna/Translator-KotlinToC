#include <stdio.h>
int complex_add (int a)
{
int c = 5;
 int d = 10;
 while ((a<=15)&&(c>d)){
c--;
 a++;
}
 return a+d;
}
int run (int argCount, char*  args)
{
int a = 8;
 int b = 9;
 while (a<=b){
printf('Aloha');
 a++;
}
 if (argCount>1){
return 1;
}
 else {
return complex_add(a);
}
}
int main (int argCount, char*  args)
{
run(2, 'stringArg');
 return 0;
}

