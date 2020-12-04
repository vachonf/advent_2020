
def day4buildData(file):

    ff = open(file)
    data = [line.strip() for line in ff]
    ff.close()

    cleaned_data = {}
    full_cleaned_data = []
    for line in data:
        if not line.strip(): #changement de data set, c'est une ligne vide
            full_cleaned_data.append(cleaned_data) #ajouter dans la liste
            cleaned_data = {}
            continue
        elements = line.split() #separer les elements
        set = dict(i.split(":") for i in elements) #convertir en dict
        cleaned_data.update(set) #ajouter et passer a l'autre ligne

    if cleaned_data: #ajouter le dernier
        full_cleaned_data.append(cleaned_data)  # ajouter dans la liste

    return full_cleaned_data


def validerYeux(yeux):
    if not yeux.startswith("#") or len(yeux) != 7:
        return False
    try:
        test = int(yeux[1:], 16)
    except ValueError:
        return False
    else:
        return True


def part2isValid(passport):

    if int(passport["byr"]) not in range(1920, 2003):
        return False

    if int(passport["iyr"]) not in range(2010, 2021):
        return False

    if int(passport["eyr"]) not in range(2020, 2031):
        return False

    if passport["hgt"].endswith("cm"):
        if int(passport["hgt"][:-2]) not in range(150, 194):
            return False
    if passport["hgt"].endswith("in"):
        if int(passport["hgt"][:-2]) not in range(59, 77):
            return False
    if not (passport["hgt"].endswith("in") or passport["hgt"].endswith("cm")):
        return False

    if not validerYeux(passport["hcl"]):
        return False

    if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    if not (len(passport["pid"]) == 9 and passport["pid"].isdigit()):
        return False

    return True


if __name__ == '__main__':
    data = day4buildData("/Users/francoisvachon/Desktop/day4.txt")

    champs_obligatoires = {"byr","pid","eyr","hgt","hcl","ecl","iyr"}

    num_valide = 0
    for passport in data:
        if set(passport).issuperset(champs_obligatoires):
            num_valide+=1

    print("Rep 1 = " + str(num_valide))

    num_valide = 0
    for passport in data:
        if set(passport).issuperset(champs_obligatoires) and part2isValid(passport):
            num_valide+=1

    print("Rep 2 = " + str(num_valide))