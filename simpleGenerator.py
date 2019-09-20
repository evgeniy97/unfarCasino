import numpy as np

# Как правильно задавать начальное распределение?

class Croupier():
    def __init__(self):
        self.states = ['F','U'] # F for Fair state, U for Unfair state
        self.transitionsProbability = {
            'F': [0.95,0.05], # to F, to U
            'U': [0.1,0.9] # to F, to U
        }
        
        self.startProbability = [2/3,1/3]

        self.currentState = np.random.choice(self.states, p =self.startProbability)
        self.diceValues = [1,2,3,4,5,6]
        self.diceValueProbability = {
            'F': [1/6 for i in range(6)],
            'U': [.1,.1,.1,.1,.1,.5]
        }


    def changeDice(self):
        self.currentState = np.random.choice(self.states,p=self.transitionsProbability[self.currentState])

    def roll(self):
        return np.random.choice(self.diceValues, p=self.diceValueProbability[self.currentState]), self.currentState

    def __call__(self):
        self.changeDice()
        return self.roll()
