# import urllib.request

# url = "http://www.crhallberg.com/cah/"
# response = urllib.request.urlopen(url)
# data = response.read().decode('json')

# print(data)
import json
import pprint
import random


whiteDeck = set()
blackDeck = set()
stage = []

file = open('cards.json', 'r')

cards = json.load(file)

players = []

class Player:
	def __init__(self):
		self.hand = []
		self.black = []


numPlayers = int(input("How many players? "))



def rdrawBlackCard(num):
	if (num not in blackDeck):
		if cards['blackCards'][num]['pick'] != 0:
			blackDeck.add(num)
		return cards['blackCards'][num]
	rdrawBlackCard((num + 1)%len(cards['blackCards']))

def drawBlackCard():
	randPos = random.randint(0,len(cards['blackCards']))
	return rdrawBlackCard(randPos)

def rdrawWhiteCard(num):
	if (num not in whiteDeck):
		whiteDeck.add(num)
		return cards['whiteCards'][num]
	rdrawWhiteCard((num + 1)%len(cards['whiteCards']))

def drawWhiteCard():
	randPos = random.randint(0,len(cards['whiteCards']))
	return rdrawWhiteCard(randPos)

def refillHand(hand):
	#O(n)
	for i in range(5):
		if hand[i] == " ":
			hand[i] = drawWhiteCard()

def judgePicks(stage):
	print("Judge!!")
	stageLine = ""
	for i in range(len(stage)):
		stageLine += stage[i][0] + ' '*4
	print(stageLine)
	pick = int(input("Judge, pick the best! ")) - 1

	pick = stage[pick]
	return pick
def setUp():
	for i in range(numPlayers):
		player = Player()
		for x in range(5):
			card = drawWhiteCard()
			player.hand.append(card)
		players.append(player)
		print(card)

def playGame():
	setUp()
	thrown = []
	judge = len(players) - 1
	highScore = 0

	while (highScore < 5):
		blackCard = drawBlackCard()
		for i in range(len(players)):
			if (i != judge):			
				#print("Player " )
				print("Player ", i + 1, " "*4, "score:", len(players[i].black))
				printHand = " "
				printHand.join(players[i].hand)
				print(printHand)
				print(players[i].hand)
				pick = int(input("Pick the best! [1-5] ")) - 1
				stage.append((players[i].hand[pick],i))
				players[i].hand[pick] = " "
				refillHand(players[i].hand)

		winningCard = judgePicks(stage)
		players[winningCard[1]].black.append(winningCard[0])
		if highScore < len(players[winningCard[1]].black):
			highScore = len(players[winningCard[1]].black)
			if highScore == 5:
				print("Player " + str(winningCard[i] + 1) + " wins!!!")
		judge+= 1
		judge = judge % len(players)

playGame()







#pprint.pprint(json_string)


# def playGame():

# 	while (highScore < 7 or playedQuestions == )

