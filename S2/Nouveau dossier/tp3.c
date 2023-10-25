%{

    tab ("\t")

%}
%%

%%
#include <stdio.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("Utilisation : %s file_in file_out", argv[0]);
        exit(EXIT_FAILURE);
    }

    yyin = fopen(argv[1], "r");
    yyout = fopen(argv[2], "w");
    if (yyin == NULL || yyout == NULL) {
        perror("Erreur lors de l'ouverture du fichier ");
        exit(EXIT_FAILURE);
    }                                           

    int j;
    while ((j = yylex()) != 0) {
        switch(j) {
        default :
            printf("Lexeme filtrÃ© : %s\n", yytext); // copier le texte sans changement 
            break;
        }
    }

    fclose(yyin); 
    fclose(yyout);
    return 0;
}
