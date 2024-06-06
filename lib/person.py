#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        if name:
            self.set_name(name)
        if job:
            self.set_job(job)

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()  # Convert to title case

    def set_job(self, job):
        approved_jobs = ["Sales", "Engineer", "Doctor", "ITC"]
        if job not in approved_jobs:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job