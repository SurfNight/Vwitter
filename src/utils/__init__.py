number_map = {
    "dois" : 2,
    "tres" : 3,
    "quatro" : 4,
    "cinco" : 5,
    "seis" : 6,
    "sete" : 7,
    "oito" : 8,
    "nove" : 9,
    "dez" : 10,
    "onze" : 11,
    "doze" : 12,
    "treze" : 13,
    "quatorze" : 14,
    "quinze" : 15,
    "dezesseis" : 16,
    "dezessete" : 17,
    "dezoito" : 18,
    "dezenove" : 19,
    "vinte" : 20,
    "trinta" : 30
}

def words_to_numbers(text):
    """
    Converts words to numbers.
    """
    number_found = 3
    for word, number in number_map.items():
        if word in text or str(number) in text:
            text = text.replace(word, str(number))
            number_found = number
            break
    return [text, number_found]
