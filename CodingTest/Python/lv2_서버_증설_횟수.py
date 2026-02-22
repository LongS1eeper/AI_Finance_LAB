def solution(players, m, k):
    answer = 0  # 하루 동안 "서버를 새로 증설한 횟수" 누적(최종 출력값)

    # servers[t] = t시각에 '운영 중인(이미 켜져 있는) 증설 서버 대수'
    # (과거에 증설해 k시간 유지 중인 서버들이 시간대별로 누적되어 기록됨)
    servers = [0] * 24

    # 0시~23시까지 시간 순서대로 확인
    for i, player in enumerate(players):
        # 해당 시간에 필요한 서버 대수:
        # "이용자 수가 m명 늘 때마다 서버 1대 필요" → (player // m) 대
        # 예) m=3이면 player=0~2 → 0대, 3~5 → 1대, 6~8 → 2대 ...
        servers_required = player // m

        # 현재 시간 i에 이미 운영 중인 서버(이전 시간에 증설해 아직 유지되는 서버 포함)
        servers_now = servers[i]

        # 현재 운영 서버가 부족하면, 부족한 만큼만 '추가 증설'
        if servers_now < servers_required:
            # 지금 시간에 새로 추가해야 할 서버 수
            servers_added = servers_required - servers_now

            # 증설 횟수 누적(서버를 servers_added대 "새로 켠" 것이므로 그만큼 더함)
            answer += servers_added

            # 새로 켠 서버는 "지금 시간 i부터 k시간 동안" 유지됨
            # 즉, i, i+1, ..., i+k-1 시간대에 서버가 돌아가고 있어야 함
            # 단, 하루는 24시간(0~23)만 있으니 24를 넘지 않게 min 처리
            for j in range(i, min(i + k, 24)):
                # j시각의 운영 서버 수에 이번에 추가한 서버 수만큼 누적
                servers[j] += servers_added

        # (부족하지 않으면 아무 것도 안 함: 기존 서버로 커버 가능)

    # 하루 동안의 총 증설 횟수 반환
    return answer