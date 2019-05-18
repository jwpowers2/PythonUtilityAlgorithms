# run linked lists

from SList import SList
from SLNode import SLNode


sll = SList()

sll.head = SLNode('Alice')

sll.head.next = SLNode('Bob')
sll.head.next.next = SLNode('Person')

sll.print_all_vals()

sll.insert_after('Bob','Stacy')
sll.delete('Bob')

sll.print_all_vals()
sll.delete('Stacy')
sll.print_all_vals()
sll.prepend('The First!').prepend("the most first")
sll.print_all_vals()

sll.append('The Last!').append('The Most Last!')
sll.print_all_vals()
