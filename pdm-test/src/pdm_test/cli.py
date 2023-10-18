import typer
from .conjectures import collatz_number

def compute_collatz(n: int):
    print(f"collatz number of {n} is {collatz_number(n)}")

def main():
    typer.run(compute_collatz)

if __name__ == "__main__":
    typer.run(compute_collatz)