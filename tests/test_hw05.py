import importlib.util, pathlib
import statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("main", ROOT/ "src" / "water_sensor.py")
main = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(main)
streaming_median = main.streaming_median

def ref_prefix_medians(nums):
    out = []
    cur = []
    for x in nums:
        cur.append(x)
        cur_sorted = sorted(cur)
        n = len(cur_sorted)
        if n % 2 == 1:
            out.append(cur_sorted[n//2])
        else:
            out.append((cur_sorted[n//2 - 1] + cur_sorted[n//2]) / 2.0)
    return out

# --- normal (4) ---
def test_simple_increasing():
    assert streaming_median([1,2,3]) == [1,1.5,2]

def test_mix_1():
    assert streaming_median([5,15,1,3]) == [5,10.0,5,4.0]

def test_even_odd_patterns():
    assert streaming_median([2,4,6,8,10]) == [2,3.0,4,5.0,6]

def test_single():
    assert streaming_median([10]) == [10]

# --- edge (3) ---
def test_empty():
    assert streaming_median([]) == []

def test_negatives():
    assert streaming_median([-1,-2,-3]) == [-1,-1.5,-2]

def test_duplicates():
    assert streaming_median([1,1,1,1]) == [1,1.0,1,1.0]

# --- complex (3) ---
def test_long_fixed():
    data = [9,1,3,7,2,6,5,4,8,0]
    assert streaming_median(data) == ref_prefix_medians(data)

def test_longer_sequence():
    data = [i%7 - 3 for i in range(20)]
    assert streaming_median(data) == ref_prefix_medians(data)

def test_spread_values():
    data = [100, -100, 50, -50, 0, 25, -25, 75, -75, 10]
    assert streaming_median(data) == ref_prefix_medians(data)
