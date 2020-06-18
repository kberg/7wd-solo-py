#!/usr/bin/env python3

import random
import sys

class Leader:
    def __init__(self, name_, colour_, symbols_, progres_):
        self.name = name_
        self.colour = colour_
        self.symbols = symbols_
        self.progres = progres_
    def print_self(self):
        print(self.name)
        print(self.progres)

hammurabi = Leader('Hammurabi', 'Jaune', ['Rond'], 'Economie, 5 points')
cleopatre = Leader('Cléopâtre', 'Bleu', ['Triangle'], 'Philosophie, Agriculture')
cesar = Leader('César', 'Violet', [], 'Stratégie')
aristote = Leader('Aristote', 'Gris', ['Rond'], 'Philosophie, Mathématiques')
bilkis = Leader('Bilkis', 'Marron', ['Rond', 'Triangle'], 'Economie')

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
            print('Rejouer !')

all_decisions = [
    Decision('Gauche à droite ==>', 'Vert', 'Rouge', None, None), Decision('Gauche à droite ==>', 'Vert', 'Rouge', None, None), Decision('Gauche à droite ==>', 'Vert', 'Rouge', None, None),
    Decision('Gauche à droite ==>', 'Rouge', 'Vert', None, None), Decision('Gauche à droite ==>', 'Rouge', 'Vert', None, None), Decision('Gauche à droite ==>', None, 'Rouge', 'Vert', 'Triangle'),
    Decision('<== Droite à gauche', 'Vert', 'Rouge', None, None), Decision('<== Droite à gauche', 'Rouge', 'Vert', None, None), Decision('<== Droite à gauche', 'Rouge', 'Vert', None, None),
    Decision('<== Droite à gauche', 'Rouge', 'Vert', None, None), Decision('<== Droite à gauche', 'Vert', 'Rouge', None, None), Decision('<== Droite à gauche', None, 'Vert', 'Rouge', 'Rond')
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
    print('Nouvelle partie !')
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
            print('Nouvelle partie !')
            print()
            g = Game()
            g.set_leader(line)
            g.leader.print_self()

if __name__=='__main__':
    main()
