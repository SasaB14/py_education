import random


suits = ('Srce', 'Karo', 'Pik', 'Tref')
ranks = ('Dvojka', 'Trojka', 'Cetvorka', 'Petica', 'Sestica', 'Sedmica', 'Osmica', 'Devetka', 'Desetka', 'Zandar', 'Kraljica', 'Kralj', 'As')
values = {'Dvojka':2, 'Trojka':3, 'Cetvorka':4, 'Petica':5, 'Sestica':6, 'Sedmica':7, 'Osmica':8, 'Devetka':9, 'Desetka':10, 'Zandar':10,'Kraljica':10, 'Kralj':10, 'As':11}

playing = True

class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0

    def __str__(self):
    	ruka=''
    	for card in self.cards:
    		ruka += card.suit+' '+card.rank+' * '
    	return ruka
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
        	self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces>0:
        	self.value -=10
        	self.aces -=1
'''
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print('$$$')
print(test_player)
print('$$$')
print(test_player.value)
'''
class Chips:
    
    def __init__(self):
        self.total = 200
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("koliko cipova ulazete: "))
		except:
			print("niste uneli ceo broj")
			continue
		else:
			if chips.bet > chips.total:
				print("Zao nam je vas ulog ne moze da bude veci od",chips.total)
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Zelite li novu kartu ili ostajete? unesite 'k' or 'o' ")
        
        if x[0].lower() == 'k':
            hit(deck,hand) 

        elif x[0].lower() == 'o':
            print("Igrac staje. delilac igra.")
            playing = False

        else:
            print("Pokusajte ponovo.")
            continue
        break

def show_some(player,dealer):
	CRED = '\033[91m'
	CGREEN  = '\33[32m'
	CEND = '\033[0m'
	print(CRED + "\nRuka delioca:" + CEND)
	print("<sakrivena karta>")
	print('',dealer.cards[1])
	print(CGREEN+"\nRuka igraca:", *player.cards, sep='\n '+CEND)
	print("Ruka igraca =",player.value)

def show_all(player,dealer):
	CGREEN  = '\33[32m'
	CRED = '\033[91m'
	CEND = '\033[0m'
	print(CRED+"\nRuka delioca:", *dealer.cards, sep='\n '+CEND)
	print("Ruka delioca =",dealer.value)
	print(CGREEN+"\nRuka igraca:", *player.cards, sep='\n '+CEND)
	print("Ruka igraca =",player.value)



def player_busts(player,dealer,chips):
    print("Igrac gubi!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Igrac dobija!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Delilac gubi!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Delilac dobija!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Izjednaceno! push!")

while True:
  
    print('BlackJack! Priblizite se 21 i pazite da ne predjete!\nDelilac gadja do 17. Asovi se racunaju kao 1 ili 11.')
    
    # kreiraj spil i promesaj ga.
    deck = Deck()
    deck.shuffle()
    
    #dodaj dve karte igracu
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    #dodaj dve karte deliocu
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Cipovi za igraca
    player_chips = Chips()      
    
    # Upitaj igraca za opkladu
    take_bet(player_chips)
    
    # prikazi karte, prva karta kod delioca sakrivena
    show_some(player_hand,dealer_hand)
    
    while playing:  # pozovi vrednost ove promenljive iz hit_or_stand funkcije
        
        # pitaj igraca
        hit_or_stand(deck,player_hand) 
        
        # prikazi karte, prva karta kod delioca sakrivena
        show_some(player_hand,dealer_hand)  
        
        # ako igraceva ruka predje 21, pokreni player_busts() i izadji iz petlje
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # ako nije presao 21, delilac igra dok ne dodje do 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # prikazi sve karte
        show_all(player_hand,dealer_hand)
        
        # koji od scenarija za pobedu vazi
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # prikazi koliko cipova ima igrac 
    print("\nIgrac ima cipova: ",player_chips.total)
    
    # Ask to play again
    new_game = input("Zelite li jos jednu ruku? unesite 'd' ili 'n' ")
    
    if new_game[0].lower()=='d':
        playing=True
        continue
    else:
        print("Hvala sto ste igrali!")
        break