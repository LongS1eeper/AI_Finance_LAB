# 풀이
def solution(video_len, pos, op_start, op_end, commands):    
    def check(pos, end):
        if pos >= end:
            pos = end
        return pos

    video_len = int(video_len[:2] + video_len[3:])
    pos = int(pos[:2] + pos[3:])
    op_start = int(op_start[:2] + op_start[3:])
    op_end = int(op_end[:2] + op_end[3:])
    
    
    if (op_start <= pos) and (pos <= op_end):
        pos = op_end
    
    for com in commands:
        if com == 'next':
            pos = pos + 10
            if pos % 100 >= 60:
                pos = pos + 40    
            pos = check(pos, video_len) 
            if (op_start <= pos) and (pos <= op_end):
                pos = op_end
                
        elif com == 'prev':
            pos = pos - 10
            if pos < 0:
                pos = 0
            if pos % 100 >= 60:
                pos = pos - 40 
            if (op_start <= pos) and (pos <= op_end):
                pos = op_end
                
    pos = str(pos)
    if len(pos) == 4:
        pos = f"{pos[:2]}:{pos[2:]}"
    elif len(pos) == 3:
        pos = f"0{pos[0]}:{pos[1:]}"
    elif len(pos) == 2:
        pos = f"00:{pos}"
    elif len(pos) == 1:
        pos = f"00:0{pos}"
        
    return pos

# 해설
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)

    for command in commands:
        if op_start <= current_pos <= op_end:
            current_pos = op_end

        if command == "prev":
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            current_pos = min(video_len, current_pos + 10)

    # 마지막 명령 실행 후 한 번 더 오프닝 체크
    if op_start <= current_pos <= op_end:
        current_pos = op_end

    return seconds_to_time(current_pos)