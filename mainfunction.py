"""
author : Jean TROUSSIER
date : jeudi 3 octobre
obj :  fichier fonction du pendu textuelle
to do :
"""
import random as rd


def bool_is_it_a_char(string):
    if len(string) == 1:
        return True
    else:
        return False

def void_letter_checker_function(char_letter_to_be_tested,unsigned_int_live,list_char_lettre_joueur,list_char_lettre_du_mot,list_char_lettre_joueur_fausse):
    if char_letter_to_be_tested in list_char_lettre_du_mot and char_letter_to_be_tested not in list_char_lettre_joueur:
        print("vous avez trouvez une nouvelle lettre")
        list_char_lettre_joueur.append(list_char_lettre_joueur)
    elif (char_letter_to_be_tested not in list_char_lettre_du_mot and char_letter_to_be_tested in list_char_lettre_joueur_fausse) or char_letter_to_be_tested in list_char_lettre_joueur:
        print("la lettre que vous avez rentré a deja été utilisé")
    else:
        unsigned_int_live += 1
    return unsigned_int_live, list_char_lettre_joueur

def initialiser(unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse):
    unsigned_int_live = 0
    list_char_lettre_du_mot = []
    list_char_lettre_joueur = []
    list_char_lettre_joueur_fausse = []
    unsigned_int_indicator_victory = 0
    return unsigned_int_indicator_victory,unsigned_int_live,list_char_lettre_du_mot,list_char_lettre_joueur,list_char_lettre_joueur_fausse


def void_afficher_mot(unsigned_int_indicator_victory, list_char_lettre_joueur, list_char_lettre_joueur_fausse,list_char_lettre_du_mot):
    """
    fonction qui n'a aucune entré et qui affiche les lettres trouvés et cache celle qui ne l'ont pas été encore
    """
    unsigned_int_indicator_victory = 0
    for char_lettre in list_char_lettre_du_mot:
        if char_lettre in list_char_lettre_joueur:
            print(char_lettre, end='')
            unsigned_int_indicator_victory += 1
        else:
            print("_", end='')
    print("lettre fausse: ",list_char_lettre_joueur_fausse)
    print(" ")



def list_string_mot(stream_file):
    """
    input : stream_file
    output : list_string_file
    fonction qui lis et recupère chaque ligne d'un fichier contenu dans le repertoire "stream_file" et copie chaque ligne dans list_string_file
    """
    list_string_file =[]
    with open(stream_file,mode="r",encoding='utf-8') as file_is_read:
        for string_line in file_is_read:
            list_string_file.append(string_line.lower())
    return list_string_file

def string_word_chooser(list_string_file):
    """
    input : list_string_file
    output : string_word_to_guess
    fonction qui choisie 'aléatoirement' un mot dans une liste de mot
    """
    unsigned_int_index = rd.randint(1,len(list_string_file)) - 1
    string_word_to_guess = list_string_file[unsigned_int_index]
    print(string_word_to_guess)
    return string_word_to_guess

def list_char_word_seperator(string_word,list_char_lettre_du_mot):
    """
    input : string_word
    fonction qui transforme une string en liste de char
    """
    for char_buffer in string_word:
        list_char_lettre_du_mot.append(char_buffer)
    return list_char_lettre_du_mot

def list_char_letter_starter(list_char_lettre_du_mot,list_char_lettre_joueur):
    """
    fonction qui met choisie "aléatoirement" une lettre et l'ajoute dans la liste du joueur
    """
    unsigned_int_index = rd.randint(1,len(list_char_lettre_du_mot)) - 1
    list_char_lettre_joueur.append(list_char_lettre_du_mot[unsigned_int_index])

def bool_death_tester(unsigned_int_live):
    """
    fonction qui vérifie que le joueur n'a pas perdu
    """
    if unsigned_int_live == 8:
        return True
    else :
        return False
    
def bool_word_found(unsigned_int_indicator_victory,list_char_lettre_du_mot):
    """
    fonction qui vérifie si le joueur n'a pas gagner
    """
    if unsigned_int_indicator_victory == len(list_char_lettre_du_mot):
        return True
    else:
        return False