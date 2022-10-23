# 유전 알고리즘을 이용한 그림그리기

##    OriginalㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤResult

<div align="">
  
  <a href="https://user-images.githubusercontent.com/105797125/197423130-867e5c2c-7f70-4b47-b04c-8a3f03db75f8.png">
    <img align="center" src="https://user-images.githubusercontent.com/105797125/197423130-867e5c2c-7f70-4b47-b04c-8a3f03db75f8.png" width="410" height="250"/>
  </a>
  <a href="https://user-images.githubusercontent.com/105797125/197423119-f45163cc-4401-471e-8608-40348e04712f.gif">
    <img align="center" src="https://user-images.githubusercontent.com/105797125/197423119-f45163cc-4401-471e-8608-40348e04712f.gif" width="400" height="250"/>
  </a>
</div>



##### 첫번째 유전자 개수
```python
first_genes = 50
```
##### 한 세대당 유전자 그룹의 숫자
```python
gene_groups = 50
```
##### 돌연변이 발생 확률
```python
mutation_occurrence = 0.01
```
##### 유전자 그룹의 원이 추가될 확률
```python
poaaciagg = 0.3 #probability of adding a circle in a gene group
```
##### 유전자 그룹의 원이 사라질 확률
```python
potdoaciagg = 0.2 #Probability of the disappearance of a circle in a gene group
```
##### 원의 크기
```python
circle_min, circle_max =  3, 10
```
##### 이미지 저장 주기
```python
image_storage_cycle = 100
```
##### 반지름, 센터, 색깔 초기화
```python
self.radius = random.randint(circle_min, circle_max)
self.center = np.array([random.randint(0, width), random.randint(0, height)])
self.color = np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
```
##### 변이의 크기, 평균 15 표준편차 4
```python
mutation_size = max(1, int(round(random.gauss(15, 4)))) / 100
```
##### 얼마만큼 원본 이미지의 가까운지 확인
```python
out = np.ones((height, width, channels), dtype=np.uint8) * 255
```
##### 유전자의 값을 원으로 그림
```python
for gene in genome:
  cv2.circle(out, center=tuple(gene.center), radius=gene.radius, color=(int(gene.color[0]), int(gene.color[1]), int(gene.color[2])), thickness=-1)
```
##### 두 이미지의 차이
```python
fitness = 255. / compare_mse(img, out)
return fitness, out
```
##### 유전자를 한꺼번에 돌연변이로 만듬
def compute_population(g):
  genome = deepcopy(g)
```  
##### 유전자의 개수에 따라 변이를 바꿔줌
```python
if len(genome) < 200:
  for gene in genome:
    if random.uniform(0, 1) < prob_mutation:
      gene.mutate()
else:
  for gene in random.sample(genome, k=int(len(genome) * prob_mutation)):
    gene.mutate()
```
##### 유전자 추가
```python
if random.uniform(0, 1)<poaaciagg:
    genome.append(Gene())
```
##### 유전자 삭제
```python
if len(genome)>0 and random.uniform(0, 1)<potdoaciagg:
    genome.remove(random.choice(genome))
```    
##### 새로운 유전자 점수 측정
```python
new_fitness, new_out = compute_fitness(genome)
  return new_fitness, genome, new_out
```    
