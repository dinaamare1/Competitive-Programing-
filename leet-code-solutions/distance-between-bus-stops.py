class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n=len(distance)
        distance=distance+distance
        begin=min(start,destination)
        end=max(start,destination)
        return min(sum(distance[end:begin+n]),sum(distance[begin:end]))
