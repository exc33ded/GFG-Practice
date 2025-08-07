class Solution:
    def time_to_seconds(self,time_sec):
        hh,mm,ss=time_sec.split(":")
        hh=int(hh)
        mm=int(mm)
        ss=int(ss)
        return hh*3600+mm*60+ss
    def minDifference(self, arr):
        time_list=[]
        for time in arr:
            time_list.append(self.time_to_seconds(time))
        time_list.sort()
        min_diff=float('inf')
        for  i in range(1,len(time_list)):
            min_diff=min(min_diff,time_list[i]-time_list[i-1])
        min_diff=min(min_diff,24*3600-time_list[-1]+time_list[0])
        return min_diff