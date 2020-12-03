
def day3():
    ff = open("/Users/francoisvachon/Desktop/day3.csv", 'r+')
    data = ff.readlines()
    ff.close()

    num_arbre = 0
    step_droite = 3
    for i in range(1, len(data)):
        if data[i][step_droite] == "#":
            num_arbre += 1  # un arbre
        step_droite += 3  # on bouge a droite
        if step_droite >= len(data[i].strip()):
            step_droite = step_droite - len(data[i].strip())

    print("rep 1:" + str(num_arbre))

    # part2, meme chose qu'en haut, mais faire une loop. une fonction serait plus beau
    angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multiplicateur_part2 = 1

    for angle in angles:
        num_arbre = 0
        step_droite = angle[0]
        step_bas = angle[1]
        posx = step_droite
        for i in range(step_bas, len(data), step_bas):
            if data[i][posx] == "#":
                num_arbre += 1  # un arbre
            posx += step_droite  # on bouge a droite
            if posx >= len(data[i].strip()):
                posx = posx - len(data[i].strip())

        multiplicateur_part2 *= num_arbre

    print("rep 2:" + str(multiplicateur_part2))


if __name__ == '__main__':
    day3()
