type Node struct {
	key  int
	val  int
	freq int

	next *Node
	prev *Node
}

type DoublyLinkedList struct {
	head *Node
	tail *Node
	size int
}

func newDoublyLinkeList() *DoublyLinkedList {
	head := &Node{}
	tail := &Node{}

	head.next = tail
	tail.prev = head

	return &DoublyLinkedList{
		head: head,
		tail: tail,
	}
}

func (list *DoublyLinkedList) addMRU(node *Node) {
	last := list.tail.prev

	last.next = node
	node.prev = last

	node.next = list.tail
	list.tail.prev = node

	list.size++
}

func (list *DoublyLinkedList) remove(node *Node) {
	node.prev.next = node.next
	node.next.prev = node.prev

	node.prev = nil
	node.next = nil

	list.size--
}

func (list *DoublyLinkedList) removeLRU() *Node {
	if list.size == 0 {
		return nil
	}

	node := list.head.next
	list.remove(node)

	return node
}

func (list *DoublyLinkedList) isEmpty() bool {
	return list.size == 0
}

type LFUCache struct {
	capacity int
	size int
	minFreq int

	// key -> Node
	nodes map[int]*Node

	// freq -> LRU list
	freqLists map[int]*DoublyLinkedList
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		capacity: capacity,
		nodes: make(map[int]*Node),
		freqLists: make(map[int]*DoublyLinkedList),
	}
}

func (this *LFUCache) Get(key int) int {
	node, exists := this.nodes[key]
	if !exists {
		return -1
	}

	this.promote(node)

	return node.val
}

func (this *LFUCache) Put(key int, value int) {
	if node, exists := this.nodes[key]; exists {
		node.val = value
		this.promote(node)
		return
	}

	if this.size == this.capacity {
		minList := this.freqLists[this.minFreq]
		evicted := minList.removeLRU()

		delete(this.nodes, evicted.key)
		this.size--

		if minList.isEmpty() {
			delete(this.freqLists, this.minFreq)
		}
	}

	node := &Node{
		key: key,
		val: value,
		freq: 1,
	}

	list := this.getOrCreateList(1)
	list.addMRU(node)

	this.nodes[key] = node
	this.size++
	this.minFreq = 1
}

func (this *LFUCache) promote(node *Node) {
	oldFreq := node.freq
	oldList := this.freqLists[oldFreq]

	oldList.remove(node)

	if oldFreq == this.minFreq && oldList.isEmpty() {
		this.minFreq = oldFreq + 1
	}

	if oldList.isEmpty() {
		delete(this.freqLists, oldFreq)
	}

	node.freq++

	newList := this.getOrCreateList(node.freq)
	newList.addMRU(node)
}

func (this *LFUCache) getOrCreateList(freq int) *DoublyLinkedList {
	list, exists := this.freqLists[freq]
	if !exists {
		list = newDoublyLinkeList()
		this.freqLists[freq] = list
	}

	return list
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param1 := obj.Get(key);
 * obj.Put(key,value);
 */