import java.awt.Point;
import java.awt.Color;

public class Triangle implements Shape {
    //Attributes
    private Point vertexA;
    private Point vertexB;
    private Point vertexC;
    private Color color;
    //Constructor
    public Triangle(Point vertexA, Point vertexB, Point vertexC, Color color){
        this.vertexA = vertexA;
        this.vertexB = vertexB;
        this.vertexC = vertexC;
        this.color = color;
    }

    public Point getVertexA() {
        return this.vertexA;
    }

    public Point getVertexB() {
        return this.vertexB;
    }

    public Point getVertexC() {
        return vertexC;
    }

    private void setVertexA(Point point){
        this.vertexA = point;
    }

    private void setVertexB(Point point){
        this.vertexB = point;
    }

    private void setVertexC(Point point){
        this.vertexC = point;
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
    public double getArea(){
        double first = getVertexA().getX() * (getVertexB().getY() - getVertexC().getY());
        double second = getVertexB().getX() * (getVertexC().getY() - getVertexA().getY());
        double third = getVertexC().getX() * (getVertexA().getY() - getVertexB().getY());
        return 0.5 * (first + second + third);

    }
    @Override
    public double getPerimeter() {
        double length1 = Math.sqrt(Math.pow(getVertexB().getX() - getVertexA().getX(), 2) +
                Math.pow(getVertexB().getY() - getVertexA().getY(), 2));
        double length2 = Math.sqrt(Math.pow(getVertexC().getX() - getVertexB().getX(), 2) +
                Math.pow(getVertexC().getY() - getVertexB().getY(), 2));
        double length3 = Math.sqrt(Math.pow(getVertexA().getX() - getVertexC().getX(), 2) +
                Math.pow(getVertexA().getY() - getVertexC().getY(), 2));
        return length1 + length2 + length3;
    }

    @Override
    public void translate(Point point) {
        double newVertexAX = getVertexA().getX() + point.getX();
        double newVertexAY = getVertexA().getY() + point.getY();
        setVertexA(new Point((int) newVertexAX, (int) newVertexAY));
        double newVertexBX = getVertexB().getX() + point.getX();
        double newVertexBY = getVertexB().getY() + point.getY();
        setVertexB(new Point((int) newVertexBX, (int) newVertexBY));
        double newVertexCX = getVertexC().getX() + point.getX();
        double newVertexCY = getVertexC().getY() + point.getY();
        setVertexC(new Point((int) newVertexCX, (int) newVertexCY));
    }
}
