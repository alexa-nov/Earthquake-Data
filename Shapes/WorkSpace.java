import java.awt.Point;
import java.awt.Color;
import java.util.List;
import java.util.ArrayList;

public class WorkSpace {
    private List<Shape> shapeList;
    //Constructor
    public WorkSpace(){
        this.shapeList = new ArrayList<Shape>();
    }
    public void add(Shape shape){
        //adds an object which implements the Shape interface to the end of the List in the WorkSpace
        shapeList.add(shape);
    }
    public Shape get(int index){
        //returns the specified Shape from the WorkSpace
        return shapeList.get(index);
    }
    public int size(){
        return shapeList.size();
    }
    public List<Circle> getCircles(){
        //returns a List of all the Circle objects contained by the WorkSpace
        List<Circle> circles = new ArrayList<Circle>();
        for (Shape shape: shapeList){
            if (shape instanceof Circle)
                circles.add((Circle) shape);
        }
        return circles;
    }

    public List<Rectangle> getRectangles(){
        //returns a List of all the Rectangle objects contained by the WorkSpace
        List<Rectangle> rectangles = new ArrayList<Rectangle>();
        for (Shape shape: shapeList){
            if (shape instanceof Rectangle)
                rectangles.add((Rectangle) shape);
        }
        return rectangles;
    }

    public List<Triangle> getTriangles(){
        //returns a List of all the Triangle objects contained by the WorkSpace
        List<Triangle> triangles = new ArrayList<Triangle>();
        for (Shape shape: shapeList){
            if (shape instanceof Triangle)
                triangles.add((Triangle) shape);
        }
        return triangles;
    }

    public List<ConvexPolygon> getConvexPolygons(){
        //returns a List of all the ConvexPolygon objects contained by the WorkSpace
        List<ConvexPolygon> convexPolygons = new ArrayList<ConvexPolygon>();
        for (Shape shape: shapeList){
            if (shape instanceof ConvexPolygon)
                convexPolygons.add((ConvexPolygon) shape);
        }
        return convexPolygons;
    }

    public List<Shape> getShapesByColor(Color color){
        //returns a List of all the Shape objects contained by the WorkSpace that match the specified Color
        List<Shape> shapesByColor = new ArrayList<Shape>();
        for (Shape shape: shapeList){
            if (shape.getColor().equals(color))
                shapesByColor.add(shape);
        }
        return shapesByColor;
    }

    public double getAreaOfAllShapes(){
        //returns the sum of the areas of all the Shapes contained by the WorkSpace
        double area = 0;
        for (Shape shape: shapeList){
            area += shape.getArea();
        }
        return area;
    }
    public double getPerimeterOfAllShapes(){
        //returns the sum of the perimeters of all the Shapes contained by the WorkSpace
        double perimeter = 0;
        for (Shape shape: shapeList){
            perimeter += shape.getPerimeter();
        }
        return perimeter;
    }
}
