"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

# 
class boid:
    boids_x = []
    boids_y = []
    boid_x_velocities = []
    boid_y_velocities = []
    
    def _init_(low_x, low_y, up_x, up_y, x_v_low, y_v_low, x_v_up, y_v_up, number):
        # self.boids_x = boids_x
        # self.boids_y = boids_y
        # self.boid_x_velocities = boid_x_velocities
        # self.boid_y_velocities = boid_y_velocities

        self.boids_x=[random.uniform(-450,50.0) for x in range(50)]
        self.boids_y=[random.uniform(300.0,600.0) for x in range(50)]
        self.boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
        self.boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]

    def update_boids():
        for i in range(len(boids_x)):
            for j in range(len(boids_x)):
                self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boids_x[j]-self.boids_x[i])*0.01/len(self.boids_x)
                self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boids_y[j]-self.boids_y[i])*0.01/len(self.boids_x)
                if (self.boids_x[j]-self.boids_x[i])**2 + (self.boids_y[j]-self.boids_y[i])**2 < 100:
                    self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boids_x[i]-self.boids_x[j])
                    self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boids_y[i]-self.boids_y[j])
                if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 10000:
                    self.boid_x_velocities[i]=self.boid_x_velocities[i]+(self.boid_x_velocities[j]-self.boid_x_velocities[i])*0.125/len(self.boids_x)
                    self.boid_y_velocities[i]=self.boid_y_velocities[i]+(self.boid_y_velocities[j]-self.boid_y_velocities[i])*0.125/len(self.boids_x)

        # change the location of the boid
        for i in range(len(boids_x)):
            boids_x[i]=self.boids_x[i]+self.boid_x_velocities[i]
            boids_y[i]=self.boids_y[i]+self.boid_y_velocities[i]


# # update the location of the boid using its current location and velocities
# def update_boids(boids):
#     boids_x,boids_y,boid_x_velocities,boid_y_velocities=boids
#     # Fly towards the middle
#     # Fly away from nearby boids
#     # Try to match speed with nearby boids
#     # Move according to velocities
#     for i in range(len(boids_x)):
#         for j in range(len(boids_x)):
#             boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[j]-boids_x[i])*0.01/len(boids_x)
#             boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[j]-boids_y[i])*0.01/len(boids_x)
#             if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 100:
#                 boid_x_velocities[i]=boid_x_velocities[i]+(boids_x[i]-boids_x[j])
#                 boid_y_velocities[i]=boid_y_velocities[i]+(boids_y[i]-boids_y[j])
#             if (boids_x[j]-boids_x[i])**2 + (boids_y[j]-boids_y[i])**2 < 10000:
#                 boid_x_velocities[i]=boid_x_velocities[i]+(boid_x_velocities[j]-boid_x_velocities[i])*0.125/len(boids_x)
#                 boid_y_velocities[i]=boid_y_velocities[i]+(boid_y_velocities[j]-boid_y_velocities[i])*0.125/len(boids_x)

#     # change the location of the boid
#     for i in range(len(boids_x)):
#         boids_x[i]=boids_x[i]+boid_x_velocities[i]
#         boids_y[i]=boids_y[i]+boid_y_velocities[i]
