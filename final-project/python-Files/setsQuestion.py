class SetOperations:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def union(self):
       # Return the union of sets A and B
       # hint use set union
       pass

    def intersection(self):
        # Return the intersection of sets A and B
        # hint use set intersection
        pass

    def symmetric_difference(self):
        # Return the symmetric difference of sets A and B
       pass

    def is_subset(self):
      # Check if set A is a subset of set B
      pass
    def is_proper_subset(self):
         # Check if set A is a proper subset of set B
        pass


def run_test_case(A, B, expected_union, expected_intersection, expected_symmetric_difference, expected_subset, expected_proper_subset):
    set_ops = SetOperations(A, B)
    union_set = set_ops.union()
    intersection_set = set_ops.intersection()
    symmetric_difference_set = set_ops.symmetric_difference()
    is_subset = set_ops.is_subset()
    is_proper_subset = set_ops.is_proper_subset()

    print("Test Case:")
    print(f"  A: {A}")
    print(f"  B: {B}")
    print(f"  Expected Union: {expected_union}")
    print(f"  Expected Intersection: {expected_intersection}")
    print(f"  Expected Symmetric Difference: {expected_symmetric_difference}")
    print(f"  Expected Subset: {expected_subset}")
    print(f"  Expected Proper Subset: {expected_proper_subset}")

    # Check if the results match the expected values
    print("--------------------------------------------------------------------")
    print ("Results of the test case:")
    if union_set == expected_union:
        print("  Union: Passed")
    else:
        print("  Union: Failed")

    if intersection_set == expected_intersection:
        print("  Intersection: Passed")
    else:
        print("  Intersection: Failed")

    if symmetric_difference_set == expected_symmetric_difference:
        print("  Symmetric Difference: Passed")
    else:
        print("  Symmetric Difference: Failed")

    if is_subset == expected_subset:
        print("  Subset Check: Passed")
    else:
        print("  Subset Check: Failed")

    if is_proper_subset == expected_proper_subset:
        print("  Proper Subset Check: Passed")
    else:
        print("  Proper Subset Check: Failed")

    print()
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")


# Test cases:
test_cases = [
    # Test Case 1: Basic sets with no common elements
    ({1, 2, 3}, {4, 5, 6}, {1, 2, 3, 4, 5, 6}, set(), {1, 2, 3, 4, 5, 6}, False, False),
    # Test Case 2: Sets with common elements
    ({1, 2, 3, 4}, {3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}, {3, 4}, {1, 2, 5, 6}, False, False),
    # Test Case 3: A is a subset of B
    ({1, 2, 3}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {1, 2, 3}, {4, 5}, True, True),
    # Test Case 4: A is a proper subset of B
    ({1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3}, {4}, True, True),
    # Test Case 5: A and B are empty sets
    (set(), set(), set(), set(), set(), True, False)
]

for i, (A, B, expected_union, expected_intersection, expected_symmetric_difference, expected_subset, expected_proper_subset) in enumerate(test_cases, start=1):
    print(f"Running Test Case {i}:")
    run_test_case(A, B, expected_union, expected_intersection, expected_symmetric_difference, expected_subset, expected_proper_subset)