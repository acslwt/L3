%{
    /* ZONE DE DEFINITION (OPTIONNELLE) */
    /* ZONE DES REGLES apres le double pourcent (OBLIGATOIRE) */
%}
%%
a      {return 300;} 
ab+c   {return 301;}
bd     {/* ne rien faire : filtrer*/} 
. | \n{return -1} 
%% 
/* zone des fonction c*/
int main(){
    int j ;
    char*invite = "Saisissez un mot matchant a(b+c)|?bd suivi de EOF(CTRL-D) SVP :";
    printf(invite);
    while ((j=yylex()) != 0)
    printf("\nJeton : %i de lexeme %s\n%s",j ,yytext,invite);
}