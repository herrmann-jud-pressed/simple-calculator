import subprocess

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b


def run_user_command(cmd):
    subprocess.call(cmd, shell=True)