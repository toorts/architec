package hw_6.data;

import java.util.ArrayList;
import java.util.List;
import hw_6.domain.Book;


public class InMemoryBookRepository implements BookRepository {
    
    private List<Book> books;

    public InMemoryBookRepository() {
        books = new ArrayList<>();
    }

    @Override
    public void addBook(Book book) {
        books.add(book);
    }

    @Override
    public void removeBook(Book book) {
        books.remove(book);
    }

    @Override
    public List<Book> getAllBooks() {
        return new ArrayList<>(books);
    }
}