# 풀이

def solution(schedules, timelogs, startday):
    
    cnt = 0
    for idx, val in enumerate(timelogs):
        
        # 제한시간 설정
        deadline = schedules[idx]
        
        if deadline%100 + 10 >= 60:
            deadline = deadline + 100 - 50
        else: deadline = deadline + 10
        
        day = startday
        
        # 지각인지 확인
        for time in val:
            if (day % 7 == 6) or (day % 7 == 0):
                day += 1
                continue
                
            if deadline - time < 0 :
                cnt += 1
                break
                
            day += 1
            
    return idx - cnt + 1


# 해설

def solution(schedules, timelogs, startday):
    # 하루를 나타내는 요일 정보를 계산하기 위한 헬퍼 함수
    # 1(월), 2(화), 3(수), 4(목), 5(금), 6(토), 7(일)
    def day_of_week(start, offset):
        return (start + offset - 1) % 7 + 1

    # 시각(예: 958)과 분(예: 10)을 더해주는 헬퍼 함수
    # 시각은 HHMM 형태로 들어오며, 958은 09:58을 의미
    def add_minutes(time, plus):
        hour = time // 100
        minute = time % 100
        total_minutes = hour * 60 + minute + plus

        new_hour = total_minutes // 60
        new_minute = total_minutes % 60
        return new_hour * 100 + new_minute

    n = len(schedules)         # 직원 수
    answer = 0                 # 상품을 받을 직원 수

    for i in range(n):
        desired_time = schedules[i]
        # '지각 판정 기준 시각' = 희망 시각 + 10분
        deadline = add_minutes(desired_time, 10)

        # 7일간 모든 평일에 대해 지각이 없었는지 확인
        ontime_for_all_weekdays = True
        for day_idx in range(7):
            # 오늘이 무슨 요일인지 계산
            wday = day_of_week(startday, day_idx)  # 1 ~ 7

            # 토/일(6, 7)은 이벤트에 영향을 주지 않으므로 무시
            if wday in [6, 7]:
                continue

            # 평일(월~금)인 경우만 지각 판정 확인
            if timelogs[i][day_idx] > deadline:
                ontime_for_all_weekdays = False
                break

        if ontime_for_all_weekdays:
            answer += 1

    return answer