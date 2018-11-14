from chromosome import Chromosome
from random import randint
from random import uniform

results = []
population = []
crossover_rate = 0.8
mutation_rate = 0.1
RESULT_FILE_NAME = "resultados.txt"
RAW_AVERAGE_FILE_NAME = "promedios.txt"

def main():
    print("Say hi")
    file_stream = open(RESULT_FILE_NAME,"w")
    average_data_stream = open(RAW_AVERAGE_FILE_NAME,"w")
    parse_data()
    create_initial_population()
    for i in range(0, 20):
        print("-----------------------------")
        print("Generation %d"%i)
        average = generation_iteration()
        file_stream.write("Generation %d \n" % i)
        file_stream.write("%f\n"%average)
        average_data_stream.write("%f\n"%average)
        # determine_average_value()
    # iteration_counter = 0
    # has_reached = False
    # while not has_reached:
    #     print("Generation %d" % iteration_counter)
    #     generation_iteration()
    #     has_reached = determine_if_reached_desire_value(2)
    #     iteration_counter += 1
    file_stream.close()

def determine_average_value():
    sumatory = 0
    for chromosome in population:
        sumatory += chromosome.result
    result = sumatory / len(population)
    print("Average value of generation ")
    print(result)

def determine_if_reached_desire_value(value):
    for chromosome in population:
        if chromosome.result > value:
            print("Reached value with")
            print(chromosome.data)
            print(chromosome.result)
            return True
    return False
def generation_iteration():
    sumatory = 0
    for chromosome in population:
        chromosome.calculate_value()
        sumatory += chromosome.result
    average = sumatory / len(population)
    print("Average value of generation ")
    print(average)
    tournament()
    time_to_procreate()
    mutation()
    return average

def calculate_random_number_in_binay():
    random_number = randint(0,10)
    return "{0:b}".format(random_number)

def tournament():
    winners = []
    highest_score = 0
    for iteration in range(0,len(population)):
        contender_one = population[randint(0,49)]
        contender_two = population[randint(0,49)]
        winner = contender_one if contender_one.result > contender_two.result else contender_two
        winners.append(winner)
        if winner.result > highest_score:
            highest_score = winner.result
            best_of_the_generation = winner


    print("The best of the generation is")
    print(best_of_the_generation.data)
    print("With score")
    print(highest_score)



def time_to_procreate():
    selected_index = []
    for i in range( 0, len(population)):
        random_number = uniform(0,1.0)
        if random_number < crossover_rate:
            selected_index.append(i)
    for in_list_index, first_parent_index in enumerate(selected_index):
        second_parent_index = 0
        if in_list_index == len(selected_index) - 1:
            second_parent_index = selected_index[0]
        else:
            second_parent_index = selected_index[in_list_index + 1]
        first_parent = population[first_parent_index]
        second_parent = population[second_parent_index]
        random_point_genes = 2
        first_parent_genes = first_parent.give_group_of_gens(random_point_genes)
        second_parent_genes = second_parent.data
        second_parent_genes.pop(random_point_genes)
        second_parent_genes.insert(random_point_genes, first_parent_genes)
        son = Chromosome(second_parent_genes,fitness_function_procedure)
        population.pop(first_parent_index)
        population.insert(first_parent_index,son)

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

"""
La mutacion qu eescogi, es por medio de swap, donde teniendo el numero de genes que
se van a modificar, determino el numero de cromosomas que voy a mutar, en funcion al
numero de genes que voy a mutar por cromosoma.
"""

def mutation():
    number_of_gens_in_population = len(population[0].data) * len(population)
    number_of_gens_to_mutate = mutation_rate * number_of_gens_in_population
    if number_of_gens_to_mutate % 2 != 0:
        number_of_gens_to_mutate += 1
        # Para hacer la mutacion por medio de swap, requiero saber cuantos cromosomas voy a alterar
        # A cada cromosoma voy a mover 2 genes
    number_of_chromosomes = int(number_of_gens_to_mutate / 2)
    for iteration in range(0,number_of_chromosomes):
        # Escogemos aleatorioamente el cromosoma
        randomIndex = randint(0,49)
        chromosome = population[randomIndex]
        gens = chromosome.data
        gen_1_index = randint(0,3)
        gen_1 = gens[gen_1_index]
        gen_2_index = randint(0,3)
        is_not_different = True
        while is_not_different:
            if gen_2_index == gen_1_index:
                gen_2_index = randint(0,3)
            else:
                is_not_different = False
        gen_2 = gens[gen_2_index]
        gens[gen_1_index] = gen_2
        gens[gen_2_index] = gen_1
        chromosome.data = gens

"""
Abrimos el archivo con los resultados previamente obtenidos. Y los vamos guardando en
un arreglo para que posteriormente se use al hacer la evaluacion con la funcion fitness
"""
def parse_data():
    archive = open("data.txt","r")
    content = archive.readlines()
    for line in content:
        string_collection = line.split(' ')
        array = []
        for index in range(1,5):
            array.append(float(string_collection[index]))
        results.append(array)
"""
En este metodo tenemos definido el procedimiento de la funcion de fitness. Esta funcion
se pasa como closure a cada cromosoma, de ese modo no tenemos que pasar el arreglo
de datos que se usa en la funcion, y por lo tanto, actualizar el arreglo a cada cromosoma
en caso de ser necesario, aunque en este ejercicio no ocurre eso.
"""
def fitness_function_procedure(investment_values):
    total_earnings = 0
    for i in range(0,4):
        total_earnings += results[investment_values[i]][i]
    total_investments = 0
    for investment in investment_values:
        total_investments += investment
    total_investments -= 10
    total_investments = abs(total_investments)
    return total_earnings/((500*total_investments) + 1)

if __name__ == '__main__':
    main()
