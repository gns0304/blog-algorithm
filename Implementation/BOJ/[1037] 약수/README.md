# [1037] 약수

## 문제 분석

- 구현 문제이다. 정수론을 안다면 푸는 게 살짝 쉬워지는 정도.
- 진짜 약수는 자기 자신을 제외한 약수를 의미하는 것으로 보인다.

## 해결 전략

- 이때 구하려는 N은 모든 진짜 약수가 주어지니 약수의 최대와 최소를 곱하면 되겠다.

## 참고 사항

- map()은 반복 가능한 요소를 지정된 함수로 처리해주는 함수다.
- 2번째 라인은 ```nums = [*map(int, input().split(" "))]```으로 표현될 수도 있다.
- *은 map을 unpacking한다.