import numpy as np

# Как правильно задавать начальное распределение?

class Croupier():
    def __init__(
        self,unfairDiceProbability, probabilityChangeFromFair, 
        probabilityChangeFromUnfair, is_current_state_fair = None ,
        fairDiceProbability = None ,random_seed = None):
        
        if random_seed is None: 
            self.random_seed = 1
        else: self.random_seed = random_seed

        if fairDiceProbability is None:
             self.fairDiceProbability = [1/6 for i in range(6)]
        else: self.fairDiceProbability = fairDiceProbability

        self.unfairDiceProbability = unfairDiceProbability

        self.diceValue = [1,2,3,4,5,6]

        if is_current_state_fair is None:
            self.is_current_state_fair = np.random.choice([False, True])
        else: self.is_current_state_fair = is_current_state_fair

        self.probabilityChangeFromFair = probabilityChangeFromFair
        self.probabilityChangeFromUnfair = probabilityChangeFromUnfair

    def __call__(self):
        self.changeBone()
        return self.generate()

    def generate(self):
        """
        Кидаем текущую кость
        """
        probabilities = self.fairDiceProbability if self.is_current_state_fair else self.unfairDiceProbability
        value = np.random.choice(self.diceValue,1,probabilities)
        state = 'F' if self.is_current_state_fair else 'U'
        return value[0], state


    def changeBone(self):
        """
        Определяем, будем ли мы менять кости или нет
        """
        probabilities = self.probabilityChangeFromFair if self.is_current_state_fair else self.probabilityChangeFromUnfair
        self.is_current_state_fair = np.random.choice([False, True], 1, p=probabilities)
