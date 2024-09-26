phrase = input("Escriba la frase a analizar: ")
letters = input("Escriba 3 Letras a analizar, separandolas por espacios: ")

split_letters = letters.split()

print(f"Letras a analizar:  {split_letters}")

# 1 cuantas veces aparecen las letras ingresadas en el texto 
first_letter = phrase.lower().count(split_letters[0])
second_letter = phrase.lower().count(split_letters[1])
third_letter = phrase.lower().count(split_letters[2])

print(f"La letra {split_letters[0]} aparece {first_letter} veces en la frase ingresada")
print(f"La letra {split_letters[1]} aparece {second_letter} veces en la frase ingresada")
print(f"La letra {split_letters[2]} aparece {third_letter} veces en la frase ingresada")

# 2 Cuantas palabras hay en total en la frase

total_words = len(phrase.split())

print(f"Hay { total_words } palabras en la frase")

# 3 Mostrar primera y ultima letra de la frase

# 4 Mostrar palabras en Orden reverso

# 5 Verificar que la palabra 'Python' aparezca  