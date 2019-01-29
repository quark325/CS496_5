from gene import Genes as G
import random
import math


class Ecosystem:
    def __init__(self, option):
        self.generation = 0
        self.parent_count = option["parent_count"]
        self.gene_count = option["gene_count"]
        self.gene_length = option["gene_length"]
        self.mutation_probability = option["mutation_probability"]
        self.gene_list = self.initialize_gene()
        self.parents = []

    # 유전자 생성
    def initialize_gene(self):
        print("#######초기화를 시작합니다.#######")
        gene_list = []
        for i in range(self.gene_count):
            while True:
                temp = []
                # 리스트의 각 원소를 -10 ~ 10사이의 값으로 채운다.
                for _ in range(self.gene_length):
                    elem = random.uniform(-1.0, 1.0)*10
                    temp.append(elem)
                g = G(temp)
                print("초기 세대", i+1, "번 유전자", g.score, "점", g.status)
                gene_list.append(g)
                break
        return gene_list

    # 부모 유전자 parent_count 만큼 선택
    def who_parents(self):
        self.parents = []
        sort_list = sorted(self.gene_list, key=lambda x: x.score, reverse=True)

        for i in range(self.parent_count):
            self.parents.append(sort_list.pop(0))

    # 부모 유전자를 제외하고 제거함
    def none_parents_delete(self):
        # success_gene_count = 0
        self.gene_list = self.parents

    # 다음 세대
    def next_generation(self):
        self.match()
        self.who_parents()
        self.none_parents_delete()
        self.generation += 1

        total = 0
        for i in self.gene_list:
            total += i.score
        return total

    def show(self):
        for i in self.gene_list:
            print(i.status, i.score)

    # 상위 유전자 교배 TODO 우리는 list 니까 적절한 교배로 바꾼다.
    def match(self):
        # 부족한 수만큼 만들꺼다
        for o in range(len(self.gene_list)):
            print(self.generation+1, "번 세대", o + 1, "번 유전자", self.gene_list[o].score, "점",
                  self.gene_list[o].status)
        for o in range(len(self.gene_list), self.gene_count):
            temp = []
            for i in range(self.gene_length):
                mutation = random.random()
                # 돌연변이가 발생한다면 그 index 에는 아무값이나 넣는다.
                if mutation < self.mutation_probability:
                    temp.append(float(random.uniform(-1, 1)*10))

                # 돌연변이가 없다면 부모값중에 골라서 넣는다.
                else:
                    r = int(random.random() * self.parent_count)
                    temp.append(self.parents[r].status[i])
            g = G(temp)
            print(self.generation+1, "번 세대", o + 1, "번 유전자", g.score, "점", g.status)
            self.gene_list.append(g)
