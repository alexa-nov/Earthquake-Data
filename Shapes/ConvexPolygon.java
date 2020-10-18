import java.awt.Point;
import java.awt.Color;


public class ConvexPolygon implements Shape {
    //Attributes
    private Point[] vertices;
    private Color color;
    //Constructor
    public ConvexPolygon(Point[] vertices, Color color){
        this.vertices = vertices;
        this.color = color;
    }

    public Point getVertex(int index){
        //takes an index and returns the specified vertex of the ConvexPolygon
        return this.vertices[index];
    }

    private void setVertex(int index, Point point){
        this.vertices[index] = point;
    }

    @Override
    public Color getColor()  {
        return this.color;
    }

    @Override
    public void setColor(Color color) {
        this.color = color;
    }

    @Override
    public double getArea() {
        double area = 0;
        int idx2 = vertices.length - 1;
        for(int idx = 0; idx < vertices.length; idx++){
            double xValues = (vertices[idx2].getX() + vertices[idx].getX());
            double yValues = (vertices[idx2].getY() - vertices[idx].getY());
            area += (xValues * yValues);
            idx2 = idx;
        }
        return Math.abs(area * 0.5);
    }

    @Override
    public double getPerimeter() {
        double perimeter = 0.0;
        for (int idx = 0; idx < vertices.length; idx++){
            if (idx + 1 >= vertices.length) {
                double x_values = Math.pow(vertices[idx].getX() - vertices[0].getX(), 2);
                double y_values = Math.pow(vertices[idx].getY() - vertices[0].getY(), 2);
                double line = Math.sqrt(x_values + y_values);
                perimeter += line;
            }
            else {
                double x_values = Math.pow(vertices[idx].getX() - vertices[idx + 1].getX(), 2);
                double y_values = Math.pow(vertices[idx].getY() - vertices[idx + 1].getY(), 2);
                double line = Math.sqrt(x_values + y_values);
                perimeter += line;
            }
        }
        return perimeter;
    }

    @Override
    public void translate(Point point) {
        for(int idx = 0; idx < vertices.length; idx++){
            double newX = vertices[idx].getX() + point.getX();
            double newY = vertices[idx].getY() + point.getY();
            setVertex(idx, new Point((int) newX, (int) newY));
        }
    }
}
