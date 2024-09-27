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

print(f"La primera letra de la frase es  {phrase[0]} y la ultima es {phrase[-1]}")

# 4 Mostrar palabras en Orden reverso

print(f"Las palabras al reverso serian {phrase.split()[::-1]}")

# 5 Verificar que la palabra 'Python' aparezca 
if("python" in phrase.lower()) :
  print(f"La palabra Python aparece en la frase")
else :
  print(f"La palabra Python no aparece en la frase")