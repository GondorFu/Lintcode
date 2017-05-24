struct Node{
	Node(int _key, int _value){
		key = _key; value = _value; pre = NULL; next = NULL;
	};

	int key;
	int value;
	Node* pre;
	Node* next;
};

class LRUCache{
public:
	// @param capacity, an integer
	LRUCache(int capacity) {
		// write your code here
		this->capacity = capacity;
		size = 0;
		head = NULL;
		tail = NULL;
	}

	void setHead(Node* p){
		if(head != p){
			if(tail == p){
				tail = tail->pre;
				tail->next = NULL;
			}
			else{
				p->pre->next = p->next;
				p->next->pre = p->pre;
			}
			head->pre = p;
			p->pre = NULL;
			p->next = head;
			head = p;
		}
	}

	// @return an integer
	int get(int key) {
		// write your code here
		if(m.find(key) == m.end())
			return -1;

		Node* p = m[key];
		int res = p->value;
		setHead(p);
		return res;
	}

	// @param key, an integer
	// @param value, an integer
	// @return nothing
	void set(int key, int value) {
		// write your code here
		if(m.find(key) != m.end()){
			Node* p = m[key];
			setHead(p);
			p->value = value;
		}
		else{
			Node* p = new Node(key, value);
			m[key] = p;
			if(head == NULL){
				head = p;
				tail = p;
			}else{
				head->pre = p;
				p->next = head;
				head = p;

			}

			if(size == capacity){
				m.erase(m.find(tail->key));
				tail = tail->pre;
				delete tail->next;
				tail->next = NULL;
			}else
				size++;
		}

	}

private:
	map<int, Node*> m;
	int capacity;
	int size;
	Node* head;
	Node* tail;
};