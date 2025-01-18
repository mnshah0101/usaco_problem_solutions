import sys
def solve():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    positions = list(map(int, data[1:]))

    positions.sort()

    pass_to = [None] * n
    for i in range(n):
        left_dist = float('inf') if i == 0 else positions[i] - positions[i-1]
        right_dist = float('inf') if i == n - \
            1 else positions[i+1] - positions[i]

        if left_dist <= right_dist:
            pass_to[i] = i-1 if i > 0 else i+1
        else:
            pass_to[i] = i+1 if i < n-1 else i-1

    # Compute in-degree for each cow.
    in_degree = [0]*n
    for i in range(n):
        in_degree[pass_to[i]] += 1

    #  Start with the number of cows that nobody passes to (in_degree == 0)
    answer = sum(1 for i in range(n) if in_degree[i] == 0)

    #  Handle mutual passes.
    # For each pair (i, j) where i < j to avoid double counting:
    #   If pass_to[i] = j AND pass_to[j] = i,
    #   and in_degree[i] = 1 and in_degree[j] = 1,
    #   then add 1 to the answer.
    for i in range(n):
        j = pass_to[i]
        if j > i:  # only check pairs once
            if pass_to[j] == i:  # mutual pass
                if in_degree[i] == 1 and in_degree[j] == 1:
                    answer += 1

    print(answer)


if __name__ == "__main__":
    sys.stdin = open("hoofball.in", "r")
    sys.stdout = open("hoofball.out", "w")
    solve()
