#!/usr/bin/env python3

import random
import sys


class Data:
  AGRICULTURE = ['Agriculture', 'Agriculture']
  ARISTOTE = ['Aristote', 'Aristotle']
  BILKIS = ['Bilkis', 'Bilkis']
  BLEU = ['Bleu', 'Blue']
  CESAR = ['César', 'Ceasar']
  CINQ_POINTS = ['5 points', '5 points']
  CLEOPATRE = ['Cléopâtre', 'Cleopatra']
  DROITE_A_GAUCHE = ['Droige à gauche ==>', 'Right to left ==>']
  ECONOMIE = ['Economie', 'Economy']
  GAUCHE_A_DROITE = ['Gauche à droite ==>', 'Left to right ==>']
  GRIS = ['Gris', 'Grey']
  HAMMURABI = ['Hammurabi', 'Hammurabi']
  JAUNE = ['Jaune', 'Yellow']
  LOI = ['Loi', 'Law']
  MARRON = ['Marron', 'Maroon']
  MATHEMATIQUES = ['Mathématiques', 'Mathematics']
  NOUVELLE_PARTIE = ['Nouvelle partie !', 'New Game!']
  PHILOSOPHIE = ['Philosophie', 'Philosophy'] 
  REJOUER = ['Rejouer !', 'Replay!']
  ROND = ['Rond', 'Round']
  ROUGE = ['Rouge', 'Red']
  STRATEGIE = ['Stratégie', 'Strategy']
  TRIANGLE = ['Triangle', 'Triangle']
  VERT = ['Vert', 'Green']
  VIOLET = ['Violet', 'Purple']

class Base:
  def __init__(self, idx):
    self.data = Data()
    self.idx = idx

  def __getattr__(self, key):
    entry = getattr(self.data, key)
    return entry[self.idx]

Francais = Base(0)
English = Base(1)

#default language
String = Francais

if len(sys.argv) > 1:
  arg = sys.argv[1].upper()
  if arg[0] == 'E':
    String = English
  if arg[0] == 'F':
    String = Francais

class Leader:
    def __init__(self, name_, colour_, symbols_, progres_):
        self.name = name_
        self.colour = colour_
        self.symbols = symbols_
        self.progres = progres_
    def print_self(self):
        print(self.name)
        print(', '.join(self.progres))

hammurabi = Leader(String.HAMMURABI, String.JAUNE, String.ROND, [String.ECONOMIE, String.CINQ_POINTS])
cleopatre = Leader(String.CLEOPATRE, String.BLEU, [String.TRIANGLE], [String.PHILOSOPHIE, String.AGRICULTURE])
cesar = Leader(String.CESAR, String.VIOLET, [], [String.STRATEGIE])
aristote = Leader(String.ARISTOTE, String.GRIS, [String.ROND], [String.PHILOSOPHIE, String.MATHEMATIQUES])
bilkis = Leader(String.BILKIS, String.MARRON, [String.ROND, String.TRIANGLE], [String.ECONOMIE])

all_leaders = [hammurabi, cleopatre, cesar, aristote, bilkis]

def randl():
    return random.choice(all_leaders)

class Decision:
    def __init__(self, arrow_, c1_, c2_, c3_, symbol_):
        self.arrow = arrow_
        self.c1 = c1_
        self.c2 = c2_
        self.c3 = c3_
        self.symbol = symbol_
    def print_self(self, leader):
        c1 = self.c1 if self.c1 else leader.colour
        c2 = self.c2 if self.c2 else leader.colour
        c3 = self.c3 if self.c3 else leader.colour
        print("{}".format(self.arrow))
        print("{} {} {}".format(c1, c2, c3))
        if self.symbol in leader.symbols:
            print(String.REJOUER)

all_decisions = [
    Decision(String.GAUCHE_A_DROITE, String.VERT, String.ROUGE, None, None),
    Decision(String.GAUCHE_A_DROITE, String.VERT, String.ROUGE, None, None),
    Decision(String.GAUCHE_A_DROITE, String.VERT, String.ROUGE, None, None),
    Decision(String.GAUCHE_A_DROITE, String.ROUGE, String.VERT, None, None),
    Decision(String.GAUCHE_A_DROITE, String.ROUGE, String.VERT, None, None),
    Decision(String.GAUCHE_A_DROITE, None, String.ROUGE, String.VERT, String.TRIANGLE),
    Decision(String.DROITE_A_GAUCHE, String.VERT, String.ROUGE, None, None),
    Decision(String.DROITE_A_GAUCHE, String.ROUGE, String.VERT, None, None),
    Decision(String.DROITE_A_GAUCHE, String.ROUGE, String.VERT, None, None),
    Decision(String.DROITE_A_GAUCHE, String.ROUGE, String.VERT, None, None),
    Decision(String.DROITE_A_GAUCHE, String.VERT, String.ROUGE, None, None),
    Decision(String.DROITE_A_GAUCHE, None, String.VERT, String.ROUGE, String.ROND)
    ]

class Game:
    def __init__(self):
        self.leader = random.choice(all_leaders)
        self.decision_pile = [d for d in all_decisions]
        random.shuffle(self.decision_pile)
    def set_leader(self, name):
        name = name.lower()
        if name[0] == 'h':
            self.leader = hammurabi
        elif name[0:2] == 'cl':
            self.leader = cleopatre
        elif name[0:2] == 'ce':
            self.leader = cesar
        elif name[0] == 'a':
            self.leader = aristote
        elif name[0] == 'b':
            self.leader = bilkis
    def next_decision(self):
        if not self.decision_pile:
            self.decision_pile = [d for d in all_decisions]
            random.shuffle(self.decision_pile)
        return self.decision_pile.pop()

def main():
    print('7 WONDERS DUEL SOLO')
    print(String.NOUVELLE_PARTIE)
    print()
    g = Game()
    if len(sys.argv) > 1:
        g.set_leader(sys.argv[1])
    g.leader.print_self()
    while True:
        line = input('').lower()
        if len(line.split()) == 0:
            d = g.next_decision()
            d.print_self(g.leader)
        elif line[0] == 'q':
            exit()
        else:
            print(String.NOUVELLE_PARTIE)
            print()
            g = Game()
            g.set_leader(line)
            g.leader.print_self()

if __name__=='__main__':
    main()
