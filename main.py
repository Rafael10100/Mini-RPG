from random import randint

lista_npcs = []
hero = {
    "name": "Heroi",
    "hp": 100,
    "damage": 10,
    "exp": 0,
    "lvl": 1,
    "lvl_up": 10,
}

def criar_monstros(level):
  level = (1 * level)
  novo_npc = {
    "nome": "Monstro",
    "level": level,
    "danos": level * 5,
    "hp": level * 10,
    "exp": level,
  }
  return novo_npc

def criar_npcs(n_npcs):
  for x in range(n_npcs):
    monstro = criar_monstros(x+1)  
    lista_npcs.append(monstro)


def mostrar_npcs():
  for npc in lista_npcs:
   print(f"nome: {npc['nome']} -      level: {npc['level']} - hp:        {npc['hp']} - danos:       {npc['danos']} - exp: {npc['exp']}")


def atacar_hero(hero, monstro):
  hero["hp"] -= monstro["danos"]
  print(f"o monstro atacou {hero['name']} e tirou {monstro['danos']} de vida")
  print(f"o hero ficou com {hero['hp']} de vida")



def atacar_monstro(hero, monstro):
  monstro["hp"] -= hero["damage"]
  print(f"hero atacou {monstro['nome']} e tirou {hero['damage']} de vida")
  print(f"o monstro ficou com {monstro['hp']} de vida")
      
def ini_batalha(hero, monstro):
  while hero["hp"] > 0 and monstro["hp"] > 0:
    atacar_hero(hero, lista_npcs[0])
    atacar_monstro(hero, lista_npcs[0])

def batalha(hero, monstro):
  print("A batalha e iniciada entre o Heroi e o monstro")
  ini_batalha(hero, monstro)
  if hero["hp"] <= 0:
    print(f"{hero['name']} morreu")
  else:
    print(f"{hero['name']} ganhou a batalha")
    hero["exp"] += monstro["exp"]
    if hero["exp"] >= hero["lvl_up"]:
      hero["lvl"] += 1
      hero["hp"] = 100
      hero["damage"] += 5
      hero["lvl_up"] += 10
      print(f"{hero['name']} subiu para o level {hero['lvl']}")

criar_npcs(5)
mostrar_npcs()
batalha(hero, lista_npcs[0])
    