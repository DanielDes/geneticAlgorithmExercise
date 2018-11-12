import main
from chromosome import Chromosome
main.parse_data()
fitness = main.fitness_function_procedure
chromosome = Chromosome(['1', '101', '10', '10'],fitness)
chromosome.calculate_value()
