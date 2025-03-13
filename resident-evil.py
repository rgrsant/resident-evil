player = str(input("Nome do jogador:"))

print("Sobreviva fazendo as escolhas certas!")
print("Primeira rodada")
print(player, ", escolha uma porta: 1, 2 ou 3?")
p1p = str(input())

if(p1p=="1"):
  print("Você sobreviveu a primeira rodada!")
  print("Segunda rodada")
  print(player, ", escolha uma porta: 1, 2 ou 3?")
  p1p = str(input())

  if(p1p=="1"):
    print("Você sobreviveu a segunda rodada!")
    print("Terceira rodada")
    print(player, ", escolha uma porta: 2 ou 3?")
    p1p = str(input())

    if(p1p=="2") or (p1p=="3"):
      print("Você escolheu uma porta que tinha zumbi.")
      print("Game Over!")

    else:
      print("Jogada inválida.")

  elif(p1p=="2"):
    print("Você sobreviveu a segunda rodada!")
    print("Terceira rodada")
    print(player, ", escolha uma porta: 1, 2 ou 3?")
    p1p = str(input())

    if(p1p=="1"):
      print("Você sobreviveu a terceira rodada!")
      print("Parabéns, você venceu!")
    
    elif(p1p=="2") or (p1p=="3"):
      print("Você escolheu uma porta que tinha zumbi.")
      print("Game Over!")

    else:
      print("Jogada inválida.")
  
  elif(p1p=="3"):
    print("Você escolheu uma porta que tinha zumbi.")
    print("Game Over!")

  else:
    print("Jogada inválida.") 

elif(p1p=="2") or (p1p=="3"):
  print("Você escolheu uma porta que tinha zumbi.")
  print("Game Over!")

else:
  print("Jogada inválida.")

     