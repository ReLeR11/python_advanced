n, m = map(int, input().split())

n_numbers = set()
m_numbers = set()

for _ in range(n):
    n_numbers.add(input())

for _ in range(m):
    m_numbers.add(input())

result = n_numbers.intersection(m_numbers)

print(*result, sep="\n")
