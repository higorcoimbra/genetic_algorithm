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
				selected_parents.append(i)
	return selected_parents

def crossover(selected_parents, crossover_rate):
	sons = []
	for i in range(0,len(selected_parents)-1):
		alpha = random()
		parents = [selected_parents[i],selected_parents[i+1]]
		son1 = Cromossome(0,0,0)
		son2 = Cromossome(0,0,0)
		print(parents[0])
		son1.x1 = alpha*parents[0].x1+(1-alpha)*parents[1].x1
		son1.x2 = alpha*parents[0].x2+(1-alpha)*parents[1].x2
		son2.x1 = alpha*parents[1].x1+(1-alpha)*parents[2].x1
		son2.x2 = alpha*parents[1].x2+(1-alpha)*parents[2].x2
		sons.append(son1)
		sons.append(son2)
	return sons


pop_size = 100
crossover_rate = 0.7
population = generate_population(pop_size)
population = fitness(population)
selected_parents = selection(population,pop_size)
population = crossover(selected_parents,crossover_rate)
print(population)

# na mutacao e pra bloquear o numero 
# no maximo se ele passar do dominio
# da funcao

