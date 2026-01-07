from preprocessing import clean_text

POSITIVE_CLUES = [
    "keren", "mantap", "bagus", "good job", "nice"
]

NEGATIVE_CLUES = {
    "bodoh": "insult",
    "goblok": "insult",
    "tolol": "insult",
    "jelek": "appearance_attack",
    "idiot": "insult",
}

SARCASM_CLUES = {
    # Body shaming
    "gendut banget": "body_shaming",
    "bajunya kekecilan": "body_shaming",
    "perutnya maju": "body_shaming",
    "mukanya bulat": "body_shaming",
    "pipinya kayak bakpau": "body_shaming",
    "kurus banget": "body_shaming",
    "kaya tulang berjalan": "body_shaming",
    "badan lo gede banget": "body_shaming",
    "ga muat bajunya": "body_shaming",

    # Appearance / physical mocking
    "kulitnya gosong": "appearance",
    "item banget": "appearance",
    "muka lo jelek": "appearance",
    "wajah lo serem": "appearance",
    "kayak hantu": "appearance",
    "kayak monyet": "appearance",
    "jelek banget": "appearance",
    "ga pantes dilihat": "appearance",
    "bau ketek": "appearance",

    # Gender / sexism
    "perempuan kok begitu": "gender",
    "dasar cewek murahan": "gender",
    "banci": "gender",
    "kayak cowok aja": "gender",
    "cewek tapi norak": "gender",
    "gak pantas jadi cowok": "gender",
    "cewek kok berani": "gender",

    # Religion
    "dasar kafir": "religion",
    "muslim sok suci": "religion",
    "kristen sesat": "religion",
    "agama lo aneh": "religion",
    "orang islam bodoh": "religion",

    # Race / ethnicity
    "magrib": "racial_sarcasm",
    "item banget kayak afrika": "racial_sarcasm",
    "cina pelit": "racial_sarcasm",
    "pribumi kampungan": "racial_sarcasm",
    "sunda lemes banget": "racial_sarcasm",
    "batak kasar": "racial_sarcasm",
    "padang pelit": "racial_sarcasm",

    # General insult / sarcasm
    "ketawa tapi takut dosa": "sarcasm",
    "ngakak liat muka lo": "insult",
    "otak udang": "insult",
    "bodoh banget": "insult",
    "goblok": "insult",
    "males banget liat lo": "insult",
    "sok banget": "sarcasm",
    "norak lo": "insult",
    "bikin malu aja": "insult",
    "dih siapa lo": "insult",
    "caper banget": "sarcasm",
    "lebay": "sarcasm",
    "alay": "insult",
    "najis liat lo": "insult",
    "sok cantik": "sarcasm",
    "sok ganteng": "sarcasm",
    "sok pinter": "sarcasm",
    "gak guna": "insult",
    "kampungan": "insult",
    "ngaca dulu deh": "sarcasm",
    "ketularan jelek": "insult",
    "cantik kali lo begitu": "sarcasm",
}

def apply_rules(text: str):
    cleaned = clean_text(text)

    if any(pos in cleaned for pos in POSITIVE_CLUES):
        return ("Non-bullying", "-", "positive_rule", 1.0)

    for clue, cat in NEGATIVE_CLUES.items():
        if clue in cleaned:
            return ("Bullying", cat, "negative_rule", 1.0)

    for clue, cat in SARCASM_CLUES.items():
        if clue in cleaned:
            return ("Bullying", cat, "sarcasm_rule", 1.0)

    return None
