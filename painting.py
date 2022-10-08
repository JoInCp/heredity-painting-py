import cv2, random, os, sys
import numpy as np
import multiprocessing as mp
from copy import deepcopy
from skimage.metrics import mean_squared_error as compare_mse

img = cv2.imread('img/imgname')
height, width, channels = img.shape

nofg = 50 #number of first genes
noggp = 50 #number of gene groups pergeneration
pomo = 0.01 #probability of mutation occurrence
poaaciagg = 0.3 #probability of adding a circle in a gene group
potdoaciagg = 0.2 #Probability of the disappearance of a circle in a gene group

circle_min, circle_max = 2, 10
image_storage_cycle = 100

class Gene():
  def __init__(self):
    self.radius = random.randint(circle_min, circle_max)
    self.center = np.array([random.randint(0, width), random.randint(0, height)])
    self.color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

  def mutate(self):
    mutation_size = max(1, int(round(random.gauss(15, 4)))) / 100

    r = random.uniform(0, 1)
    if r<0.33:
      self.radius = np.clip(random.randint(
        int(self.radius * (1 - mutation_size)),
        int(self.radius * (1 + mutation_size))
      ), 1, 100)
    elif r<0.66:
      self.center = np.array([
        np.clip(random.randint(int(self.center[0] * (1-mutation_size)), int(self.center[0] * (1+mutation_size))), 0, width),
        np.clip(random.randint(int(self.center[1] * (1-mutation_size)), int(self.center[1] * (1+mutation_size))), 0, height)
      ])
    else:
      self.color = np.array([
        np.clip(random.randint(int(self.color[0] * (1-mutation_size)), int(self.color[0] * (1+mutation_size))), 0, 255),
        np.clip(random.randint(int(self.color[1] * (1-mutation_size)), int(self.color[1] * (1+mutation_size))), 0, 255),
        np.clip(random.randint(int(self.color[2] * (1-mutation_size)), int(self.color[2] * (1+mutation_size))), 0, 255)
      ])

def compute_fitness(genome):
  out = np.ones((height, width, channels), dtype=np.uint8) * 255
  for gene in genome:
    cv2.circle(out, center=tuple(gene.center), radius=gene.radius, color=(int(gene.color[0]), int(gene.color[1]), int(gene.color[2])), thickness=-1)
  fitness = 255. / compare_mse(img, out)
  return fitness, out

def compute_population(g):
  genome = deepcopy(g)
  if len(genome) < 200:
    for gene in genome:
      if random.uniform(0, 1) < pomo:
        gene.mutate()
  else:
    for gene in random.sample(genome, k=int(len(genome) * pomo)):
      gene.mutate()

  if random.uniform(0, 1) < poaaciagg:
    genome.append(Gene())

  if len(genome) > 0 and random.uniform(0, 1) < potdoaciagg:
    genome.remove(random.choice(genome))
    
  new_fitness, new_out = compute_fitness(genome)
  return new_fitness, genome, new_out