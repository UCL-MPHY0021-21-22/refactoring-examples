"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

class boid:
    boids_x = []
    boids_y = []
    boid_x_velocities = []
    boid_y_velocities = []
    
    def _init_(x_low, y_low, x_up, up_y, x_v_low, y_v_low, x_v_up, y_v_up, number):
        
        # initialize boids with given parameters
        self.boids_x=[random.uniform(x_low,x_up) for x in range(number)]
        self.boids_y=[random.uniform(y_low,y_up) for x in range(number)]
        self.boid_x_velocities=[random.uniform(x_v_low,x_v_up) for x in range(number)]
        self.boid_y_velocities=[random.uniform(y_v_low.0,y_v_up) for x in range(number)]

    def update_boids():
        # for each boid
        for i in range(len(boids_x)):
            for j in range(len(boids_x)):
                # Fly towards the middle
                self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boids_x[j]-self.boids_x[i])*0.01/len(self.boids_x)
                self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boids_y[j]-self.boids_y[i])*0.01/len(self.boids_x)
                # Fly away from nearby boids
                if (self.boids_x[j]-self.boids_x[i])**2 + (self.boids_y[j]-self.boids_y[i])**2 < 100:
                    self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boids_x[i]-self.boids_x[j])
                    self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boids_y[i]-self.boids_y[j])
                # Try to match speed with nearby boids
                if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 10000:
                    self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boid_x_velocities[j]-self.boid_x_velocities[i])*0.125/len(self.boids_x)
                    self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boid_y_velocities[j]-self.boid_y_velocities[i])*0.125/len(self.boids_x)

        # Move according to velocities
        for i in range(len(boids_x)):
            boids_x[i]=self.boids_x[i]+self.boid_x_velocities[i]
            boids_y[i]=self.boids_y[i]+self.boid_y_velocities[i]