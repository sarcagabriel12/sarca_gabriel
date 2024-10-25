articol = " Altstadt, centrul istoric al orașului, este împachetat într-o zonă de mai puțin de 500 de metri pătrați - cele 300 de baruri și restaurante ale sale sunt amplasate atât de strâns, încât centrul a fost supranumit „cel mai lung bar din lume”. Străzile sale pietruite duc spre vest către cel mai vechi parc public din Germania, Hofgarten, iar spre est către cel mai lung râu al orașului"
lungine_articol = len(articol)
jumatate_articol = lungine_articol // 2
print(jumatate_articol)

# 1.Impartirea sirului
prima_parte = articol[:jumatate_articol]
print(prima_parte)
parte_secunda = articol[jumatate_articol:]
print(parte_secunda)

# 2.Prima parte a articolului
prima_parte_upper = prima_parte.upper()
print(prima_parte_upper)
prima_parte_strip = prima_parte_upper.strip()
print(prima_parte_strip)

# 3.A doua parte a articolului
parte_secunda_revers = parte_secunda[::-1]
print(parte_secunda_revers)
parte_secunda_cap = parte_secunda_revers.capitalize()
print(parte_secunda_cap)
parte_secunda_remove = parte_secunda_cap.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
print(parte_secunda_remove)

# 4.Rezultatul
rezultat = prima_parte_strip + parte_secunda_remove
print(rezultat)