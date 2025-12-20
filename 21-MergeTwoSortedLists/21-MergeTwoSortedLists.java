// Last updated: 12/20/2025, 5:43:44 PM
1/**
2 * Definition for singly-linked list.
3 * public class ListNode {
4 *     int val;
5 *     ListNode next;
6 *     ListNode() {}
7 *     ListNode(int val) { this.val = val; }
8 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
9 * }
10 */
11class Solution {
12    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
13        ListNode solutionhead = new ListNode();
14        ListNode solution = solutionhead;
15        ListNode current1 = list1;
16        ListNode current2 = list2;
17        
18        while (current1 != null && current2 != null) {
19            if (current1.val < current2.val) {
20                solution.next = current1;
21                current1 = current1.next;
22            } else {
23                solution.next = current2;
24                current2 = current2.next;
25            }
26            solution = solution.next;
27        }
28
29        if (current1 != null) {
30            solution.next = current1;
31        } else {
32            solution.next = current2;
33        }
34
35        return solutionhead.next;
36    }
37}