import torch
import torch.nn as nn
import numpy as np
import json

with open(r'C:\Users\KDCA\Desktop\IL\field_data.json') as f:
        p = json.load(f)

p = p[0]

data_ = []
labels_ = []

for i in range(len(p)):
	data_.append(p[i][0][0])
	labels_.append(p[i][0][1]+[0])

data = torch.tensor(data_[0])
labels = torch.tensor(labels_[0])

# Define a function to create a random neural network
def create_random_net(input_size, output_size, min_layers=3, max_layers=8, min_neurons=4, max_neurons=20):
    num_layers = np.random.randint(min_layers, max_layers+1)
    layers = []
    in_size = input_size
    for i in range(num_layers):
        out_size = np.random.randint(min_neurons, max_neurons+1)
        layers.append(nn.Linear(in_features=in_size, out_features=out_size))
        layers.append(nn.ReLU())
        in_size = out_size
    layers.append(nn.Linear(in_features=in_size, out_features=output_size))
    return nn.Sequential(*layers)

# Define a function to evaluate the performance of a neural network
def evaluate_net(net, data, labels):
    output = net(data)
    loss = nn.MSELoss()(output, labels)
    return loss

# Define the genetic algorithm
population_size = 100
num_generations = 100
input_size = 121
output_size = 6

# Initialize the population
population = [create_random_net(input_size, output_size) for _ in range(population_size)]

for generation in range(num_generations):
    # Evaluate the performance of each individual
    fitness = [evaluate_net(net, data, labels) for net in population]

    # Select the best individuals to form the next generation
    next_population = []
    for _ in range(population_size):
        best_index1 = torch.argmin(torch.tensor(fitness))
        next_population.append(population[best_index1])
        fitness[best_index1] = float('inf')
        best_index2 = torch.argmin(torch.tensor(fitness))
        next_population.append(population[best_index2])
        fitness[best_index2] = float('inf')

    # Crossover and mutation to generate new individuals
    for i in range(population_size):
        parent1 = next_population[np.random.randint(population_size)]
        parent2 = next_population[np.random.randint(population_size)]
        child = []
        for j, (param1, param2) in enumerate(zip(parent1.children(), parent2.children())):
            if np.random.rand() < 0.5:
                child.append(param1)
            else:
                child.append(param2)
        child = nn.Sequential(*child)
        next_population.append(child)

    population = next_population

# The final population will contain the best-performing neural networks
best_net = population[np.argmin([evaluate_net(net, data, labels) for net in population])]
