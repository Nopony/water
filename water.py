from random import *
import copy
import time

def InsertBefore(string, index, character):
    return string[:index] + character + string[index + 1:]

class Window:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.frameTime = 1.0 / fps

        self.matrix = []
        for i in range(0, height):
            el = ''
            for j in range(0, width):
                el += '.'
            self.matrix.append(el)

    def line(self, width, offset, char):
        prefix = offset
        suffix = self.width - offset - width
        return '.'*prefix + char*width + '.'*suffix

    def clear(self):
        print(chr(27) + "[2J")

    def display(self):
        for line in self.matrix:
            print(line)
    def loop(self, N):
        for i in range(0, N):
            if(i < N/2):
                window.matrix[0] = window.line(1, 45, '#')
            self.simulate()
            window.matrix[len(window.matrix) - 1] = self.line(0,0,'')
            # self.clear()
            # self.display()
            # time.sleep(self.frameTime)
        remaining = 0
        for line in self.matrix:
            for char in line:
                if(char == '#'):
                     remaining += 1
        return remaining
    def loopDisplay(self, N):
        for i in range(0, N):
            if(i < N/2):
                window.matrix[0] = window.line(1, 45, '#')
            self.simulate()
            window.matrix[len(window.matrix) - 1] = self.line(0,0,'')
            self.clear()
            self.display()
            time.sleep(self.frameTime)
    def clearMatrix(self):
        self.matrix = []
        for i in range(0, self.height):
            el = ''
            for j in range(0, self.width):
                el += '.'
            self.matrix.append(el)
    def simulate(self):
        lidx = len(self.matrix) - 1
        while(lidx >= 0):
            cidx = 0
            while(cidx < len(self.matrix[lidx])):
                if(self.matrix[lidx][cidx] == '#'):
                    if(lidx != len(self.matrix) - 1):
                        if(self.matrix[lidx+1][cidx] == '.'):
                            self.matrix[lidx] = self.matrix[lidx][:cidx] + '.' + self.matrix[lidx][cidx+1:]
                            self.matrix[lidx+1] = self.matrix[lidx+1][:cidx] + '#' + self.matrix[lidx+1][cidx+1:]
                        else:
                            if(cidx != 0 and cidx != len(self.matrix[lidx]) - 1):
                                if(self.matrix[lidx][cidx+1] == '.' and self.matrix[lidx][cidx-1] == '.'):
                                    # print 1
                                    charOffset = randint(-1, 1)
                                    self.matrix[lidx] = self.matrix[lidx][:cidx] + '.' + self.matrix[lidx][cidx+1:]
                                    self.matrix[lidx] = self.matrix[lidx][:cidx + charOffset] + '#' + self.matrix[lidx][cidx + charOffset + 1:]
                                elif(self.matrix[lidx][cidx+1] != '.' and self.matrix[lidx][cidx-1] != '.'): papiez = 'xd'
                                elif(random() > 0.25):
                                    if(self.matrix[lidx][cidx+1] != '.'):
                                        self.matrix[lidx] = self.matrix[lidx][:cidx - 1] + '#.' + self.matrix[lidx][cidx + 1:]
                                        cidx += 1
                                        # print str(len(self.matrix[lidx])) + " : 3"
                                    else:
                                        self.matrix[lidx] = self.matrix[lidx][:cidx] + '.#' + self.matrix[lidx][cidx+2:]
                                        # print str(len(self.matrix[lidx])) + " : 4"

                    else:
                        if(cidx != 0 and cidx != len(self.matrix[lidx]) - 1):
                            if(self.matrix[lidx][cidx+1] == '.' and self.matrix[lidx][cidx-1] == '.'):
                                # print 1
                                charOffset = randint(-1, 1)
                                self.matrix[lidx] = self.matrix[lidx][:cidx] + '.' + self.matrix[lidx][cidx+1:]
                                self.matrix[lidx] = self.matrix[lidx][:cidx + charOffset] + '#' + self.matrix[lidx][cidx + charOffset + 1:]
                            elif(self.matrix[lidx][cidx+1] != '.' and self.matrix[lidx][cidx-1] != '.'): papiez = 'xd'
                            elif(random() > 0.25):
                                if(self.matrix[lidx][cidx+1] != '.'):
                                    self.matrix[lidx] = self.matrix[lidx][:cidx - 1] + '#.' + self.matrix[lidx][cidx + 1:]
                                    cidx += 1
                                    # print str(len(self.matrix[lidx])) + " : 3"
                                else:
                                    self.matrix[lidx] = self.matrix[lidx][:cidx] + '.#' + self.matrix[lidx][cidx+2:]
                                    # print str(len(self.matrix[lidx])) + " : 4"


                cidx += 1
            lidx -= 1



window = Window(86, 24, 30)
# window.matrix[10] = window.line(10, 40, 'X')
# window.matrix[9] = "...#..#..##.############################X........X..................................."
# window.matrix[8] = "...#..#..##.############################X........X..................................."
# window.loop()


