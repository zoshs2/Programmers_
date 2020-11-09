'''
< 문제 설명 >
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
'''

'''
< 제한 사항 >
1. 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
2. completion의 길이는 participant의 길이보다 1 작습니다.
3. 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
4. 참가자 중에는 동명이인이 있을 수 있습니다.
'''

'''
< 입출력 예시 >
-> Participants(참가자) / Completion(완주자) / return (완주하지 못한 사람)
["leo", "kiki", "eden"]	/ ["eden", "kiki"] / leo
["marina", "josipa", "nikola", "vinko", "filipa"] / ["josipa", "filipa", "marina", "nikola"] / vinko
["mislav", "stanko", "mislav", "ana"] / ["stanko", "ana", "mislav"]	/ mislav
'''

'''
< 입출력 예 설명 >
1. 예제 #1 : leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
2. 예제 #2 : vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
3. 예제 #3 : mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
'''

# 내가 풀어본 문제. 해시를 완전히 활용한 형태는 아니지만, 결국 해시도 키-값(데이터)인 측면에서는 딕셔너리를 잘 활용한...? 흠ㅋ
def solution(participant, completion):
    hash = {}
    for part in participant:
        if part in hash:
            hash[part] += 1
        else:
            hash[part] = 1
    
    for comp in completion:
        if hash[comp] == 1:
            del hash[comp]
        else:
            hash[comp] -= 1

    answer = list(hash.keys())[0]
    return answer

# 결과 : 테스트 데이터 3/3 & 채점 데이터 10/10

# 다른 사람들 풀이를 보자.
## 1. 가장 좋아요 많았던 풀이
import collections

def solution_1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
# -> 초대박 간결한 모습...
# 몰랐는데, collections의 .Counter메소드는 입력을 분석해서 요소별 갯수를 카운트해준다. 그것도 딕셔너리 형태로.
# 예컨대, list_1 = ["Yungi", "Yungi", "Sungjae","Hyuna"] 이런 데이터가 들어오면
# collections.Counter(list_1) 은 {"Yungi":2, "Sungjae":1, "Hyuna":1} 이렇게 반환한다.
# 더욱 놀라운 건 이들끼리 연산도 된다는 점. 어떤식으로 되냐면 같은 '키'끼리 대응시켜서 '값'들을 연산한다. 홀리쎗


## 2. 가감을 이용한 풀이
# 이것도 재밌고 기발한 풀이라고 생각한다.
def solution_2(participant, completion):
    answer = None
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part # hash()라는 BIF를 써줬음. 해당 입력에 대한 해쉬값을 생성해주는 함수
        temp += int(hash(part)) # 그리고 모든 참가자 이름에 대한 해쉬값들을 temp에다가 누적시킴
    
    for com in completion:
        temp -= int(hash(com)) # 그리고 완주자 이름들의 해쉬값을 누적했던 temp에서 하나씩 빼준다. 
    
    answer = dict[temp] # 결국 빼다가 남은 temp값이 완주하지 못한 이에 대한 해쉬값일 것이다. (미완주자가 '한명'이라는 전제가 이미 문제에 있었다.)
    return answer
# Good !

