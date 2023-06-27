# Kubernetes

컨테이너를 오케스트레이션하는 도구

- 자동 배포
- 스케일링
- 로드밸런싱

<br>

## 쿠버네티스를 사용하는 이유

Container health checks, Automatic re-deployment
Autoscaling
Load balancer
Management

쿠버네티스의 경우 위의 각각의 기능들을 독립적으로 정의할 수 있음!

클라우드 프로바이더에 상관없이 사용 가능하며, 추가 구성이 필요한 경우 병합 가능
ex) AWS를 사용할 경우 AWS 서비스에서만 사용 가능(AWS에서 정의한대로 모든 것을 구성해야하기 때문에)
 



<br>


## 쿠버네티스 구성 요소

- Cluster : 배포 혹은 원하는 최종상태를 구성하는 컬렉션 세트
- Nodes : 하나 또는 여러개의 포드를 호스팅하며, 클러스터와 통신하거나 클러스터 내에서 통신하는 물리적 머신 또는 가상 머신
  포드를 호스팅하는 실제 머신이며 앱 컨테이너와 컨테이너의 필요한 리소스를 실행함
  - Master Node : 포드를 관리하는 컨트롤 플레인을 가지고 있음
  - Worker Node : 
- Pods : 컨테이너를 시작하여 그 컨테이너를 관리한다.
- Containers : 
- Services : 고유한 포드 및 컨테이너의 독립적인 IP 주소를 가진 포드 그룹, 포드에 접근하고 
  - IP 주소
  - 




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

+

Deployment:



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
