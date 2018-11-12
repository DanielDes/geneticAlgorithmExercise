from chromosome import Chromosome
from random import randint
from random import uniform

results = []
population = []
crossover_rate = 0.4
mutation_rate = 0.1
number_of_gens_in_population = 0
highest_score = 0
def main():
    print("Say hi")
    parse_data()
    # a_chromosome = Chromosome(['1000','11','1','1000'],fitness_function_procedure)
    # b_chromoseom = Chromosome(['1000','11','111','1000'],fitness_function_procedure)
    # population = [a_chromosome,b_chromoseom,b_chromoseom,a_chromosome]
    # print(population)
    # time_to_procreate()
    # a_chromosome.calculate_value()
    # print(a_chromosome.result)
    create_initial_population()
    for i in range(0, 20):
        print("Generation %d"%i)
        generation_iteration()


def generation_iteration():
    for chromosome in population:
        chromosome.calculate_value()
    tournament()
    # check_results()
    time_to_procreate()
    mutation()

def calculate_random_number_in_binay():
    random_number = randint(0,10)
    return "{0:b}".format(random_number)

def tournament():
    winners = []
    highest_score = 0
    for iteration in range(0,len(population)):
        contender_one = population[randint(0,49)]
        contender_two = population[randint(0,49)]
        winner = contender_one if contender_one.result > contender_two else contender_two
        winners.append(winner)
        if winner.result > highest_score:
            highest_score = winner.result
            best_of_the_generation = winner


    print("The best of the generation is")
    print(best_of_the_generation.data)
    print("With score")
    print(highest_score)

    # print(winners)


def time_to_procreate():
    selected_index = []
    # print(len(population))
    for i in range( 0, len(population)):
        random_number = uniform(0,1.0)
        # print(random_number)
        if random_number < crossover_rate:
            # print("pass")
            selected_index.append(i)
    # print(selected_index)
    # print(population)
    for in_list_index, first_parent_index in enumerate(selected_index):
        second_parent_index = 0
        # print(first_parent_index)
        if in_list_index == len(selected_index) - 1:
            second_parent_index = selected_index[0]
        else:
            second_parent_index = selected_index[in_list_index + 1]
        first_parent = population[first_parent_index]
        second_parent = population[second_parent_index]
        # print(first_parent)
        # print(first_parent.data)
        # print(second_parent)
        # print(second_parent.data)


        random_point_genes = randint(0,3)
        # print(random_point_genes)

        first_parent_genes = first_parent.give_group_of_gens(random_point_genes)
        second_parent_genes = second_parent.data
        second_parent_genes.pop(random_point_genes)
        second_parent_genes.insert(random_point_genes, first_parent_genes)
        # print(second_parent_genes)
        son = Chromosome(second_parent_genes,fitness_function_procedure)
        son.calculate_value()
        # print(son)
        # print("-------")
        population.pop(first_parent_index)
        population.insert(first_parent_index,son)
    # print(population)

def check_results():
    for individue in population:
        print(individue.result)
def create_initial_population():
    for i in range(0,50):
        genes = []
        for i in range(0,4):
            genes.append(calculate_random_number_in_binay())
        a_chromosome = Chromosome(genes, fitness_function_procedure)
        population.append(a_chromosome)

def mutation():
    number_of_gens_in_population = len(population[0].data) * len(population)
    number_of_gens_to_mutate = mutation_rate * number_of_gens_in_population
    if number_of_gens_to_mutate % 2 != 0:
        number_of_gens_to_mutate += 1
        # Para hacer la mutation por medio de swap, requiero saber cuantos cromosomas voy a alterar
        # A cada cromosoma voy a mover 2 genes
    number_of_chromosomes = int(number_of_gens_to_mutate / 2)
    for iteration in range(0,number_of_chromosomes):
        # Escogemos aleatorioamente el cromosoma
        randomIndex = randint(0,49)
        chromosome = population[randomIndex]
        gens = chromosome.data
        # print("before")
        # print(chromosome.data)
        # Escogemos dos genes aleatorios
        gen_1_index = randint(0,3)
        gen_1 = gens[gen_1_index]
        # print(gen_1)
        gen_2_index = randint(0,3)
        is_not_different = True
        while is_not_different:
            if gen_2_index == gen_1_index:
                gen_2_index = randint(0,3)
            else:
                is_not_different = False
        gen_2 = gens[gen_2_index]
        # print(gen_2)
        gens[gen_1_index] = gen_2
        gens[gen_2_index] = gen_1
        chromosome.data = gens
        # print("after")
        # print(chromosome.data)
        # print(population[randomIndex].data)

# Procesamos los datos obtenidos
def parse_data():
    archive = open("data.txt","r")
    content = archive.readlines()
    for line in content:
        string_collection = line.split(' ')
        array = []
        for index in range(1,5):
            array.append(float(string_collection[index]))
        results.append(array)
    # print(results)

def fitness_function_procedure(investment_values):
    # print("Hey there")
    # print(investment_values)
    total_earnings = 0
    for i in range(0,4):
        total_earnings += results[investment_values[i]][i]
    # print(total_earnings)
    total_investments = 0
    for investment in investment_values:
        total_investments += investment
    total_investments -= 10
    total_investments = abs(total_investments)
    # print(total_investments)
    return total_earnings/((500*total_investments) + 1)
if __name__ == '__main__':
    main()
