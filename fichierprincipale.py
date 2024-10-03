"""
author : Jean TROUSSIER
date : jeudi 3 octobre
obj :  fichier principale du pendu textuelle
to do :
"""
import mainfunction as mf

score = 0
highscore = 0
unsigned_int_live = 0
list_char_lettre_du_mot = []
list_char_lettre_joueur = []
list_char_lettre_joueur_fausse = []
unsigned_int_indicator_victory = 0
as_it_began = False

while(1):
    if is_it_the_first_game == True :
        is_it_the_first_game = False
        score = 0
    if as_it_began == True:
        unsigned_int_indicator_victory = mf.void_afficher_mot(unsigned_int_indicator_victory, list_char_lettre_joueur, list_char_lettre_joueur_fausse,list_char_lettre_du_mot)
    if as_it_began == False:
        unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse = mf.initialiser(unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse)
        as_it_began = True
        list_char_lettre_du_mot = mf.list_char_word_seperator(mf.string_word_chooser(mf.list_string_mot("dictionnaire/dico.txt")),list_char_lettre_du_mot)[:]
        mf.list_char_letter_starter(list_char_lettre_du_mot,list_char_lettre_joueur)
    elif mf.bool_death_tester(unsigned_int_live) == True:
        print("vous avez perdu...")
        if highscore < score:
            score == highscore
    elif mf.bool_word_found(unsigned_int_indicator_victory,list_char_lettre_du_mot) == True:
        print("vous avez gagné")
        score += 1
    else :
        char_letter_chosen = input("veuillez entrer une lettre :")
        while mf.bool_is_it_a_char(char_letter_chosen) != True:
            print("la lettre entrée n'est pas valide...")
            char_letter_chosen = input("veuillez entrer une lettre :")
        unsigned_int_live, list_char_lettre_joueur, list_char_lettre_joueur_fausse = mf.void_letter_checker_function(char_letter_chosen,unsigned_int_live,list_char_lettre_joueur,list_char_lettre_du_mot,list_char_lettre_joueur_fausse)