"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

from typing import List

class Boid:
    def __init__(self, x_position, x_velocity, y_position, y_velocity):
        self.position = {'x' : x_position, 'y' : y_position}
        self.velocity = {'x' : x_velocity, 'y' : y_velocity}

    def update_pos(self):
        self.position['x'] += self.velocity['y']
        self.position['y'] += self.velocity['y']

    def update_vel(self, update:List[float]):
        self.velocity['x'] += update[0]
        self.velocity['y'] += update[1]

def towards_middle(self:Boid, other:Boid, number_of_boids:int, scaling = 0.01):
    """Updates the velocity of self so that it moves toward other"""
    self.update_vel([(self.position['x']-other.position['x'])*scaling/number_of_boids, (self.position['y']-other.position['y'])*scaling/number_of_boids])
    return 0

def away_from_neighbours(self:Boid, other:Boid, number_of_boids:int, distance = 100):
    """Updates the velocity of self so that it moves away from other if other is nearer than distance"""
    if (other.position['x']-self.position['x'])**2 + (other.position['y']-self.position['y'])**2 < distance:
        self.update_vel([(self.position['x']-other.position['x'])/number_of_boids, (self.position['y']-other.position['y'])/number_of_boids])
    return 0

def match_speed_of_neighbours(self:Boid, other:Boid, number_of_boids:int, distance = 10000, scaling = 0.125):
    """Updates the velocity of self so that it is similar to other if other is nearer than distance"""
    if (other.position['x']-self.position['x'])**2 + (other.position['y']-self.position['y'])**2 < distance:
        self.update_vel([(other.velocity['x']-self.velocity['x'])*scaling/number_of_boids, (other.velocity['y']-self.velocity['y'])*scaling/number_of_boids])

def update_boids(boids:List[Boid], number_of_boids:int):
    for self in boids:
        for other in boids:
            towards_middle(self, other, number_of_boids)
            away_from_neighbours(self, other, number_of_boids)
            match_speed_of_neighbours(self, other, number_of_boids)
        self.update_pos()

no_boids = 50
boids = [Boid(random.uniform(-450,50.0), random.uniform(0,10.0), random.uniform(300.0,600.0), random.uniform(-20.0,20.0)) for _ in range(no_boids)]