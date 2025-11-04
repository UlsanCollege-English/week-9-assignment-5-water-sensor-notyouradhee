[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DmnIIFUh)
# HW05 — Water Sensor: Streaming Median

**Story intro (new theme):**  
A **water quality sensor** sends a number each minute. You must output the **median after each reading** to smooth noise.

**Technical description**  
- **Input:** list `nums` of integers (stream order).  
- **Output:** list of floats/ints: median after each prefix.  
- **Rules:** If count is even, median is the **average** of the two middle values (as float).  
- **Expected complexity:** **Time** `O(n log n)` using **two heaps** (max-heap + min-heap); **Space** `O(n)`.

---

## Minimal prompts (you drive the 8 Steps)
- Decide what goes in each heap (`low` holds smaller half; `high` holds larger half).  
- Keep sizes balanced so `len(low) >= len(high)` and difference ≤ 1.  
- Median = top of `low` (odd) or average of tops (even).  
- Implement with `heapq` and negatives for the max-heap.

---

## Hints
- Push to one heap, then move one item to the other to keep order.  
- Rebalance if heaps differ in size by more than 1.  
- For even count, compute `(a + b) / 2.0`.

---

## How to run tests
python -m pytest -q


---

## FAQ
- **Q:** Float or int output? **A:** Use float when even; int when odd is fine.  
- **Q:** Negative numbers? **A:** Allowed.  
- **Q:** Duplicates? **A:** Allowed.  
- **Q:** stdin? **A:** No. Implement a function the tests call.  
- **Q:** Complexity? **A:** `O(n log n)` time, `O(n)` space.  
- **Q:** Reading failures? **A:** Compare your prefix medians to expected