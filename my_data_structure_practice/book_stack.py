


class book:
title = ""
author = ""
long_book = Book()
long_book.title = "War and Peace"
long_book.author = "Tolstoy"
medium_book = Book()
medium_book.title = "Book of Armaments"
medium_book.author = "Maynard"
short_book = Book()
short_book.title = "Vegetables I Like"
short_book.author = "John Keyser"







#############################################
book_stack = []
book_stack.append(medium_book)
book_stack.append(short_book)
book_stack.append(long_book)
next_book = book_stack.pop()
print(next_book.title+" by "+next_book.author)


OUTPUT:
War and Peace by Tolstoy
