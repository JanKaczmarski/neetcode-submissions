func isAlienSorted(words []string, order string) bool {
    ordering := make(map[byte]int)
    for i := range order {
        ordering[order[i]] = i
    }
    
    for i := 0; i < len(words) - 1; i++ {
        letterIdx := 0
        minLen := len(words[i])
        if len(words[i+1]) < minLen {
            minLen = len(words[i+1])
        }
        for letterIdx < minLen {
            if words[i][letterIdx] == words[i+1][letterIdx] {
                letterIdx++
                continue
            }
            if isSmaller(words[i][letterIdx], words[i+1][letterIdx], ordering) {
                break
            } else {
                return false
            }
        }

        // prefix equal -> is len correct?
        if letterIdx == minLen && len(words[i]) > len(words[i+1]){
            return false
        }
    }

    return true
}


// is a < b in ordering `order`
func isSmaller(a, b byte, order map[byte]int) bool {
    return order[a] <= order[b]
}