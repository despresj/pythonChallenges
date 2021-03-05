
def order(sentence):
    ind = [x for x in sentence if x.isdigit()]
    sentence = sentence.split(" ")
    my_dict = {key: x for key,x in zip(ind, sentence)} 
    output = []
    for i in sorted(my_dict.keys()):
        output.append(my_dict[i])
    return ' '.join(output)


sentence = "is2 Thi1s T4est 3a"
sentence = "4of Fo1r pe6ople g3ood th5e the2"
order(sentence)


def decodeMorse(morse_code):
    code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',
            
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.',  ' ': '_'
            }
    morse = {letter: x for (x, letter) in code.items()}

    morseIn = morse_code
    morseIn = morseIn.replace(" ", "!")
    morseIn = morseIn.replace("!!!", "!_!")

    morseIn = morseIn.split("!")

    morseOut = []
    for item in morseIn:
        morseOut.append(morse[item])
    return ''.join(morseOut) 
decodeMorse('... --- ...')
