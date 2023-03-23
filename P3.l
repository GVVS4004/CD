%{
 /*LEX to recognize  keywords and identifiers  */
%}
letter [a-z][A-Z][0-9]*[a-z0-9]+
digit [0-9]*
%%
int|float|char|double|else|for|if|while  {printf("\n reserved words is %s ",yytext);}
letter(digit|letter)*                    {printf("valid identifiers is %s \n", yytext);}
%%
main()
{
yylex();
}
int  yywrap()
{
 return 1;
}