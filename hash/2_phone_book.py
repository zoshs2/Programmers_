'''
< 문제 설명 > 
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''

'''
< 제한 사항 >
1. phone_book의 길이는 1 이상 1,000,000 이하입니다.
2. 각 전화번호의 길이는 1 이상 20 이하입니다.
'''

'''
< 입출력 예제 >
입력(phone_book) / 출력 
["119", "97674223", "1195524421"] / false
["123","456","789"] / true
["12","123","1235","567","88"] / false
'''

'''
< 입출력 예 설명 >
1. 입출력 예 #1
앞에서 설명한 예와 같습니다.
2. 입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.
3. 입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.
'''

# 해시(Hash)는 아니지만 리스트로 풀어봄.
def solution(phone_book):
    temp = []
    phone_book = sorted(phone_book, key=len)
    for i, phone in enumerate(phone_book):
        for j in range(len(phone)):
            temp.append(phone[:j+1])
        # print(temp)
        if i+1 == len(phone_book):
            return True
        
        for k in range(i+1, len(phone_book)):
            length = len(phone_book[k])
            for prefix in temp[1:]:
                # print(prefix)
                if prefix == phone_book[k][:len(prefix)]:
                    return False
                
        
        temp = []
        
    answer = True
    return answer

# 결과 -> 테스트 입력데이터에서는 모두 통과함. 하지만, 채점데이터에서는 13개 중 2개를 틀림.. 이유는 아직까지 모르겠음 ㅜ 왜지;; 이번엔 해쉬로 한번 풀어보자.
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))