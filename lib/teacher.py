#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = ["Teaching is fun!"]

    def teach(self):
        return random.choice(self.knowledge)