#Set Mutations


# Enter your code here. Read input from STDIN. Print output to STDOUT
A_len = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    operation, operation_set_len = input().split()
    operation_set = set(map(int, input().split()))
    
    match operation:
        case "update":
            A.update(operation_set)
        case "intersection_update":
            A.intersection_update(operation_set)
        case "difference_update":
            A.difference_update(operation_set)
        case "symmetric_difference_update":
            A.symmetric_difference_update(operation_set)

print(sum(A))
