type vertexAncestorPair struct {
	vertex int
	anc    int
}

func validTree(n int, edges [][]int) bool {
	// find-union:
	// 2. if 2 vertexes are connected by the edge they go into single group
	// 3. each group has a representative
	// 4. if 2 vertexes are in the same gropu AND we encouter and edge with them
	// it means we have a cycle

	// dfs/bfs:
	// 1. keep track of visited array
	// 2. in each iteration move to the next element and keep from which vertex we're coming (backward edge)
	// 3. if our neighbour is already visited (and it isn't backward edge) we have a cycle
	// 4. do this for each disjoint graph that edges make

	// 1. dfs
	graph := make([][]int, n)
	for i := range graph {
		graph[i] = make([]int, 0)
	}

	for _, edge := range edges {
		left := edge[0]
		right := edge[1]

		graph[left] = append(graph[left], right)
		graph[right] = append(graph[right], left)
	}

	visited := make([]bool, n)
	start := 0
	stack := []vertexAncestorPair{{
		vertex: start,
		anc:    -1, // doesn't exits - can move anywhere
	}}

	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		visited[current.vertex] = true

		for _, neigh := range graph[current.vertex] {
			if neigh == current.anc {
				continue
			}
			if visited[neigh] {
				return false
			}

			stack = append(stack, vertexAncestorPair{
				vertex: neigh,
				anc:    current.vertex,
			})
		}
	}

	for _, wasVisitied := range visited {
		if !wasVisitied {
			return false
		}
	}

	return true
}
