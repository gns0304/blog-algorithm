# [10809] 알파벳 찾기

## 문제 분석

- 구현 문제이다.

## 해결 전략

- 알파벳 리스트 생성 시 string의 ascii_lowercase를 이용한다.

## 참고 사항

- string을 쓰지 않는다면 ```[chr(c) for c in range(ord('a'), ord('z') + 1)]```로도 만들 수 있을 것.