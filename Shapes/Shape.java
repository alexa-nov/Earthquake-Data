import java.awt.Color;
import java.awt.Point;

public interface Shape {

    //Returns color of Shape
    public Color getColor();

    //Sets color of Shape
    public void setColor(Color color);

    //Returns area of Shape
    public double getArea();

    //Returns perimeter of Shape
    public double getPerimeter();

    //Translates the entire shape by the (x,y) coordinates of a given Point
    public void translate(Point point);
}
