#créé en 12 septembre 2023
#créé par Kevin Wen
#c'est le code de TP1


def word_count(): # creer la fonction de word count
    sentence = str(input('entrer une phrase pour savoir le nombre de mots: ')) # permettre que l'utilisateur entre son phrase

    numberWords = len(sentence.split(" ")) # separer les espaces pour compter le nombre de mots

    return numberWords # effectuer la fonction

reply = f'la phrase contient {word_count()} mots.' # creer la phrase pour montrer le nombre de mots

print(reply) # imprimer la phrase
