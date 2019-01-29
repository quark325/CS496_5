import random
import time
import pygame
import sys
import math
import copy
import numpy
import matplotlib.pyplot as plt
import pygame.locals as keys
import numpy as np
import tensorflow as tf
import run_game
from echo import Ecosystem as Echo

if __name__ == '__main__':
    pygame.init()
    run_game.FPSCLOCK = pygame.time.Clock()
    run_game.DISPLAYSURF = pygame.display.set_mode((run_game.WINDOWWIDTH, run_game.WINDOWHEIGHT))
    run_game.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    run_game.BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Tetromino')

    run_game.show_text_screen('Tetromino')
    games_completed = 0
    scoreArray = []
    weight0Array = []
    weight1Array = []
    weight2Array = []
    weight3Array = []
    game_index_array = []

    x = tf.placeholder('float', name='X')
    y = tf.placeholder('float', name='Y')

    addition = tf.add(x, y, name='add')

    # Trial2 가 텐서보드에 뜨는 태그 -> 실행 할 때 마다 바꾸면 좋음
    tf.summary.scalar('Tetris_v2.0', addition)
    summary_op = tf.summary.merge_all()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # 저장경로
        writer = tf.summary.FileWriter('./tetris_logs', sess.graph)

        option = {
            "parent_count": 5,
            "gene_count": 50,
            "gene_length": 6,
            "mutation_probability": 0.05
        }
        echo = Echo(option)
        generation_limit = 100

        while True:
            print('=======================')
            print(str(echo.generation) + '세대 유전자들')
            #parameter로 들어간게 점수임
            total = echo.next_generation()

            print(str(echo.generation) + '세대 상위 유전자')
            score_avg = total / option["parent_count"]
            for parent in echo.parents:
                print(parent.status, parent.score)

            # 앞에서 define 한 변수들에게 값을 씌워줌
            var1 = np.float64(0);
            var2 = np.float64(score_avg);

            add, s_ = sess.run([addition, summary_op], feed_dict={x: var1, y: var2})
            writer.add_summary(s_, echo.generation+1)

            run_game.show_text_screen('Game Over')

            if echo.generation >= generation_limit:
                print('=======================')
                print('Generic algorithm End')
                break