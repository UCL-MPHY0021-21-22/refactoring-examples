"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random



def update_boids(xs,ys,xvs,yvs):
    max_iteration = len(xs)
    fly_middle(xs,ys,xvs,yvs,max_iteration)
    fly_away(xs,ys,xvs,yvs,max_iteration)
    match_speed(xs,ys,xvs,yvs,max_iteration)
    move(xs,ys,xvs,yvs,max_iteration)


def fly_middle(xs,ys,xvs,yvs,max_iteration):
    """Fly towards the middle"""
    for i in range(max_iteration):
        for j in range(max_iteration):
            xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
    for i in range(max_iteration):
        for j in range(max_iteration):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)

def fly_away(xs,ys,xvs,yvs,max_iteration):
    """Fly away from nearby boids"""
    for i in range(max_iteration):
        for j in range(max_iteration):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
def match_speed(xs,ys,xvs,yvs,max_iteration):
    """Try to match speed with nearby boids"""
    for i in range(max_iteration):
        for j in range(max_iteration):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
def move(xs,ys,xvs,yvs,max_iteration):
    """Move according to velocities"""
    for i in range(max_iteration):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]



def create_number_range(lower_bound,upper_bound,max_number):
    return [random.uniform(lower_bound,upper_bound) for x in range(max_number)]

if __name__ == "__main__":
    number_range = 50
    boids_x = create_number_range(-450,50.0,number_range)
    boids_y = create_number_range(300.0,600.0,number_range)
    boid_x_velocities = create_number_range(0,10.0,number_range)
    boid_y_velocities = create_number_range(-20.0,20.0,number_range)
    boids= update_boids(boids_x,boids_y,boid_x_velocities,boid_y_velocities)