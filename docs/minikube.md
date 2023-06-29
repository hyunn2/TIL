# minikube 실행해보기

1. minikube 설치

```
brew install minikube
```

2. 클러스터 시작하기

```
minikube start
```

3. 클러스터와 상호작용
```
# 모두 같게 실행

kubectl get po -A

kubectl get pod -A

kubectl get pods -A
```

```
# 브라우저 상으로 보기
minikube dashboard
```

4. 


5. 클러스터 관리
```
# 영향을 주지 않고 멈춤
minikube pause

# 푸쉬된 인스턴스 멈춘거 풀기
minikube unpause

# 클러스터 정지
minikube stop

# 기본 메모리 한계 변경(재시작 필요)
minikube config set memory 9001

# 쿠버네티스에 설치할 수 있거나 설치된 에드온 확인
minikkube addons list

# 두번째 클러스터 실행
minikube start -p aged --kubernetes-version=v1.16.1

# 클러스터에 있는 모든것 삭제
minikube delete --all
```


## 애드온 설치 및 제거
```
# 설치
minikube addons enable <name>

# 클러스터 시작하면서 애드온 추가
minikube start --addons <name1> --addons <name2>

# 
minikube addons open <name>

# 제거
minikube disable <name>
```

k8s에선 2가지 서비스가 있으며 minikube에도 가능하다.
- NodePort
- LoadBalancer

NodePort
외부 트래픽을 서비스로 가져오는 방법
포트를 열고 그 포트로 트래픽을 보내게 만든다.

```
minikube service <service-name> --url
```

tunnel : 로드밸런서 서비스에 연결

### NodePort 예시
1. deployment 생성
```
kubectl create deployment [만들 이름] --image=[이미지]
```

2. k8s service type 생성(NodePort)
```
kubectl expose deployment [노출시킬 디플로이먼트 이름] --type=NodePort --port=8080
```

3. NodePort 확인
```
kubectl get svc
```

5. 브라우저로 확인
```
minikube service [service 이름] --url
```


### LoadBalancer 예시
1. tunnel 실행
```
kubectl tunnel
```

2. deploy 생성
```
kubectl create deployment hello-minikube1 --image=kicbase/echo-server:1.0
```

3. service type을 로드밸런서로 설정
```
kubectl expose deployment hello-minikube1 --type=LoadBalancer --port=8080
```

4. external IP 확인
```
kubectl get svc
```

5. 실행해보기
```
위에서 본 external IP로 접속
```

## 애드온 정리
- Inspektor Gadget
디버깅 및 검사하는 도구 모음

- Cloud Spanner
관계형 데이터베이스이며, 비용이 들지 않고 테스트를 할 수 있음

- Headlamp
쿠버네티스 웹 UI

- Kong Ingress
minikube 서버 실행 컨트롤러

- Ingress DNS
minikube 서버에서 실행되는 컨트롤러를 위한 DNS 서비스

- GCP Auth
Google Cloud 서비스에 접근

- Custom Images



```shell
# minikube ip 확인
echo $(minikube ip)

# proxy 확인
echo -e "Starting Proxy. After starting it will not output a response. Please return to your original terminal window\n"; kubectl proxy

# pod name 환경변수화
export POD_NAME=$(kubectl get pods -o=go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')

# pod name 확인
echo Name of the Pod: $POD_NAME

# 애플리케이션 출력 확인
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME



# POD_NAME을 저렇게 안구하고 쉽게 할 수 있는 방법
kubectl get pod
위의 명령어를 통해 pod name 복사하면 된다.
```
