import java.awt.Point;
import java.awt.Color;

public class Circle implements Shape {
    //Attributes
    private double radius;
    private Point center;
    private Color color;
    //Constructor
    public Circle(double radius, Point center, Color color){
        this.radius = radius;
        this.center = center;
        this.color = color;
    }

    public double getRadius(){
        return this.radius;
    }

    public void setRadius(double radius){
        this.radius = radius;
    }

    public Point getCenter(){
        return this.center;
    }

    private void setCenter(Point center){
        this.center = center;
    }

    @Override
    public Color getColor() {
        return this.color;
    }

    @Override
    public void setColor(Color color) {
        this.color = color;
    }

    @Override
    public double getArea() {
        return (Math.PI * (getRadius() * getRadius()));
    }

    @Override
    public double getPerimeter() {
        return (2 * Math.PI * getRadius());
    }

    @Override
    public void translate(Point point) {
        double newX = getCenter().getX() + point.getX();
        double newY = getCenter().getY() + point.getY();
        setCenter(new Point((int) newX, (int) newY));
    }
}