def generate():

    arr = []
    for i in range(0,18):
        arr.append('.' * 42)

    Xs = 30

    while(Xs > 0):
        l = randint(min(2, Xs), min(15, Xs))
        originLine = randint(2, 15)
        originChar = randint(2, 39)

        while(arr[originLine][originChar] == '#'):
            originLine = randint(2, 15)
            originChar = randint(2, 39)

        verticalOffset = 0

        direction = 1 if random() > 0.5 else -1

        for i in range(1, l+1):
            possibleJumps = []
            if(arr[(originLine + verticalOffset) % 18][(originChar + i * direction) % 42] == '.'):
                possibleJumps.append([(originLine + verticalOffset) % 18, (originChar + i * direction) % 42])
            if(arr[(originLine + verticalOffset - 1) % 18][(originChar + i * direction) % 42] == '.'):
                possibleJumps.append([(originLine + verticalOffset - 1) % 18, (originChar + i * direction) % 42])
            if(arr[(originLine + verticalOffset + 1) % 18][(originChar + i * direction) % 42] == '.'):
                possibleJumps.append([(originLine + verticalOffset + 1) % 18, (originChar + i * direction) % 42])
            if(len(possibleJumps) == 0):
                 break
            jump = possibleJumps[randint(0, len(possibleJumps) - 1)]

            arr[jump[0]] = arr[jump[0]][:jump[1]] + 'X' + arr[jump[0]][jump[1] + 1:]
            Xs -= 1
            verticalOffset = jump[0] - originLine

    return arr

def mutate(spec):
    specimen = copy.copy(spec)
    idx1 = [randint(0, len(specimen) - 1), randint(0, len(specimen[0]) - 1)]
    idx2 = idx1
    while(specimen[idx1[0]][idx1[1]] == specimen[idx2[0]][idx2[1]]):
        idx2 = [randint(0, len(specimen) - 1), randint(0, len(specimen[0]) - 1)]

    tmp = specimen[idx1[0]][idx1[1]]
    specimen[idx1[0]] = InsertBefore(specimen[idx1[0]], idx1[1], specimen[idx2[0]][idx2[1]])
    specimen[idx2[0]] = InsertBefore(specimen[idx2[0]], idx2[1], tmp)

    return specimen

def crossMutate(x, y):
    a = copy.copy(x)
    b = copy.copy(y)

    idx1 = [randint(0, len(a) - 1), randint(0, len(a[0]) - 1)]
    while(a[idx1[0]][idx1[1]] != 'X'): idx1 = [randint(0, len(a) - 1), randint(0, len(a[0]) - 1)]
    idx2 = [randint(0, len(b) - 1), randint(0, len(b[0]) - 1)]
    while(b[idx2[0]][idx2[1]] != '.'): idx2 = [randint(0, len(b) - 1), randint(0, len(b[0]) - 1)]

    tmp = a[idx1[0]][idx1[1]]
    a[idx1[0]] = InsertBefore(a[idx1[0]], idx1[1], b[idx2[0]][idx2[1]])
    b[idx2[0]] = InsertBefore(b[idx2[0]], idx2[1], tmp)


    return [a, b]

def grade(specimen, window):

    window.clearMatrix()
    for idx, line in enumerate(specimen):
        line = '.'*22 + line + '.'*22
        window.matrix[idx + 4] = line

    return window.loop(100) / 50.0

def iterate(population):
     gradedPopulation = map(lambda specimen: [grade(specimen, window), specimen], population)

     gradedPopulation.sort(key=lambda tup: -tup[0])

     print gradedPopulation[0][0]

     newGeneration = []
     for i in range(0, 25):
         newGeneration.append(gradedPopulation[i][1])
         newGeneration.append(mutate(mutate(mutate(mutate(gradedPopulation[i][1])))))
         newGeneration.append(mutate(mutate(mutate(mutate(gradedPopulation[i][1])))))
         newGeneration.append(mutate(mutate(mutate(mutate(gradedPopulation[i][1])))))

     for i in range(0, 5):
         for j in range(5, 15):
             mutated = crossMutate(gradedPopulation[i][1], gradedPopulation[j][1])
             newGeneration.append(mutated[0])
             newGeneration.append(mutated[1])

     print len(newGeneration)
     return newGeneration

def evolve(basePopulationSize, iterationsAmount, window):
    population = []
    for i in range(0, basePopulationSize):
        population.append(generate())

    for i in range(0, iterationsAmount):
        population = iterate(population)

    gradedPopulation = map(lambda specimen: [grade(specimen, window), specimen], population)

    gradedPopulation.sort(key=lambda tup: -tup[0])

    window.clearMatrix()
    for idx, line in enumerate(gradedPopulation[0][1]):
        line = '.'*22 + line + '.'*22
        window.matrix[idx + 4] = line
    print "Fitness achieved: " + str(gradedPopulation[0][0])
    window.display()
    return gradedPopulation[0][1]

evolve(500, 5, window)

time.sleep(5)
window.loopDisplay(500)
