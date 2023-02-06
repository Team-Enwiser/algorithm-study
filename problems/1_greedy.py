'''
[문제1] 1이 될 때까지 

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.

1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.

예를 들어 N이 17, K가 4라고 가정합시다. 이때 1번의 과정을 한 번 수행하면 N은 16이 됩니다.
이후에 2번의 과정을 두 번 수행하면 N은 1이 됩니다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다.
이는 N을 1로 만드는 최소 횟수 입니다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요.

- 입력 조건: 첫째 줄에 N(1<=N<=100000)과 K(2<=K<=100000)가 공백을 기준으로 하여 각각 자연수로 주어집니다.
- 출력 조건: 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다.


[입력 예시]
25 5

[출력 예시]
2




[문제 2] 곱하기 혹은 더하기

각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합시다.

예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0+2)x9)x8)x4) = 576입니다.
또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.


- 입력 조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1<=S의 길이<=20)
- 출력 조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.

[입력 예시]
02984

[출력 예시]
576

[입력 예시]
567

[출력 예시]
210




[문제3] 모험가 길드

예를 들어 N=5이고, 각 모험가의 공포도가 다음과 같다고 가정합시다.
2 3 1 2 2
이 경우 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게되면 총 2개의 그룹을 만들 수 있습니다.
또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

- 입력 조건: 첫째 줄에 모험가 수 N이 주어집니다.(1<=N<=100000)
           둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

- 출력 조건: 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

[입력 예시]
5
2 3 1 2 2

[출력 예시]
2
'''