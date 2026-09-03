func longestPalindrome(s string) string {
	n := len(s)
	if n < 2 {
		return s
	}

	resL, resR := 0, 0

	var expand func(l, r int) (int, int)
	expand = func(l, r int) (int, int) {
		for l >= 0 && r < n && s[l] == s[r] {
			l--
			r++
		}
		// we went 1 too far
		return l + 1, r - 1
	}

	for i := range n {
		// odd case
		l1, r1 := expand(i, i)

		// even case
		l2, r2 := expand(i, i+1)

		if r1 - l1 > resR - resL {
			resL = l1
			resR = r1
		}

		if r2 - l2 > resR - resL {
			resL = l2
			resR = r2
		}
	}

	return s[resL:resR+1]
}
