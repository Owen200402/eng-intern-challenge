
import sys

if __name__ == "__main__":
    translateMap = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
        "capital": ".....O",
        "decimal": ".O...O",
        "number": ".O.OOO",
        ".": "..OO.O",
        ",": "..O...",
        "?": "..O.OO",
        "!": "..OOO.",
        ":": "..OO..",
        ";": "..O.O.",
        "-": "....OO",
        "/": ".O..O.",
        "<": ".OO..O",
        ">": "O..OO.",
        "(": "O.O..O",
        ")": ".O.OO.",
        " ": "......",
    }

    args = sys.argv[1:]
    
    result = ""
    counter = 1

    for arg in args:
        numberPrev = False
        trimCounter = 0
        capitalFlag = False
        numberFlag = False
        # Braille to English
        if all(c in {'O', '.'} for c in arg):
            for i in range(0, len(arg), 6):
                ch = arg[i: i+6]
                counterNested = 1

                for key, value in translateMap.items():
                    if numberFlag == True and not key.isdigit():
                        continue
                    elif value == ch:
                        if key == "capital" and counterNested != 2:
                            capitalFlag = True
                        elif capitalFlag == True:
                            capitalFlag = False
                            result += key.capitalize()
                        elif key == "number" and counterNested != 2:
                            numberFlag = True
                        elif key == " " and counterNested != 2:
                            numberFlag = False
                            result += " "
                        elif counterNested != 2:
                            result += key
                        counterNested += 1
        # English to Braille
        else:
            for ch in arg:
                if ch.isupper():
                    result += translateMap["capital"]
                    result += translateMap[ch.lower()]
                elif ch == ".":
                    result += translateMap["decimal"]
                    result += translateMap[ch]
                elif ch.isnumeric() and numberPrev == False:
                    numberPrev = True
                    result += translateMap["number"]
                    result += translateMap[ch]
                elif ch.isnumeric() and numberPrev == True:
                    result += translateMap[ch]
                else:
                    result += translateMap[ch]
            if counter != len(args):
                result += translateMap[" "]
            counter += 1
    
    print(result)




