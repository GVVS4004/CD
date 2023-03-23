%{
    #include<stdio.h>
    #include<stdlib.h>
   
%}



%%
^(a|A)[a-z]*[0-9]* {printf("starting with a");}
%%

int main(){
    yylex();
    return 0;
}
int yywrap(){
    return 1;
}

