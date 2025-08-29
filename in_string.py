def check_vowels():
    texto = input("Ingrese su nombre ")
	nombre = texto.lower()
	vocala = "a" in nombre
	vocale = "e" in nombre
	vocali = "i" in nombre
	vocalo = "o" in nombre
	vocalu = "u" in nombre
	print("Contiene a:" + str(vocala))
	print("Contiene e:" + str(vocale))
	print("Contiene i:" + str(vocali))
	print("Contiene o:" + str(vocalo))
	print("Contiene u:" + str(vocalu))
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
