class Node {
  constructor(value) {
    this.val = value;
    this.next = null;
  }
}

class SList {
  constructor() {
    this.head = null;
  }

  addFront(val) {
    var node = new Node(val);
    node.next = this.head;
    this.head = node;
    return this;
  }

  removeFront() {
    // set temp to current head
    var temp = this.head;
    // move where head points to second node, if there is no second node, this will be null
    this.head = this.head.next;
    // remove the pointer from the old node to the new head
    temp.next = null;
    // return this for chaining
    return this;
  }
}

var list = new SList();
list.addFront('C').addFront('B').addFront('A').addFront('Z')
console.log(list);
list.removeFront();
console.log(list);