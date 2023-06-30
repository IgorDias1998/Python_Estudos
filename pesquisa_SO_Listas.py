opcoes = [
    "linux",
    "windows",
    "unix",
    "mac_os",
    "outros"
]

votos = [0] * len(opcoes)

print("Sistema Operacional:")
print("Linux(0) - Windows(1) - Unix(2) - Mac_os(3) - Outros(4)\n")
while True:
    voto = int(input("Informe o voto (0 a 4, *8 para encerrar*): "))
    if voto == 8:
        break
    if voto < 0 or voto > 4:
        print("Valor inválido. Tente novamente.")
        continue
    votos[voto] += 1

i = 0
print("Sistema Operacional   Votos")
print("-------------------   -----")
for i in range(len(opcoes)):
    print(f"{opcoes[i]:<24}{votos[i]:<7}")


indice_vencedor = votos.index(max(votos))
print("Com mais votos o vencedor foi: {}".format(opcoes[indice_vencedor]))