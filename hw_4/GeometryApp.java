/**
 * Интерфейс для геометрической фигуры.
 */
interface IShape {
    /**
     * Получает площадь фигуры.
     *
     * @return Площадь фигуры.
     */
    double getArea();

    /**
     * Получает периметр фигуры.
     *
     * @return Периметр фигуры.
     */
    double getPerimeter();
}

/**
 * Класс для представления круга.
 */
class Circle implements IShape {
    private double radius;

    /**
     * Конструктор для создания объекта круга.
     *
     * @param radius Радиус круга.
     */
    public Circle(double radius) {
        this.radius = radius;
    }

    /**
     * Получает площадь круга.
     *
     * @return Площадь круга.
     */
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    /**
     * Получает периметр круга.
     *
     * @return Периметр круга.
     */
    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

/**
 * Класс для представления прямоугольника.
 */
class Rectangle implements IShape {
    private double length;
    private double width;

    /**
     * Конструктор для создания объекта прямоугольника.
     *
     * @param length Длина прямоугольника.
     * @param width  Ширина прямоугольника.
     */
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    /**
     * Получает площадь прямоугольника.
     *
     * @return Площадь прямоугольника.
     */
    @Override
    public double getArea() {
        return length * width;
    }

    /**
     * Получает периметр прямоугольника.
     *
     * @return Периметр прямоугольника.
     */
    @Override
    public double getPerimeter() {
        return 2 * (length + width);
    }
}

/**
 * Класс для представления треугольника.
 */
class Triangle implements IShape {
    private double side1;
    private double side2;
    private double side3;

    /**
     * Конструктор для создания объекта треугольника.
     *
     * @param side1 Длина первой стороны треугольника.
     * @param side2 Длина второй стороны треугольника.
     * @param side3 Длина третьей стороны треугольника.
     */
    public Triangle(double side1, double side2, double side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    /**
     * Получает площадь треугольника.
     *
     * @return Площадь треугольника.
     */
    @Override
    public double getArea() {
        double s = (side1 + side2 + side3) / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    /**
     * Получает периметр треугольника.
     *
     * @return Периметр треугольника.
     */
    @Override
    public double getPerimeter() {
        return side1 + side2 + side3;
    }
}

/**
 * Главный класс приложения для демонстрации работы с геометрическими фигурами.
 */
public class GeometryApp {
    public static void main(String[] args) {
        // Пример использования конкретных классов геометрических фигур
        Circle circle = new Circle(5.0);
        System.out.println("Площадь круга: " + circle.getArea());
        System.out.println("Периметр круга: " + circle.getPerimeter());

        Rectangle rectangle = new Rectangle(4.0, 6.0);
        System.out.println("Площадь прямоугольника: " + rectangle.getArea());
        System.out.println("Периметр прямоугольника: " + rectangle.getPerimeter());

        Triangle triangle = new Triangle(3.0, 4.0, 5.0);
        System.out.println("Площадь треугольника: " + triangle.getArea());
        System.out.println("Периметр треугольника: " + triangle.getPerimeter());
    }
}
