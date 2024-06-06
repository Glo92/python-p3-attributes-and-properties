#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        if name:
            self.set_name(name)
        if breed:
            self.set_breed(breed)

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

    def set_breed(self, breed):
        approved_breeds = ["Pug", "Beagle", "Bulldog", "Labrador", "Golden Retriever"]
        if breed not in approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self.breed = breed