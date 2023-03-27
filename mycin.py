# Création d'une base de règles de production
regles = [
    {"si": ["fièvre", "toux", "mal de gorge"], "alors": "infection respiratoire"},
    {"si": ["fièvre", "maux de tête", "vomissements"], "alors": "méningite"},
    {"si": ["douleur abdominale", "nausées", "vomissements"], "alors": "gastro-entérite"},
    {"si": ["douleur thoracique", "essoufflement", "fatigue"], "alors": "insuffisance cardiaque"},
    {"si": ["douleur à la poitrine", "essoufflement", "toux", "fièvre"], "alors": "pneumonie"},
    {"si": ["douleur au bas du dos", "fièvre", "nausées", "vomissements"], "alors": "infection urinaire"},
    {"si": ["fatigue", "perte de poids", "soif excessive"], "alors": "diabète"},
    {"si": ["douleur abdominale", "constipation", "diarrhée", "flatulences"], "alors": "syndrome du côlon irritable"}
]

# Fonction pour poser une question à l'utilisateur et retourner sa réponse
def poser_question(symptome):
    reponse = input("Avez-vous {} ? (oui/non) ".format(symptome))
    return reponse.lower() == "oui"

# Fonction pour appliquer les règles de production et retourner le diagnostic
def diagnostiquer(symptomes):
    for regle in regles:
        si_vrai = True
        for symptome in regle["si"]:
            if symptome not in symptomes:
                si_vrai = False
                break
        if si_vrai:
            return regle["alors"]
    return "Maladie inconnue"

# Demander à l'utilisateur les symptômes et diagnostiquer
symptomes = []
symptomes.append(poser_question("fièvre"))
symptomes.append(poser_question("toux"))
symptomes.append(poser_question("mal de gorge"))
symptomes.append(poser_question("maux de tête"))
symptomes.append(poser_question("vomissements"))
symptomes.append(poser_question("douleur abdominale"))
symptomes.append(poser_question("nausées"))
symptomes.append(poser_question("douleur thoracique"))
symptomes.append(poser_question("essoufflement"))
symptomes.append(poser_question("fatigue"))
symptomes.append(poser_question("douleur à la poitrine"))
symptomes.append(poser_question("constipation"))
symptomes.append(poser_question("diarrhée"))
symptomes.append(poser_question("flatulences"))
symptomes.append(poser_question("perte de poids"))
symptomes.append(poser_question("soif excessive"))

diagnostic = diagnostiquer(symptomes)
print("Diagnostic : {}".format(diagnostic))
