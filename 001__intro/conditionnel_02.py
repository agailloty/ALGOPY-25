# Conditionnel

# Python offre un mécanisme pour exécuter un bloc de code uniquement si certaines
# conditions sont respectées. 

prenom = input("Entrez votre prénom : ")
# Opérateurs de comparaison : == (égal), != (différent), < (inférieur à), <= (inférieur ou égal à)
# > (supérieur à), >= (supérieur ou égal à)

print(len(prenom))
print(len(prenom.strip()))

if prenom.strip() != "":
    print("Bonjour, ", prenom.strip())
else:
    print("Vous n'avez rien saisi")