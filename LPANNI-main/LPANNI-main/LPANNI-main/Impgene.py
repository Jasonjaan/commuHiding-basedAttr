import random

# 遗传算法参数
POPULATION_SIZE = 10
GENERATION_COUNT = 100
MUTATION_RATE = 0.1

# 目标函数（这里是一个简单的例子，你需要根据具体问题定义你的目标函数）
def fitness(individual):
    return sum(individual)

# 初始化种群
def initialize_population():
    return [[random.randint(0, 1) for _ in range(5)] for _ in range(POPULATION_SIZE)]

# 选择操作
def selection(population):
    return random.choice(population)

# 交叉操作
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# 变异操作
def mutation(individual):
    mutated_index = random.randint(0, len(individual) - 1)
    individual[mutated_index] = 1 - individual[mutated_index]
    return individual

# 遗传算法主体
def genetic_algorithm():
    population = initialize_population()

    for generation in range(GENERATION_COUNT):
        # 计算适应度
        fitness_scores = [fitness(individual) for individual in population]

        # 选择两个个体进行交叉操作
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)

        # 根据变异率进行变异操作
        if random.random() < MUTATION_RATE:
            child = mutation(child)

        # 替换最差的个体
        min_fitness_index = fitness_scores.index(min(fitness_scores))
        population[min_fitness_index] = child

        # 输出每一代的最佳解
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation + 1}: Best Individual {best_individual}, Fitness {max(fitness_scores)}")

    # 输出最终的最佳解
    final_best_individual = population[fitness_scores.index(max(fitness_scores))]
    print("\nFinal Best Individual:", final_best_individual)

if __name__ == "__main__":
    genetic_algorithm()
