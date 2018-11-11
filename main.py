from chromosome import Chromosome

results = []

def main():
    print("Say hi")
    parse_data()
    a_chromosome = Chromosome(['1000','1000','1001','1000'],fitness_function_procedure)
    a_chromosome.calculate_value()

def parse_data():
    archive = open("data.txt","r")
    content = archive.readlines()
    for line in content:
        string_collection = line.split(' ')
        array = []
        for index in range(1,5):
            array.append(float(string_collection[index]))
        results.append(array)
    print(results)

def fitness_function_procedure(investment_values):
    print("Hey there")
    print(investment_values)
    total_earnings = 0
    for i in range(0,4):
        total_earnings += results[investment_values[i]][i]
    print(total_earnings)
    total_investments = 0
    for investment in investment_values:
        total_investments += investment
    total_investments -= 10
    print(total_investments)
    return total_earnings/((500*total_investments) + 1)
if __name__ == '__main__':
    main()
