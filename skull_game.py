#Skull game for 3 players
print(r'''
Welcome to Skull!
  _____
 /     \
| () () |
 \  ^  /
  |||||
  |||||
      ''')
player = {'deck':['f','f','f','s'],'stack':[], 'bet':0}
opponent1 = {'deck':['f','f','f','s'],'stack':[], 'bet':0}
opponent2 = {'deck':['f','f','f','s'],'stack':[], 'bet':0}

print(player['deck'])
print(player['stack'])

def add_card(player, card):
    if (len(player['deck']) != 0) and (card in player['deck']):
        player['stack'].append(card)
        player['deck'].remove(card)
    elif len(player['deck']) == 0:
        print('The deck is empty')
    elif card not in player['deck']:
        print('Player does not have this type of card')
