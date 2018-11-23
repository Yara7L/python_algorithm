# _*_ coding:utf-8 _*_

import numpy as np
import math

infinite = float(-2.0 ** 31)  # 负无穷


# 对pi，A，B结果取对数，因为单个数值太小，会溢出
def log_val(data):
    # 遍历矩阵每一行，每一行概率相加为1，做取对数处理
    col_len = data.shape[1]
    for k, line in enumerate(data):
        sum1 = np.sum(line)
        log_sum = math.log(sum1)
        for i in range(col_len):
            if data[k][i] == 0:
                data[k][i] = infinite
            else:
                data[k][i] = math.log(data[k][i]) - log_sum
    return data


def viterbi(A, B, PI, O):
    """
    :param A: 状态转移矩阵
    :param B: 发射矩阵
    :param PI: 初始化状态
    :param O: 观测序列
    :return: I 最优路径  P 最大概率
    """
    A = log_val(A)
    B = log_val(B)

    # 取对数
    sum1 = np.sum(PI)
    for i in range(len(PI)):
        PI[i] = math.log(PI[i] / sum1)

    T = np.shape(O)[0]
    # T时间，对应观测的序列顺序
    N, K = np.shape(B)
    # N,K，发射矩阵（隐藏状态的N个取值，观测变量的K个可能取值）
    I = np.array([np.nan] * T)
    delta = np.zeros((T, N))
    # 保存计算过的所有δ
    # 保存所有状态的最大值是由哪一个状态产生的，δ[t](i)时，是由哪一个δ[t-1](q)产生的，q就是哪个状态
    phi = np.zeros((T, N))
    # 初始化最优的P(i,O1)=max{P(O1|I)*p(I)}
    for i in range(N):
        delta[0, i] = PI[i] + B[i, O[0]]
        phi[0, 1] = 0
    for t in range(1, T):
        for i in range(N):
            delta[t][i] = delta[t - 1][0] + A[0][i]
            #  寻找最大的δ[t](i)
            for j in range(1, N):
                current = delta[t - 1][j] + A[j][i]
                if current > delta[t][i]:
                    delta[t][i] = current
                    # 保存当前的δ[t](i)取最大值，是从哪一个j状态来的
                    phi[t][i] = j
            delta[t][i] += B[i, O[t]]

    P = np.max(delta[-1, :])
    I[-1] = np.where(delta[-1, :] == P)[0][0]
    P = np.exp(P)
    print(P)
    for t in range(T - 2, -1, -1):
        I[t] = phi[t + 1][int(I[t + 1])]
    return P, I


if __name__ == "__main__":
    A = np.array([[0.5, 0.2, 0.3],
                  [0.3, 0.5, 0.2],
                  [0.2, 0.3, 0.5]])
    B = np.array([[0.5, 0.5],
                  [0.4, 0.6],
                  [0.7, 0.3]])
    PI = np.array([0.2, 0.4, 0.4])
    O = np.array([0, 1, 0])
    T = np.shape(O)[0]
    N, K = np.shape(B)
    P, I = viterbi(A, B, PI, O)
    print('最优路径：')
    print(I)
    print('该最优路径的概率：')
    print(P)
