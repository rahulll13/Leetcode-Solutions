class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans=-1
        dis=float('inf')
        for i,(x,y,r) in enumerate(drones):
            diff=abs(x-target[0]) + abs(target[1]-y)
            if diff<=r and diff<dis:
                ans=i
                dis=diff
        return ans