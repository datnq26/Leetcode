// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_two_lists(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut current = &mut dummy;

        while l1.is_some() && l2.is_some() {
            if l1.as_ref().unwrap().val <= l2.as_ref().unwrap().val {
                let next = l1.as_mut().unwrap().next.take();
                current.next = l1;
                l1 = next;
            } else {
                let next = l2.as_mut().unwrap().next.take();
                current.next = l2;
                l2 = next;
            }
            current = current.next.as_mut().unwrap();
        }

        current.next = if l1.is_some() { l1 } else { l2 };
        dummy.next
    }
}