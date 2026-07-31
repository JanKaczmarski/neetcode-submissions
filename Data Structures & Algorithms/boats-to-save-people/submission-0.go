func numRescueBoats(people []int, limit int) int {
	// match largest with the smallest, if:
	// - sum > limit -> put largest alone in the bote
	// - sum <= limit -> put both on the boat
	sort.Ints(people)

	l, r := 0, len(people) - 1
	res := 0

	for l < r {
		sum := people[l] + people[r]
		if sum > limit {
			res++
			r--
		} else {
			res++
			l++
			r--
		}
	}

	if l == r {
		res++
	}


	return res
}
