from random import random
from echo import Ecosystem as Echo
import time

MAXGAMES = 200
MAXSCORE = -1

if __name__ == "__main__":
    option = {
                "parent_count": 5,
                "gene_count": 20,
                "gene_length": 6,
                "mutation_probability": 0.05
            }
    echo = Echo(option)

    while echo.generation <= MAXGAMES:
        print('=======================')
        print(str(echo.generation) + '세대 유전자들')
        echo.next_generation()

        print(str(echo.generation - 1) + '세대 상위 유전자')
        count = 0
        for parent in echo.parents:
            if parent.score == MAXSCORE:
                count += 1
            print(parent.status, parent.score)

        print('=======================\n\n')