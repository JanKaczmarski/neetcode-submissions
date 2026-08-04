//import "container/heap"

type Item struct {
	value int
	index int
}

type MaxHeap []Item

func (h MaxHeap) Len() int {
	return len(h)
}

func (h MaxHeap) Less(i, j int) bool {
	return h[i].value > h[j].value
}

func (h MaxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(Item))
}

func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[:n-1]
	return item
}

func maxSlidingWindow(nums []int, k int) []int {
	h := &MaxHeap{}
	res := make([]int, 0, len(nums)-k+1)

	for i, value := range nums {
		heap.Push(h, Item{
			value: value,
			index: i,
		})

		windowStart := i - k + 1

		// Remove elements that are no longer in the window.
		for h.Len() > 0 && (*h)[0].index < windowStart {
			heap.Pop(h)
		}

		if i >= k-1 {
			res = append(res, (*h)[0].value)
		}
	}

	return res
}