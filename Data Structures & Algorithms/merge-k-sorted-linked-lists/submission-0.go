/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

const maxVal = 1001

func mergeKLists(lists []*ListNode) *ListNode {
    // 1. have a `res` linked list
	// 2. while at least 1 list is not empty:
	// - go thorugh each list and select the smallest elemtn
	// - add this element to `res` and remove it from it's original list
	// - repeat
	// 3. return `res.head`
	// Time: O(n ** 2), n - number of elements
	resTail := &ListNode{}
	res := resTail

	for {
		minVal, minIdx := maxVal, -1
		for i, list := range lists {
			if list == nil {
				continue
			}

			if list.Val < minVal {
				minVal = list.Val
				minIdx = i
			}
		}

		if minIdx == -1 {
			break
		}

		minNode := lists[minIdx]
		lists[minIdx] = minNode.Next
		
		minNode.Next = nil
		resTail.Next = minNode
		resTail = resTail.Next
	}
	
	return res.Next
}
