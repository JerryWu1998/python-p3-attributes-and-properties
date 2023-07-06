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
    "Purchasing",
]


class Person:
    def __init__(self, name=None, job=None):
        if name is not None:
            self.name = name
        if job is not None:
            self.job = job

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) == str and len(new_name) >= 1 and len(new_name) <= 25:
            self._name = new_name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
