# [10828] 스택

## 문제 분석

- 간단하게 스택을 구현하면 되는 것으로 보인다.

## 해결 전략

- 드디어 나타난 시간 초과 상황. 아래의 표준입출력함수를 사용해보자.

``` python
import sys
input = sys.stdin.readline


def print(src):
    sys.stdout.write(str(src) + '\n')
```

## 참고 사항

- [표준 스트림](https://ko.wikipedia.org/wiki/%ED%91%9C%EC%A4%80_%EC%8A%A4%ED%8A%B8%EB%A6%BC)