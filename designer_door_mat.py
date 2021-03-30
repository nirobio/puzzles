# Hackerrank - Designer Door Mat
# repetitions of '.|.' with remaining L/R filled with '-'
# top and bottom of central 'WELCOME' belt are symmetrical (hence N//2)

N, M = map(int, input().split())
pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))
