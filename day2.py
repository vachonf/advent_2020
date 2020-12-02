
import pandas as pd

def day2():
    # lire fichier
    data = pd.read_csv("/Users/francoisvachon/Desktop/day2.csv", sep=" ", header=None)
    # creer les columns
    data.columns = ["temp_range", "lettre_choisi", "mot_de_passe"]
    # parser le min max
    data[["min", "max"]] = data["temp_range"].str.split("-", expand=True).apply(pd.to_numeric)
    # enlever le ":"
    data["lettre_choisi"] = data["lettre_choisi"].str.replace(":", "")

    question1 = 0
    question2 = 0
    for i, row in data.iterrows():
        mot = row["mot_de_passe"]
        min = row["min"]
        max = row["max"]
        lettre = row["lettre_choisi"]

        lettercount = mot.count(lettre)
        if min <= lettercount <= max:
            question1 += 1

        is_pos1 = (mot[min - 1] == lettre)
        is_pos2 = (mot[max - 1] == lettre)
        question2 += ((is_pos1 + is_pos2) == 1)

    print ("reponse question 1: " + str(question1))
    print ("reponse question 2: " + str(question2))

if __name__ == '__main__':
    day2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
