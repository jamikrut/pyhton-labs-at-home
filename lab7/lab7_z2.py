# Skrypt wyznacza ocenę, jaką otrzyma student, ze względu na ilość otrzymanych punków z kolokwium.
'''
• ocena bardzo (5,0) dobra, jeżeli student otrzymał 95 lub więcej punktów,
• jeżeli punktów jest mniej niż 95, ale więcej niż 84 ocena ponad dobra (4,5),
• ocena dobra (4,0) dla ilości punktów z przedziału [70, 84],
• jeżeli student otrzymał więcej niż 60, ale mniej niż 70 to przysługuje mu ocena dość dobra (3,5),
• ocena dostateczna od przynajmniej 60, ale powyżej 50 punktów,
• wszystkie wyniki równe 50 i mniej ocena niedostatecznej (2.0).
'''

points = int(input("Podaj ilość punktów otrzymanych z kolokwium: "))
if points > 100 or points < 0:
    print("Niepoprawny wynik z kolokwium.")
elif points >= 95:
    print("Otrzymujesz ocenę bardzo dobrą (5.0).")
elif points > 84:
    print("Otrzymujesz ocenę ponad dobrą (4.5).")
elif points >= 70:
    print("Otrzymujesz ocenę dobrą (4.0).")
elif points >= 60:
    print("Otrzymujesz ocenę dość dobrą (3.5).")
elif points > 50:
    print("Otrzymujesz ocenę dość dobrą (3.0).")
else:
    print("Otrzymujesz ocenę dość niedostateczną (2.0).")
