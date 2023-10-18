from baser.collatz import collatz
def collatz_number(n: int) -> int:
    cnt = 0
    while n != 1:
        n = collatz(n)
        cnt += 1
    return cnt