"""
author : Jean TROUSSIER
date : jeudi 3 octobre
obj :  fichier fonction du pendu textuelle
to do :
"""

import random as rd
unsigned_int_live = 0
list_char_lettre_du_mot = []
list_char_lettre_joueur = []
list_char_lettre_joueur_fausse = []
unsigned_int_indicator_victory = 0

def void_afficher_mot():
    """
    fonction qui n'a aucune entré et qui affiche les lettres trouvés et cache celle qui ne l'ont pas été encore
    """
    global unsigned_int_indicator_victory 
    unsigned_int_indicator_victory = 0
    for char_lettre in list_char_lettre_du_mot:
        if char_lettre in list_char_lettre_joueur:
            print(char_lettre, end='')
            unsigned_int_indicator_victory += 1
        else:
            print("_", end='')
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
    return string_word_to_guess

def list_char_word_seperator(string_word):
    """
    input : string_word
    fonction qui transforme une string en liste de char
    """
    for char_buffer in string_word:
        list_char_lettre_du_mot.append(char_buffer)
    
def list_char_letter_starter(string_word_to_guess):
    """
    input : string_word_to_guess
    fonction qui met choisie "aléatoirement" une lettre et l'ajoute dans la liste du joueur
    """
    unsigned_int_index = rd.randint(1,len(string_word_to_guess)) - 1
    list_char_lettre_joueur.append(string_word_to_guess[unsigned_int_index])

def bool_death_tester():
    """
    fonction qui vérifie que le joueur n'a pas perdu
    """
    if unsigned_int_live == 8:
        return True
    else :
        return False
    
def bool_word_found():
    """
    fonction qui vérifie si le joueur n'a pas gagner
    """
    if unsigned_int_indicator_victory == len(list_char_lettre_du_mot):
        return True
    else:
        return False