# Kubernetes

컨테이너를 오케스트레이션하는 도구

<br>

## 쿠버네티스를 사용하는 이유

Container health checks, Automatic re-deployment
Autoscaling
Load balancer
Management

쿠버네티스의 경우 위의 각각의 기능들을 독립적으로 정의할 수 있음! 

클라우드 프로바이더에 상관없이 사용 가능하며, 추가 구성이 필요한 경우 병합 가능


<br>

**용어 정리**

Pod:

가장 작고 단순한 쿠버네티스 오브젝트, 사용자 클러스터에서 동작하는 컨테이너 집합

<br>

deployment:

로컬 상태가 없는 파드를 실행하여 복제된 애플리케이션을 관리하는 API 오브젝트

<br>
Ingress: 

HTTP와 같이 클러스터 안에 서비스들를 접근하고 관리하기 위한 API 오브젝트

<br>

Service:

Pod 집합에서 실행중인 애플리케이션을 네트워크 서비스로 노출하는 추상화 방법

<br>

## 간단한 튜토리얼

애플리케이션을 minikube에 배포

배포한 애플리케이션 실행

애플리케이션의 로그 확인
<br>
쿠버네티스 환경을 볼 수 있는 방법으론 2가지가 있는데,

첫번째, 터미널에서 보는 방법과

두번재, 브라우저에서 보는 방법이 있다.

<br>

0. minikube 실행

```
minikube start
```

<br>

1. 쿠버네티스 대시보드(dashboard) 열기

**터미널에서 보는 방법**
```
minikube dashboard --url
```
이 명령은 대시보드 애드온과 프록시가 활성화된다.
- 옵션 : url (자동으로 웹 브라우저를 열리지 않고 대시보드 접속 url만 출력함)

<br>

**브라우저에서 보는 방법**

```
Select port to view on Host 1 클릭
port : 30000입력
```


<br>

2. 디플로이먼트(deployment) 만들기
```
kubectl create deployment <이름> <이미지> <포트번호>
```

- 디플로이먼트(deployment) 확인
```
kubectl get deployments
```

- 파드(pods) 보기
```
kubectl get pods
```

- 클러스터 이벤트 보기
```
kubectl get events
```

- 환경설정 보기
```
kubectl config view
```

<br>

3. 서비스 만들기


4. 애드온 사용하기 


5. 제거하기
```
kubectl delete service <서비스 이름>
kubectl delete deployment <디플로이먼트 이름>

# 가상 머신 정지
minikube stop

# 가상 머신 삭제
minikube delete
```


## 쿠버네티스 기초 모듈

1. 쿠버네티스 클러스터 생성
2. 애플리케이션 배포
3. 앱 조사
4. 앱 외부로 노출
5. 애플리케이션 스케일링
6. 앱 업데이트
