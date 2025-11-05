"""
HW05 — Water Sensor: Streaming Median

Implement streaming_median(nums) -> list
"""

def streaming_median(nums):
    import heapq
    low = []
    high = []
    result = []
    for num in nums:
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        if len(low) > len(high):
            median = -low[0]
        else:
            median = (-low[0] + high[0]) / 2.0
        result.append(median)
    return result
