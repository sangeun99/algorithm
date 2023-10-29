# 탐색

## 깊이 우선 탐색 (DFS: Depth-first Search)

시작 노드에서 출발하여 탐색할 한 쪽 분기를 정하여 최대 길이까지 탐색을 마친 후 다른 쪽 분기로 이동하여 다시 탐색을 수행하는 알고리즘

### 특징

- 그래프 완전 탐색
- 재귀 함수로 구현
- Stack 자료구조 이용
- 시간복잡도: O(V + E)
  - V: 노드 수
  - E: 에지 수

### 핵심 이론

1. DFS를 시작할 노드를 정한 후 사용할 자료구조 (인접 리스트, 방문 배열, 스택) 초기화하기
![image](https://github.com/sangeun99/algorithm/assets/63828057/b8fd47af-4769-4a25-91ab-debf700e5aec)


2. 스택에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 스택에 삽입하기
![image](https://github.com/sangeun99/algorithm/assets/63828057/4b9b0280-241a-4a1e-b963-e5ea24f2f18d)

3. 스택 자료구조에 값이 없을 때까지 반복하기

## 너비 우선 탐색 (BFS: Breadth-first Search)

시작 노드에서 출발해 시작 노드를 기준으로 가까운 노드를 먼저 방문하면서 탐색하는 알고리즘

### 특징

- 그래프 완전 탐색
- Queue 자료구조 이용
- 시간복잡도: O(V + E)
  - V: 노드 수
  - E: 에지 수

### 핵심 이론

1. BFS를 시작할 노드를 정한 후 사용할 자료구조 (인접 리스트, 방문 배열, 큐) 초기화하기

![image](https://github.com/sangeun99/algorithm/assets/63828057/920f3d1d-5d60-46aa-bedb-8f1b79bcdb83)

2. 큐에서 노드를 꺼낸 후 꺼낸 노드의 인접 노드를 다시 큐에 삽입하기

![image](https://github.com/sangeun99/algorithm/assets/63828057/a7c76192-89f3-4117-8523-9771f82e21de)

3. 큐 자료구조에 값이 없을 때까지 반복하기

![image](https://github.com/sangeun99/algorithm/assets/63828057/b3620771-3e3c-4c14-8ec0-abb2ce2d2ae9)

## 이진 탐색

데이터가 정렬돼 있는 상태에서 원하는 값을 찾아내는 알고리즘. 대상 데이터의 중앙값과 찾고자 하는 값을 비교해 데이터의 크기를 절반씩 줄이면서 대상을 찾습니다.

### 특징

- 타깃 데이터 탐색
- 중앙값 비교를 통한 대상 축소 방식
- O(log N)

### 핵심 이론

오름차순으로 정렬된 데이터
1. 현재 데이터셋의 중앙값을 선택한다.
2. 중앙값 > 타깃 데이터일 때 중앙값 기준을 왼쪽 데이터셋을 선택한다.
3. 중앙값 < 타깃 데이터일 때 중앙값 기준으로 오른쪽 데이터셋을 선택한다.
4. 과정 1~3을 반복하다가 중앙값 == 타깃 데이터일 때 탐색을 종료한다.

![image](https://github.com/sangeun99/algorithm/assets/63828057/8497eec0-1fa5-4bb9-a0a1-f2b5fd0263fe)