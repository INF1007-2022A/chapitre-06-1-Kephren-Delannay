#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = [float(input("Entrer un nombre ")) for i in range(10)]
        values.sort()
    return values


def anagrams(words: list = None) -> bool:
    l1, l2 = [], []
    if words is None:
        words = [input('Veuillez entrer la chaine de caractère') for i in range(2)]
        l1, l2 = list(words[0]), list(words[1])
        l1.sort()
        l2.sort()
    return l1 == l2


def contains_doubles(items: list) -> bool:
    for item in items:
        if items.count(item) > 1:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    g = list(student_grades.values())[0]
    best = {list(student_grades.keys())[0] : g}
    best_moy = sum(g) / len(g)
    for key, val in student_grades.items():
        moy = sum(val) / len(val)
        if moy > best_moy:
            best = {key : val}
    return best


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    result = {}
    for lettre in sentence:
        if sentence.count(lettre) >= 5 and lettre.isalnum():
            result[lettre] = sentence.count(lettre)

    return {k: v for k, v in sorted(result.items(), key=lambda item:item[1], reverse=True)}


def get_recipes():
    nom = input('Donnez un nom à la recette \n')
    ingredients = input('Entrez les ingrédients de votre recette séparés par une virgule \n').split(',')
    return {nom: ingredients}

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input('Quel est le nom de votre recette ? \n')
    if nom in ingredients:
        print(ingredients[nom])
    else:
        print("Cette recette n'est pas sauvegardée !")
        print_recipe(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
