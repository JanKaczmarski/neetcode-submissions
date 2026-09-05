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
	} else if n == 2 {
		return max(nums[0], nums[1])
	}
	
	prevRob, currRob := nums[0], nums[0]
	prevNoRob, currNoRob := 0, nums[1]

	for i := 2; i < n; i++ {
		//fmt.Printf("i: %d, prevRob: %d, currRob: %d\n", i, prevRob, currRob)
		//fmt.Printf("i: %d, prevNoRob: %d, currNoRob: %d\n", i, prevNoRob, currNoRob)
		if i == n - 1 {
			prevNoRob, currNoRob = currNoRob, max(currNoRob, prevNoRob + nums[i])
			continue
		}
		prevRob, currRob = currRob, max(currRob, prevRob + nums[i])
		prevNoRob, currNoRob = currNoRob, max(currNoRob, prevNoRob + nums[i])
	}

	//fmt.Printf("FINAL prevRob: %d, currRob: %d\n", prevRob, currRob)
	//fmt.Printf("FINAL prevNoRob: %d, currNoRob: %d\n", prevNoRob, currNoRob)

	return max(currRob, currNoRob)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}