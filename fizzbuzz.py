def fizzbuzz(n):
    result = ""
    
    # Vérifier si le nombre est divisible par 3 ou contient un 3
    if n % 3 == 0 or '3' in str(n):
        result += "Fizz"
    
    # Vérifier si le nombre est divisible par 5 ou contient un 5
    if n % 5 == 0 or '5' in str(n):
        result += "Buzz"
    
    # Si le résultat est vide, afficher simplement le nombre
    if result == "":
        return str(n)
    return result

# Parcourir les nombres de 1 à 100
for i in range(1, 101):
    print(fizzbuzz(i))
