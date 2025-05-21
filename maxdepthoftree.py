def maxDepth(values, index=0):
    if index >= len(values) or values[index] == -1:
        return 0
    left = maxDepth(values, 2 * index + 1)
    right = maxDepth(values, 2 * index + 2)
    return max(left, right) + 1
user_input = input("Enter tree nodes in level order (use None for null):\n")
values = list(map(int, user_input.strip().split()))
print(maxDepth(values))
