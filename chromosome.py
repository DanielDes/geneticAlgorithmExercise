class Chromosome:

    def __init__(self,data,fitnessfunction):
        #Data is an array of strings
        self.data = data
        self.calculate_integer_values()
        self.fitness_function = fitnessfunction
        self.result = 0

    def give_group_of_gens(self,index):
        return self.data[index]
    def give_group_off_gens_excluding(self, index):
        return [self.data[:index],self.data[index:]]
    def calculate_integer_values(self):
        self.integerValues = []
        for string_value in self.data:
            self.integerValues.append(int(string_value,2))
        # print(self.integerValues)
    def calculate_value(self):
        self.result = self.fitness_function(self.integerValues)
        # print(self.result)

    def mutate_group_of_gens(self,gens,index):
        self.data[index] = gens
        self.calculate_integer_values()
