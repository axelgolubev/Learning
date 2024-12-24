#Skull game for 2 players
import random

print(r'''
Welcome to Skull!
  _____
 /     \
| () () |
 \  ^  /
  |||||
  |||||
      ''')

all_players = {
                'player':{'deck':['f','f','f','s'],'stack':[], 'bet':0, 'win_point':0, 'passed':0},
                'opponent1':{'deck':['f','f','f','s'],'stack':[], 'bet':0, 'win_point':0,'passed':0}
}
players_position = ['player','opponent1']
curr_player = 'player'
betting_status = False
highest_bet = 0
all_stacks = 0

open_stacks = False
openning_player = ''

#Player functions
def player_add()
    deck_p = all_players['player']['deck']
    print(f'Your deck: {deck_p }')
    card_choice = input('Choose a card to add - (f) or (s) >  ')
    add_card('player', card_choice)
    check_decks_stacks()    # Testing line

def player_bet_or_pass():
    bet_or_pass = input('Choose: to (b)et or to (a)dd. > ')
        if bet_or_pass == 'b':
            you_bet()
        elif bet_or_pass == 'p':
            all_players['player']['passed'] = 1

def you_bet():
    print('Current bet is ' + str(highest_bet))
    your_bet = int(input("What is your bet? > "))
    all_players['player']['bet'] = your_bet
    highest_bet = your_bet
    print('Current bet is ' + str(highest_bet))

# technical functions
def start_round():
    for player in all_players.keys():
        if player == 'player':
            pass
        else:
            random.shuffle(all_players[player]['deck'])
            card = all_players[player]['deck'].pop()
            all_players[player]['stack'].append(card)

def next_player():
    global curr_player
    next_player = 'opponent1' if (curr_player == 'player') else 'player'
    curr_player = next_player

def check_decks_stacks():
    '''For testing decks and stacks of all the players'''
    for player in all_players.keys():
        print('----')
        print(player)
        print(all_players[player]['deck'])
        print(all_players[player]['stack']) 
        print('----')

def all_passed():
    pass

# Opponents related functions. Could be generalized for many players, when I understand how to implement
def bet(player, increase):
        betting_status = True
        highest_bet += increase
        all_players[player]['bet'] = highest_bet

def add_card(player, card):
    if (len(all_players[player]['deck']) != 0) and (card in all_players[player]['deck']):
        all_players[player]['stack'].append(card)
        all_players[player]['deck'].remove(card)
    elif len(all_players[player]['deck']) == 0:
        print('The deck is empty')
    elif card not in all_players[player]['deck']:
        print('Player does not have this type of card')


def choose_random_card(player):
    ''' Choose a random card from a deck. The card exists in the deck. 
    
    '''
    if len(all_players[player]['deck']) != 0:
        card = random.choice(all_players[player]['deck'])
        all_players[player]['stack'].append(card)
        all_players[player]['deck'].remove(card)
    elif len(all_players[player]['deck']) == 0:
        print('The deck is empty')
    return card


def opponents_add_or_bet(player):
    '''Opponent randomly chooses either he wants to bet or add a new card on top.
       Then the logic of adding or betting starting. The bet is always a one. 
       TO DO in future: implement betting based on the number of card in all stacks, if somebody has win points
    '''
    opp_choice = random.choice(['add','bet'])
    if opp_choice == 'add':
        random_card = choose_random_card(player)
        add_card(player, random_card)
        next_player()
    elif opp_choice == 'bet':
        bet(player, 1)
        next_player()  




def opponent_bet_or_pass():
    bet_or_pass = random.choice(['b','p'])
        if bet_or_pass == 'b':
            you_bet()
        elif bet_or_pass == 'p':
            all_players['opponent1']['passed'] = 1



# Round
starting_card = input('Choose a card for a start - (f) or (s) >  ')
add_card('player', starting_card)
start_round()
check_decks_stacks()

# Main loop
while open_stacks != True:
    if curr_player == 'player':
        if betting_status == False:
            player_bet_or_add = input('Choose: to (b)et or to (a)dd. > ')
            if player_bet_or_add == 'a':
                player_add()
                next_player()
            elif player_bet_or_add == 'b':
                betting_status = True
                you_bet()
                next_player()
        elif (betting_status == True) and (highest_bet != 8):
            player_bet_or_pass() # Not implemented
            next_player()
        else:
            print('You go ALL IN!')
            highest_bet = 8
            openning_player = 'player'
            open_stacks = True
        if all_passed():
            openning_player = 'player'
            open_stacks = True

    elif curr_player == 'opponent1' :
        if betting_status == False:
            opponents_add_or_bet('opponent1')
        elif (betting_status == True) and (highest_bet != 8):
            opponent_bet_or_pass() # Not implemented
            next_player()
        else:
            print('Opponent goes ALL IN!')
            highest_bet = 8
            openning_player = 'opponent1'
            open_stacks = True
        if all_passed():
            openning_player = 'opponent1'
            open_stacks = True

# Open the stacks. If skulls - loose one card, if flower > continue, if tries == bet > get one point
# End the round. Clean all stacks, refill decks

# Main TO DOs: 1) passing is not implemented. For two people the passing is easier, then for many. 
#              2) It is probably wise to add player + opponent into one function and separate by conditional inside
#              3) Class player() with all the methods and attributeswould be better
