import java.awt.Point;
import java.awt.Color;

public class Rectangle implements Shape {
    //Attributes
    private double width;
    private double height;
    private Point topLeftCorner;
    private Color color;
    //Constructor
    public Rectangle(double width, double height, Point topLeftCorner, Color color){
        this.width = width;
        this.height = height;
        this.topLeftCorner = topLeftCorner;
        this.color = color;
    }

    public double getWidth(){
        return this.width;
    }

    public void setWidth(double width){
        this.width = width;
    }

    public double getHeight(){
        return this.height;
    }

    public void setHeight(double height){
        this.height = height;
    }

    public Point getTopLeft(){
        return this.topLeftCorner;
    }

    private void setTopLeft(Point topLeftCorner){
        this.topLeftCorner = topLeftCorner;
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
        return getHeight() * getWidth();
    }

    @Override
    public double getPerimeter() {
        return 2 * (getHeight() + getWidth());
    }

    @Override
    public void translate(Point point) {
        double newX = getTopLeft().getX() + point.getX();
        double newY = getTopLeft().getY() + point.getY();
        setTopLeft(new Point((int) newX, (int) newY));
    }
}
