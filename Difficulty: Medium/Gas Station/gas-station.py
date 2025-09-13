class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        total_gas, total_cost = sum(gas), sum(cost)
        
        # If not enough gas overall, impossible
        if total_gas < total_cost:
            return -1
        
        start, tank = 0, 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Reset start position
                start = i + 1
                tank = 0
        
        return start