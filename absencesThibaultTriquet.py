import datetime
import csv

RADIUS = "radius.log"
LOGIN_FILE = "login_1a_2015"

# Création du fichier csv
c = csv.writer(open("Absence.csv", "w"))

# Initilisation des dictionnaires

presence = {}
statistics = {}

# Il ouvre le fichier Login
for login in open(LOGIN_FILE, "r"):

    # Définition du compteur du nombre d'absence dans le dictionnaire
    # Le .strip permet de retirer le \n des noms et prénoms
    statistics[login.strip()] = 0

for line in open(RADIUS):
    # Sépare les dates et les noms des personnes se connectant au réseau
    if 'Auth: Login OK:' in line:
        res = line.split(' : ')

        # Conversion en chaîne de caractère
        dat = datetime.datetime.strptime(res[0], "%a %b %d %H:%M:%S %Y")
        # Conversion en structure de datetime
        day = dat.strftime("%d-%m-%Y")

        # Les étudiants ne travaillent pas le weekend
        if dat.strftime('%a') == "Sat" or dat.strftime('%a') == "Sun":
            continue
        # Le 11 Novembre est un jour férié
        if dat.strftime('%b') == "Nov" and dat.strftime('%d') == "11":
            continue
        # Comptage en absence
        if day not in presence:
            presence[day] = []

        # Lecture du fichier radius
        login = line[line.find("[") + 1:line.find("]")]
        if login not in presence[day] and login in statistics:
            presence[day].append(login)

# Compteur pour savoir qui est le plus absent
mostAbsent = 0
mustAbsent = 0

# Comptage Abscence des élèves
for day in presence:
    for student in statistics:
        if student not in presence[day]:
            print('Student %s was absent on %s' % (student, day))
            statistics[student] += 1
            if statistics[student] > mostAbsent:
                mostAbsent = statistics[student]
                mustAbsent = student

# Sortie du nombre d'absence des élèves
for login in sorted(statistics):
    print("%s => %d" % (login, statistics[login]))
    c.writerow((login, statistics[login]))

print("L'étudiant ayant le plus d'absence est", mustAbsent, "il a", mostAbsent, "absences !")










