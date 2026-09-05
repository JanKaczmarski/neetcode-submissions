func rob(nums []int) int {
    // brute force - backtrack, to rob current house or not, if rob move 2 houes forward
	// store the boolean if the first house was robbed (robbing last house depends on it)

	// dp - have a standard accumulators prev and curr which stores house robbing until now,
	// on the last house, have prev and curr store the bool if the first house was robbed

	// 2 cases:
	// - rob the first house
	// - don't rob the first house
	// take maximum out of both outputs

	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	
	return max(robRow(nums[:n - 1]), robRow(nums[1:]))
}

func robRow(nums []int) int {
	prev, curr := 0, 0

	for _, val := range nums {
		newRob := max(val + prev, curr)
		prev, curr = curr, newRob
	}

	return curr
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}