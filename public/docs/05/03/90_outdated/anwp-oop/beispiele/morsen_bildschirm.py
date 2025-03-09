import sys, morsen
def schreibeCode(text, code):
    for zeichen in text:
        try:
            print(code[zeichen], end=" ")
        except KeyError:
            print(" ", end=" ")
    print()

code = morsen.leseCode()
schreibeCode("Hallo Welt", code)
