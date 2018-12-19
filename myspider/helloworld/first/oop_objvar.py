#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Robot:
    """一个有名字的机器人"""
    population = 0
    def __init__(self, name):
        """数据的初始化"""
        self.name = name
        print("(initializing {})".format(self.name))
        Robot.population += 1
    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))

        else:
            print("there are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人真挚的问候"""
        print("greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """print now have how many population"""
        print("we have {:d} robots.".format(cls.population))

droid1 = Robot("r2-d2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("c-3po")
droid2.say_hi()
Robot.how_many()

print("robots have finished their work. so let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
print(Robot.__doc__)