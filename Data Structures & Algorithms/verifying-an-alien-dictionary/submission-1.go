func isAlienSorted(words []string, order string) bool {
    ordering := make(map[byte]int)
    for i := range order {
        ordering[order[i]] = i
    }
    
    for i := 0; i < len(words) - 1; i++ {
        if !isSmaller(words[i], words[i+1], ordering) {
            return false
        }
    }

    return true
}

func isSmaller(word1, word2 string, order map[byte]int) bool {
    m := len(word1)
    n := len(word2)
    
    for i := 0; i < m && i < n; i++ {
        if word1[i] == word2[i] {
            continue
        }

        return order[word1[i]] < order[word2[i]]
    }
    
    return m < n
}
