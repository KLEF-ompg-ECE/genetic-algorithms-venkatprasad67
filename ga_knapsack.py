import random
import matplotlib.pyplot as plt
import os

# =============================================================================
# PROBLEM DATA
# =============================================================================

ITEMS = [
    ("Water bottle", 2.0, 9),
    ("First aid kit", 1.5, 10),
    ("Tent", 4.0, 10),
    ("Sleeping bag", 3.0, 9),
    ("Torch", 0.5, 6),
    ("Energy bars (x6)", 1.0, 7),
    ("Rain jacket", 1.0, 8),
    ("Map & compass", 0.3, 7),
    ("Camera", 1.2, 5),
    ("Extra clothes", 2.0, 4),
    ("Cooking stove", 1.5, 6),
    ("Rope (10 m)", 2.5, 5),
    ("Sunscreen", 0.3, 4),
    ("Trekking poles", 1.5, 5),
    ("Power bank", 0.8, 6),
]

NUM_ITEMS = len(ITEMS)
MAX_WEIGHT = 15.0

WEIGHTS = [i[1] for i in ITEMS]
VALUES = [i[2] for i in ITEMS]
NAMES = [i[0] for i in ITEMS]

# =============================================================================
# FITNESS
# =============================================================================

def fitness(chromosome):
    total_weight = sum(WEIGHTS[i] for i in range(NUM_ITEMS) if chromosome[i] == 1)
    total_value = sum(VALUES[i] for i in range(NUM_ITEMS) if chromosome[i] == 1)
    if total_weight > MAX_WEIGHT:
        return 0
    return total_value

# =============================================================================
# GA OPERATORS
# =============================================================================

def tournament_select(population, fitnesses, k=3):
    candidates = random.sample(range(len(population)), k)
    winner = max(candidates, key=lambda i: fitnesses[i])
    return population[winner][:]

def crossover(p1, p2, rate=0.8):
    if random.random() > rate:
        return p1[:]
    cut = random.randint(1, NUM_ITEMS - 1)
    return p1[:cut] + p2[cut:]

def mutate(chromosome, rate):
    result = chromosome[:]
    for i in range(NUM_ITEMS):
        if random.random() < rate:
            result[i] = 1 - result[i]
    return result

# =============================================================================
# GENETIC ALGORITHM
# =============================================================================

def run_ga(population_size=20, generations=50,
           crossover_rate=0.8, mutation_rate=0.05,
           tournament_size=3, seed=42):

    random.seed(seed)

    population = [[random.randint(0, 1) for _ in range(NUM_ITEMS)]
                  for _ in range(population_size)]

    best_chromosome = None
    best_value = -1
    value_log = []

    for _ in range(generations):

        fitnesses = [fitness(c) for c in population]

        gen_best_i = max(range(population_size), key=lambda i: fitnesses[i])
        if fitnesses[gen_best_i] > best_value:
            best_value = fitnesses[gen_best_i]
            best_chromosome = population[gen_best_i][:]

        value_log.append(best_value)

        next_gen = [best_chromosome[:]]

        while len(next_gen) < population_size:
            p1 = tournament_select(population, fitnesses, tournament_size)
            p2 = tournament_select(population, fitnesses, tournament_size)
            child = crossover(p1, p2, crossover_rate)
            child = mutate(child, mutation_rate)
            next_gen.append(child)

        population = next_gen

    return best_chromosome, best_value, value_log

# =============================================================================
# OUTPUT
# =============================================================================

def print_solution(chromosome):
    total_weight = sum(WEIGHTS[i] for i in range(NUM_ITEMS) if chromosome[i] == 1)
    total_value = sum(VALUES[i] for i in range(NUM_ITEMS) if chromosome[i] == 1)

    print("\nBest Packing List")
    print("-" * 35)
    for i in range(NUM_ITEMS):
        if chromosome[i] == 1:
            print("+", NAMES[i])

    print("-" * 35)
    print("Weight :", total_weight)
    print("Value  :", total_value)
    print("Valid  :", "Yes" if total_weight <= MAX_WEIGHT else "No")

def save_plot(value_log, filename, title):
    os.makedirs("plots", exist_ok=True)
    plt.plot(value_log)
    plt.xlabel("Generation")
    plt.ylabel("Best Value")
    plt.title(title)
    plt.grid()
    plt.savefig(filename)
    plt.close()

# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":

    # ==========================================================
    # EXPERIMENT 1 - Baseline
    # ==========================================================
    best_chr, best_val, val_log = run_ga(
        population_size=20, generations=50,
        crossover_rate=0.8, mutation_rate=0.05,
        tournament_size=3, seed=42
    )

    print_solution(best_chr)
    print(f"  Generations run : {len(val_log)}")
    print(f"  Value at gen 1  : {val_log[0]}")
    print(f"  Final best value: {best_val}")
    save_plot(val_log, "plots/experiment_1.png",
              "Baseline  mutation_rate=0.05")

    # ==========================================================
    # EXPERIMENT 2
    # ==========================================================

    # mutation 0.01
    chr2a, val2a, vl2a = run_ga(
        population_size=20, generations=50,
        crossover_rate=0.8, mutation_rate=0.01,
        tournament_size=3, seed=42
    )
    print_solution(chr2a)
    print(f"  Final best value: {val2a}")
    save_plot(vl2a, "plots/experiment_2a.png", "mutation_rate=0.01")

    # mutation 0.05
    chr2b, val2b, vl2b = run_ga(
        population_size=20, generations=50,
        crossover_rate=0.8, mutation_rate=0.05,
        tournament_size=3, seed=42
    )
    print_solution(chr2b)
    print(f"  Final best value: {val2b}")
    save_plot(vl2b, "plots/experiment_2b.png", "mutation_rate=0.05")

    # mutation 0.30
    chr2c, val2c, vl2c = run_ga(
        population_size=20, generations=50,
        crossover_rate=0.8, mutation_rate=0.30,
        tournament_size=3, seed=42
    )
    print_solution(chr2c)
    print(f"  Final best value: {val2c}")
    save_plot(vl2c, "plots/experiment_2c.png", "mutation_rate=0.30")
