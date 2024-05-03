"""
방금 그곡 서비스 조건
1) 음악 제목, 재생이 시작되고 끝난 시간, 악보 제공
2) 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
3) 각 음은 1분에 1개씩 재생, 반드시 처음부터 재생
4) 음악 길이보다 재생시간이 길면 처음부터 반복해서 재생, 짧으면 재생 시간만큼만 재생
5) 음악이 00:00 넘겨서까지 재생되는 일은 없음
6) 조건에 일치하는 음악이 여러개이면 재생된 시간이 가장 긴 음악 제목을 반환, 길이도 같으면 먼저 입력된 음악 제목을 반환
7) 없으면 None 반환

멜로디를 담은 문자열 m
방송된 곡의 정보 배열 musicinfos(,로 구분)

조건에 맞는 음악 제목을 return
"""

def solution(m, musicinfos):
    answer = '(None)ans'
    music_dict = {}
    new_m = []

    for i in m:
        if i == "#":
            new_m[-1] += i
            continue
        new_m.append(i)

    for musicinfo in musicinfos:
        lst = musicinfo.split(',')
        fh, fm = lst[1].split(":")
        sh, sm = lst[0].split(":")
        time = (int(fh)-int(sh)) * 60 + (int(fm)-int(sm))
        lyrics = []
        for i in lst[3]:
            if i == "#":
                lyrics[-1] += i
                continue
            lyrics.append(i)

        len_ly = time - len(lyrics)
        if len_ly > 0:
            for i in range(len_ly):
                lyrics.append(lyrics[i])

        elif len_ly < 0:
            lyrics = lyrics[:len_ly]

        if lst[2] not in music_dict:
            music_dict[lst[2]] = (time, lyrics)

    if len(new_m) == 0:
        return answer

    music_dict = sorted(music_dict.items(), key=lambda x:x[1][0], reverse=True)
    for i, j in music_dict:
        for k in range(len(j[1]) - len(new_m) + 1):
            if j[1][k:k+len(new_m)] == new_m:
                return i
    return answer


print(solution("ABCDEFG", 	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))