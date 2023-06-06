letras = "abcdefghijklmnopqrstuvxwyz"
l = ""
i = 0
numero_dig = int(input("Digite a altura da piramide: "))
fonte = input("Digite a fonte desejada: maiuscula ou minuscula: ")
if fonte == "maiuscula":
    for letra in letras:
        l += letra.upper()
        print("."*(25-i) + l)
        i += 1
        if i == numero_dig:
            break
elif fonte == "minuscula":
    for letra in letras:
        l += letra
        print("."*(25-i) + l)
        i += 1
        if i == numero_dig:
            break