from random import random, uniform
from math import sin, sqrt

# offset of function to turn negative numbers into positive ones
offset = 1500

# function domain
min_domain = -600
max_domain = 600

class Cromossome:
	def __init__(self, x1, x2,fitness):
		self.x1 = x1
		self.x2 = x2
		self.fitness = fitness


# define population list
def generate_population(pop_size):
	population = []
	for i in range(0,pop_size):
		cromossome = Cromossome(uniform(min_domain,max_domain),uniform(min_domain,max_domain),0)
		population.append(cromossome)
	return population

# generate fitness value for every cromossome in population
def fitness(population):
	for c in population:
		c.fitness = (-c.x2+47)*sin(sqrt(abs(c.x2+(c.x1/2)+47)))-c.x1*sin(sqrt(abs(c.x1-(c.x2+47))))
		c.fitness = -c.fitness+offset
	return population

# selection process - roulette wheel
def selection(population,pop_size):
	roullete = []
	value = 0
	# roullete ranges
	roullete.append(0)
	for c in population:
		value += c.fitness
		roullete.append(value)
	# selection with random number
	selected_parents = []
	for i in range(0,pop_size):
		rand = uniform(0.0,max(roullete))
		for i in range(1,len(roullete)):
			if(rand > roullete[i-1] and rand < roullete[i]):
				selected_parents.append(i-1)
	return selected_parents

def crossover(population, selected_parents, crossover_rate):
	sons = []
	i = 0
	while i < len(selected_parents):
		alpha = random()
		parents = [population[selected_parents[i]], population[selected_parents[i+1]]]
		if(random() < crossover_rate):
			son1 = Cromossome(0,0,0)
			son2 = Cromossome(0,0,0)
			son1.x1 = alpha*parents[0].x1+(1-alpha)*parents[1].x1
			son1.x2 = alpha*parents[0].x2+(1-alpha)*parents[1].x2
			son2.x1 = alpha*parents[1].x1+(1-alpha)*parents[0].x1
			son2.x2 = alpha*parents[1].x2+(1-alpha)*parents[0].x2
		else:
			son1 = population[selected_parents[i]]
			son2 = population[selected_parents[i+1]]
		sons.append(son1)
		sons.append(son2)
		i = i+2
	return sons

def mutacao(population, mutation_rate):
	for c in population:
		if(random() < mutation_rate):
			mutated_value = c.x1+uniform(-2.0,2.0)
			if(not(mutated_value < -600)):
				c.x1 = mutated_value
			else:
				c.x1 = -600
			if(not(mutated_value > 600)):
				c.x1 = mutated_value
			else:
				c.x1 = 600

		if(random() < mutation_rate):
			mutated_value = c.x2+uniform(-2.0,2.0)
			if(not(mutated_value < -600)):
				c.x2 = mutated_value
			else:
				c.x2 = -600
			if(not(mutated_value > 600)):
				c.x2 = mutated_value
			else:
				c.x2 = 600
	return population

def print_population(population):
	for c in population:
		print(str(c.x1)+" "+str(c.x2))

pop_size = 100
crossover_rate = 0.7
mutation_rate = 0.1
population = generate_population(pop_size)
generations = 30
for i in range(0,generations):
	population = fitness(population)
	selected_parents = selection(population,pop_size)
	population = crossover(population, selected_parents, crossover_rate)
	population = mutacao(population,mutation_rate)

