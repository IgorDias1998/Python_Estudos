secreto = 'programador'
digitados = []
chances = 3

while True:
      if chances <= 0:
          print('VOCE PERDEU')
          break

      letra = input('Digite uma letra: ')

      if len(letra) > 1:
          print('Digite apenas uma letra')
          continue

      digitados.append(letra)

      if letra in secreto:
          print(f'BOA, a letra {letra} esta na palavra secreta.')
      else:
          print(f'A letra {letra} não está na palavra, vixiii')
          digitados.pop()

      secreto_temporario = ''
      for letra_secreta in secreto:
          if letra_secreta in digitados:
              secreto_temporario += letra_secreta
          else:
              secreto_temporario += '*'

      if secreto_temporario == secreto:
          print(f'BOA você ganhou, a palavra secreta é {secreto_temporario}')
          break
      else:
          print(f'A palavra secreta está assim, {secreto_temporario}')

      if letra not in secreto:
          chances -= 1

      print(f'Você ainda tem {chances} chances.')
      print()
