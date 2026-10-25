class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        daysPerMonth=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        aM=int(arriveAlice[:2])-1
        bM=int(leaveAlice[:2])-1
        cM=int(arriveBob[:2])-1
        dM=int(leaveBob[:2])-1
        aD=int(arriveAlice[-2:])
        bD=int(leaveAlice[-2:])
        cD=int(arriveBob[-2:])
        dD=int(leaveBob[-2:])
        daysA=sum(daysPerMonth[:aM])+aD
        daysB=sum(daysPerMonth[:bM])+bD
        daysC=sum(daysPerMonth[:cM])+cD
        daysD=sum(daysPerMonth[:dM])+dD
        if daysA<daysC and daysC>daysB:
            return 0
        if daysA>daysC and daysD<daysA:
            return 0
        return abs(max(daysA,daysC)-min(daysB,daysD))+1