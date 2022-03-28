# a = [
#   [ (value, index_column) ], - i == 0
#   []      - i == 1
# ] 

class matrice:


    def __init__(self, n) -> None:
        self.n = 0
        self.a = []
        for i in range(0, n): 
            self.a.append([])
    
    def read_values(self, line):
        numbers = line.split(", ")
        value = float(numbers[0])
        index_line = int(numbers[1])
        index_column = int(numbers[2])
        
        if len(self.a[index_line]) == 0:
            self.a[index_line] = [(value, index_column)]
        else :
            found_flag = False
            for idx, tpl in enumerate(self.a[index_line]):
                if tpl[1] == index_column:
                    self.a[index_line][idx] = (tpl[0] + value, tpl[1])
                    found_flag = True
            if not found_flag:
                self.a[index_line].append((value, index_column))


file1 = open('a.txt', 'r')
n = int(file1.readline())
file1.readline()
Lines = file1.readlines()
matr = matrice(n)
for line in Lines:
    # print("Line {}".format(line.strip()))
    matr.read_values(line)
#print(matr.a)
file1.close()


file1 = open('b.txt', 'r')
file1.readline()
file1.readline()
Lines = file1.readlines()
for line in Lines:
    # print("Line {}".format(line.strip()))
    matr.read_values(line)
print(matr.a)
file1.close()


file2 = open('a_plus_b.txt', 'r')
n = int(file2.readline())
file2.readline()
Lines = file2.readlines()
matr_a_plus_b = matrice(n)
for line in Lines:
    # print("Line {}".format(line.strip()))
    matr_a_plus_b.read_values(line)
print(matr_a_plus_b.a)

equals = True

for index_line in range(n):
    for idx, tpl in enumerate(matr.a[index_line]):
        if tpl not in matr_a_plus_b.a[index_line]:
            equals = False

for index_line in range(n):
    for idx, tpl in enumerate(matr_a_plus_b.a[index_line]):
        if tpl not in matr.a[index_line]:
            equals = False

print(equals)