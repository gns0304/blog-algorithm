# [5598] シーザー暗号

## 문제 분석
- 큰 어려움 없는 구현 문제이다.
- 카이사르 암호 문제이다.
- ASCII 코드를 이용하는 문제로 생각되나 매칭 패턴이 간단하므로 리스트나 딕셔너리로 풀 수도 있을 것으로 보인다.

## 해결 전략

- 최대한 Pythonic하게 풀어보기 위하여 List Comprehension을 이용한다.
- if문도 in-line 처리한다.
- ASCII 코드로 변환해주는 ord()와 문자로 변환하는 chr() 함수를 이용한다.

## 참고 사항

- [ASCII]("https://ko.wikipedia.org/wiki/ASCII")