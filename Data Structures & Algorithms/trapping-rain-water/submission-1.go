func trap(height []int) int {
	n := len(height)
	if n < 3 {
		return 0
	}
	// two pointers
	lMax, rMax := 0, 0
	res := 0

	for i := 1; i < n - 1; i++ {
		if i >= rMax {
			rMax = findRightMaxIdx(height, i + 1)
		}

		minLR := height[lMax]
		if height[rMax] < minLR {
			minLR = height[rMax]
		}

		hereWater := minLR - height[i]
		if hereWater > 0 {
			res += hereWater
		}

		if height[i] > height[lMax] {
			lMax = i
		}
	}

	return res
}

func findRightMaxIdx(height []int, startIdx int) int {
	// todo: guardrails here
	rMax := startIdx
	for i := startIdx + 1; i < len(height); i++ {
		if height[i] > height[rMax] {
			rMax = i
		}
	}

	return rMax
}
