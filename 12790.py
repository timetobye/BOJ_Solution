def game(data):
    HP, MP, attack, defense, HP_inv, MP_inv, a_inv, d_inv = map(int, data.split())
    HP = HP + HP_inv
    MP = MP + MP_inv
    attack = attack + a_inv
    defense = defense + d_inv
    if HP < 1:
        HP = 1
    if MP < 1:
        MP = 1
    if attack < 0:
        attack = 0
    fight = 1 * HP + 5 * MP + 2 * attack + 2 * defense
    return fight

TC = int(input())
for _ in range(TC):
    data = input()
    print(game(data))