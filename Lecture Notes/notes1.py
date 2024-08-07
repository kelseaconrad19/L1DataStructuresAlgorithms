# Dictionaries - doesn't have the same constraints as lists because it's not ordered. O(1) operation
## if genre is in dictionaries, it will return the book
# Lists = [genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre, genre1]
# Lists are pretty time intensive because you have to iterate through the entire list to find the value you want - O(n) operation


class Library: 
  def __init__(self):
    self.shelves = {}
    
  def add_book(self, section, book):
    if section not in self.shelves: #! O(1) operation
      self.shelves[section] = [book]
    else:
      self.shelves[section].append(book)
      
    
  def retrieve_books(self, section):
    return self.shelves.get(section, 'No books available in this section...')
  

#? Example Usage
library = Library()

#? Adding books to the library
library.add_book('YA', 'Harry Potter')
library.add_book('Fiction', 'Lord of the Rings')
library.add_book('YA', 'The Hunger Games')

#? Retrieving books from the library
print(library.retrieve_books('Fiction')) # ['Harry Potter', 'Lord of the Rings', 'The Hunger Games']
print(library.retrieve_books('Non-Fiction')) # No books available in this section...


