try:
    lord_of_the_rings = open('lor.txt', 'r', encoding='UTF-8')

    for line in lord_of_the_rings:
        print(line.rstrip(), end='\n')
        # raise ValueError
except:
    print("Exception!!!")
finally:
    print("Zamykam plik")
    lord_of_the_rings.close()
