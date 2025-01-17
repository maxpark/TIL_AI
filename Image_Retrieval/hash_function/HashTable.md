## Hash 알고리즘

### 해쉬란?

임의의 크기를 가진 데이터를 고정된 데이터의 크기로 변환시키는 것을 말한다.

**즉 해쉬 알고리즘은 해쉬를 하는 방법에 대해 절차적으로 명세한다.**



이를 이용해서 특정한 배열의 인덱스나 위치나 위치를 입력하고자 하는 데이터의 값을 이용해 저장하거나 찾을 수 있다. 기존에 사용했던 자료 구조들은 탐색이나 삽입에 선형시간이 걸리기도 했던 것에 비해, 해쉬를 이용하면 즉시 저장하거나 찾고자 하는 위치를 참조할 수 있으므로 더욱 빠른 속도로 처리할 수 있다.



### 1. Direct Addressing Table

![img](https://t1.daumcdn.net/cfile/tistory/2714953C570C9A8D0F)

* Direct Addressing Table은 Key-value 쌍의 데이터를 배열에 저장할 , key값을 직접적으로 배열의 인덱스로 사용하는 방법이다. 
* 예를 들면 키 값이 400인 데이터가 있다면, 이는 배열의 인덱스가 400인 위치에 키 값을 저장하고 포인터로 데이터를 연결한다. 
* 똑같은 키 값이 존재하지 않는다고 가정하면, 삽입 시에는 , 각 키마다 자신의 공간이 존재하므로 그 위치에다 저장을 하면 되고, 삭제 시에는 해당 키의 위치에 NULL값을 넣어주면 된다. 

**장점**: 찾고자 하는 데이터의 key만 알고있으면 즉시 위치를 찾는 것이 가능하므로 탐색, 저장, 삭제, 갱신은 모두 선형시간인 0(1)로 매우 빠르게 처리가 가능하다. 

**단점** : 다만 key값의 최대 크기만큼 배열이 할당되기 때문에, 크기는 매우 큰데, 저장하고자 하는 데이터가 적다면 공간을 많이 낭비할 수 있다는 단점이 있다.



### 2. Hash Table

![img](https://t1.daumcdn.net/cfile/tistory/21565B36570C9C560F)

* Hash Table은 key-value 쌍에서 key값을 테이블에 저장할 때, Direct Addressing Table과 달리 key값을 함수를 이용해 계산을 수행한 후, 그 결과값을 배열의 인덱스로 사용하여 저장하는 방식이다. 여기서 Key 값을 계산하는 함수는 **해쉬 함수(Hash Function)**이라고 부른다.

* 해쉬 함수는 입력으로 key를 받아, 0부터 배열의 크기 -1 사이의 값을 출력한다. 해쉬에 대한 첫 정의대로 임의의 숫자를 배열의 크기만큼으로 변환시킨 것이다. 이 경우 k값이 h(k)로 해쉬되었다고 하며, h(k)는 k의 해쉬값이라고 한다.
* 위 그림에서 각 k값들의 해쉬값인 h(k)값들은 배열의 인덱스로 사용되고 있음.

**장점** : 해쉬 테이블은 Direct Addressing Table에 비해 공간 낭비가 매우 적은데 이는 Key값의 크기에 테이블의 크기가 좌우되는 것이 아니고, h(k)만큼의 공간에 저장되기 때문이다.

**단점** : 충돌이 일어날 수 있다. 다른 k값이 동일한 h(k)값을 가져 동일한 slot에 저장되는 경우를 말한다.

예를 들자면 k1과 k12를 해쉬하였더니 h(k1)= h(k12)인 경우를 들 수 있다. Direct Addressing Table에서는 이를 방지하기 위해 key값이 다르다고 전제하였지만 해쉬 테이블에서는 key 값이 달라도 해쉬의 결과가 같을 수 있기 때문에 이를 방지하기 위한 방법이 필요하다. 



**Hash에서 충돌을 최소화 하는 방법 4가지**

1. **Chaining 방법** - 충돌을 허용하되 최소화 하는 방법 중 하나로서 데이터들을 포인터를 이용해 서로 체인형태로 엮어 나가는 것을 뜻하며, 해쉬 테이블에선 동일한 해쉬값이 출력되 충돌이 일어나면, 그 위치에 있던 데이터에 key값을 포인터로 뒤이어 연결한다. Chaining 방법에서의 수행시간은 삽입 시에는 해쉬값을 이용해 바로 slot에 저장하면 되므로 상수시간에 일어나고, 삭제는 연결리스트의 삭제와 동일하게 상수시간에, 탐색 시에는 연결리스트를 따라 가기 때문에 리스트의 길이 만큼 발생하지만, 최악의 경우, 즉 모든 데이터의 해쉬값이 일치하여 한 인덱스에 저장되었을 경우에는 연결리스트의 탐색 시간과 동일한 선형시간을 갖게 된다.
2. **적재률** - 극단 적인 예로, 평균적으로 O(a+1)의 시간이 걸린다. a는 적재율을 뜻하며 적재율이란 현재 저장된 key값 갯수(K), 전체 테이블의 갯수(N)을 서로 나눈 값(K/N)이다. 즉 현재 저장된 데이터가 많으면 많아질 수록 충돌 확률이 높아져 연결 리스트 탐색 확률도 증가하며 적을수록 리스트 탐색 확률이 적어진다는 것이다. 
3. **Simple uniform hash** - 충돌을 최소화 하는 방법 중에 충돌이 적은 좋은 해쉬 함수를 만드는 방법도 있다. 좋은 해쉬 함수의 조건은 Simple uniform hash 함수를 만드는 것으로 이조건은 다음과 같다. 
   1. 계산된 해쉬값들은 0부터 배열의 크기가 -1 사이의 범위를 '동일한 확률'로 골고루 나타날 것
   2. 각각의 해쉬값들은 서로 연관성을 가지지 않고 독립적으로 생선된다.
4. **division method**