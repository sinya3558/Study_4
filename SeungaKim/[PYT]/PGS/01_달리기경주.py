# 01_달리기경주.py

def solution(players, callings):    # players: str list, callings : str list
    try:
        # 제한 사항
        if not 5 <= len(players) <= 50000:
            raise ValueError("invalid input size of 'players'")
        # 2 ≤ callings의 길이 ≤ 1,000,000
        if not 2 <= len(callings) <= 1000000:
            raise ValueError("invalid input size of 'calling'")
        
        # dictionary
        p_dict = {}
        for idx, runner in enumerate(players):
            p_dict[runner] = idx
            # print(p_dict)
        
        # 다시 이름 확인
        for name in callings:
            # 이름 찾았으면, 순서 -1

            # 바꿀 데이터 저장
            idx = p_dict[name]  # players 랑 p_dict 이랑 동일해서 괜춘
            prev_name = players[idx - 1]

            # 1. dict 순서 업데이트
            ## 잉? 테스트 fail 함
            # p_dict[name] = idx - 1
            # p_dict[prev_name] = idx

            # 2. player list 순서 업데이트
            players[idx], players[idx - 1] = players[idx - 1], players[idx]

            # 3. 
            p_dict[name] = idx - 1
            p_dict[prev_name] = idx

        answer = players
        return answer

    except Exception as e:
        print(e)