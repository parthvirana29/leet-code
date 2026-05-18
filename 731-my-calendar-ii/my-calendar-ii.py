class MyCalendarTwo:
    def __init__(self):
        self.single_booked = []
        self.double_booked = []
    
    def get_overlap(self, start1, end1, start2 ,end2):
        overlap_start = max(start1,start2)
        overlap_end = min(end1, end2)
        if (overlap_start < overlap_end):
            return (overlap_start,overlap_end)

        return None

    def book(self, startTime: int, endTime: int) -> bool:
        for db_start, db_end in self.double_booked:
            if startTime < db_end and endTime > db_start:
                return False
        for sb_start, sb_end in self.single_booked:
            overlap = self.get_overlap(startTime, endTime, sb_start,sb_end)
            if overlap:
                self.double_booked.append(overlap)
        self.single_booked.append((startTime, endTime))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)