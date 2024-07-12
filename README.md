# istio-retry-test
Testing Istio Retry Logic with Python Apps

## sample diagram
![istio-retry-diagram](https://github.com/user-attachments/assets/8d891383-3a67-4360-bd6a-e6eba963d745)

## testing option
<img width="1122" alt="Screenshot 2024-07-12 at 18 07 49" src="https://github.com/user-attachments/assets/4c724cf4-63fb-4e76-8d6d-241782dc5657">

## deploy service-a
```sh
cd service-a
kubectl apply -f .
```

## deploy service-b
```sh
cd service-b
kubectl apply -f
```

## expose service-a
```sh
kubectl port-forward svc/service-a 5000:5000
```
