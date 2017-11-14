"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...],
find the minimum number of meeting rooms required.
"""
from heapq import heapreplace, heappush
class meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def meetingRoomII(meetings):
    """
    :type nums: List[meeting]
    :rtype: int
    """
    meetings.sort(key = lambda x: x.start)
    heap = []
    for meeting in meetings:
        if heap and meeting.start >= heap[0]:
            heapreplace(heap, meeting.end)
        else:
            heappush(heap, meeting.end)
    return len(heap)

# Testing
a = meeting(1,3)
b = meeting(3,4)
c = meeting(4,7)
meetings = [a,b,c]
print (meetingRoomII(meetings))
