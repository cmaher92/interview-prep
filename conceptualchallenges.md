
1. Alternative Resizable Array:
What if while appending item to end of resizable array, there isn't space
Creating a new underlying array and copying all the items is a time-consuming operation
What alt. approaches could you use to create a resizable array and how would you implement it

Answer:
I would create a new underlying based on the current size of the array, so once the size threshold
is crossed a new array is created.

2. Implement a Queue
Assume working implementations of the core list data structures:
    - resizable array (get, set, size)
    - circular buffer (get, set, head)
    - singly linked list (head, tail, append, prepend, size)

Which are good choices to implement a queue? Explain why or why not for each.
What is the time complexity of the enqueue, dequeue, front, and size operations?

Answer:
Resizable array is not a good choice for a queue because it is constant time to enqueue something but O(n) time to dequeue.
Circular buffer is a good option for a queue because it is a fixed size data structure, both enqueue and dequeue are constant time.
Singly linked list is also a good option because enqueue and dequeue are both constant time, front and size would also be constant time as well.


3. Hash Table Buckets
When storing an entry in a hash table, we calculate the key's have value. Sometimes there is a collision
and a new entry hashes to the same bucket as an existing entry. To resolve this with chaining, we used a linked list in each
bucket to hold multiple entries. Could we instead use another type of list, like an array or even another hash table?
What type of list would be an improvement over using a linked list? Why or why not?

Answer:
I had to look this up because I needed a refresher on the specifics.

Separate chaining with linked lists:
If a collision occurs the item is added to the end of the list, maintains effective even when number of keys is larger than number of slots.
Worst case scenario is proportional to number of keys.
- The next pointer in each entry record can be a space overhead
- Poor cache performance

Separate chaining with other structures:
self-balancing tree brings down theoretical worst-case time of common hash table operations (insertion, deletion, lockup)
down to O(log n). Only worth the trouble and extra memory cost if long delays MUST be avoided.

Array hash table uses a dynamic array to store all the entries that hash to the same slot, each newly inserted entry gets
appended to the end of the dynamic array that is assigned to the slot. Array only grows in an exact manner. It can be modified
based on time & space needs.

Also open addressing is an option
