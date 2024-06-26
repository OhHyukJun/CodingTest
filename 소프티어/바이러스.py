'''
1초당 P배 증가하는 바이러스
K마리가 있었다면 N초 후에는 몇 마리의 바이러스로?
N초 동안 죽는 바이러스는 없음
10000000007
K + K*P
(K + K*P)*P
'''
import sys

K,P,N = map(int,sys.stdin.readline().split())
a = K*pow(P,N,1000000007)

print(a%1000000007)