package hw_6.presentation;

import hw_6.domain.Book;
import hw_6.data.BookRepository;
import hw_6.data.InMemoryBookRepository;

import java.util.List;


public class Main {
    public static void main(String[] args) {

        BookRepository bookRepository = new InMemoryBookRepository();

        // Добавляем книги в магазин
        Book book1 = new Book("1", "Clean Code", "Robert C. Martin", 34.99);
        Book book2 = new Book("2", "Effective Java", "Joshua Bloch", 29.99);
        bookRepository.addBook(book1);
        bookRepository.addBook(book2);

        // Получаем список всех книг в магазине
        List<Book> allBooks = bookRepository.getAllBooks();
        for (Book book : allBooks) {
            System.out.println("Книга: " + book.getTitle() + ", Автор: " + book.getAuthor() + ", Цена: $" + book.getPrice());
        }
    }
}