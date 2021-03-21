#in WAR, each player draws a card from the deck, and the player from the highest card wins
#You will build War by defining classes representing a card, a deck, a player, and finally
#the game itself

#first create a CARD class with two class variables that are lists. one named SUITS and list
#all the suit types. the other called VALUES that lists all values in a card deck.
class Card:
    suits = ['Spades','Hearts','Diamonds','Clubs']

    values = ['None','None','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

#create two instance variables called SUIT and VALUE. for a 2-hearts, you would pass 2 and 1 to represent
#the indexes
    def __init__(self,v,s):
        self.suit = s
        self.value = v

#create magic methods __lt__ and __gt__ to compare two Card objects. The code should also handle
#if the card has the same value. If this occurs, methods use the value of the suits to break the tie.

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
#create magic method to pull the values of the card objects by their indexes in order to print
#"value of suits"
    def __repr__(self):
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v

#now you need to define a class to represent a deck of cards. Create a Deck class and
#a instance variable called CARDS which is an empty list. Use to 4 loops to create 52 cards
#and add them to the empty list and then shuffle the list
from random import shuffle
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,14):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
#create an rm_card method to return the card back to the deck
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

#create class called PLAYER to represent player. create instance variables for name, card player
#is currentyl holding, and number of wins
class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = None

#finally create a class to the represent the GAME. create two instance variables using input function
#to represent the players. Create Deck() object and store in DECK instance variable, Create Player() objects
#and pass the instance variables
class Game:
    def __init__(self):
        name1 = input("Player 1 name")
        name2 = input("Player 2 name")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
#create method that displays the name of the winner of the round called WINS
    def wins(self,winner):
        w = '{} wins this round'
        w = w.format(winner)
        print(w)
#create method called DRAW that prints the players' name and the card they drew
    def draw(self,p1n,p1c,p2n,p2c):
        d = '{} drew {} {} drew {}'
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

#create method play_game to start the game. create loop that keeps going as long as there are two
#or more cards left in the deck and an input called RESPONSE to quit the game. pull two cards for each
#and assign their name. call the draw() method to print the card and names. compare the cards,increment
#the win count, call the wins() method to print the winner
    def play_game(self):
        cards = self.deck.cards
        print('beginning War!')
        while len(cards) >= 2:
            m = 'q to quit. Press any ' + 'key to play:'
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
#create instance variable WIN to use for printing winner after all cards are dealt using the winner()
#method you need to create
        win = self.winner(self.p1,self.p2)

        print('War is over. {} wins'.format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'It was a tie!'

game = Game()
game.play_game()
