#Mutations


def mutate_string(string, position, character):
    Mutated = string[:position] + character + string[position+1:]
    return Mutated

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
