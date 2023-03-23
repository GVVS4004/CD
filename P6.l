%{
 #include<stdio.h>
 #include<string.h>
 int flag=0;
 void display(char *s);
%}
dot [.]
num [0-9]+
nxt [\n]
%%
{dot} {flag=1;}
{num} {if(flag==1)display(yytext);}
{nxt} {flag=0;printf("\n");}
%%
int main()
{
yylex();
return 0;
}
void display(char *s)
{ 
 printf("%zu",strlen(s));
 
}
int yywrap()
{
return 1;
}
