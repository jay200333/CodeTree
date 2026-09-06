secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class MeetingInfo:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

meeting_info = MeetingInfo(secret_code, meeting_point, time)

print(f"secret code : {meeting_info.code}")
print(f"meeting point : {meeting_info.point}")
print(f"time : {meeting_info.time}")