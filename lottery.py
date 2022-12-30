# Python Program with process fork, os.fork() method
# Megasena and Quina Brazilian Lottery

# os module to handle multiple process fork parent and child processes
import os
import random

# Parent process will generate Megasena combination
# Using os.fork() method
# In this point of code will be two execution threads
pid = os.fork()

# pid greater than 0 is associated with parent process
# Parent process - Megansena
if pid > 0:
    cartela = random.randint(1, 50063860)
    jogo = 0
    for a in range(0, 60):
        for b in range(a+1, 60):
            for c in range(b+1, 60):
                for d in range(c+1, 60):
                    for e in range(d+1, 60):
                        for f in range(e+1, 60):
                            jogo = jogo+1
                            if (jogo == cartela):
                                print(
                                    "Encontrei um número da Megasena no processo Pai")
                                print(
                                    "Percorri no processo Pai 50.063.860 combinações que correspondem a combinação de 60, 6 a 6")
                                print(str(jogo) + ' ' + str(a+1) + ' ' + str(b+1) + ' ' +
                                      str(c+1) + ' ' + str(d+1) + ' ' + str(e+1) + ' ' + str(f+1))

# pid equal to 0 is associated with child process
# Child process - Quina
else:
    cartela = random.randint(1, 24040016)
    jogo = 0
    for a in range(0, 80):
        for b in range(a+1, 80):
            for c in range(b+1, 80):
                for d in range(c+1, 80):
                    for e in range(d+1, 80):
                        jogo = jogo+1
                        if (jogo == cartela):
                            print("Encontrei um número da Quina no processo filho")
                            print(
                                "Percorri no processo filho 24.040.016 combinações que correspondem a combinação de 80, 5 a 5")
                            print(str(jogo) + ' ' + str(a+1) + ' ' + str(b+1) +
                                  ' ' + str(c+1) + ' ' + str(d+1) + ' ' + str(e+1))

# In case of any error associated with process fork,
# os.fork() method throws OSError exception.
