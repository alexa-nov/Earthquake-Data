import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

import java.awt.Color;
import java.awt.Point;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class TestCases
{
   public static final double DELTA = 0.00001;

   /* some sample tests but you must write more! see lab write up */

   @Test
   public void testCircleGetRadius1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      assertEquals(5.678, c.getRadius(), DELTA);
   }

   @Test
   public void testCircleSetRadius1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      c.setRadius(7.8);
      assertEquals(7.8, c.getRadius(), DELTA);
   }

   @Test
   public void testCircleGetCenter1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      assertEquals(new Point (2,3), c.getCenter());
   }

   @Test
   public void testCircleGetColor1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      assertEquals(Color.BLACK, c.getColor());
   }

   @Test
   public void testCircleSetColor1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      c.setColor(Color.RED);
      assertEquals(Color.RED, c.getColor());
   }


   @Test
   public void testCircleGetArea1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(101.2839543, c.getArea(), DELTA);
   }

   @Test
   public void testCircleGetPerimeter1()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(35.6759261, c.getPerimeter(), DELTA);
   }

   @Test
   public void testCircleTranslate1()
   {
      Circle c = new Circle(5.678, new Point(0, 0), Color.BLACK);
      c.translate(new Point(5, 2));
      assertEquals(new Point (5,2), c.getCenter());
   }

   @Test
   public void testCircleTranslate2()
   {
      Circle c = new Circle(5.678, new Point(-5, -2), Color.BLACK);
      c.translate(new Point(1, 1));
      assertEquals(new Point (-4,-1), c.getCenter());
   }

   @Test
   public void testRectangleGetWidth1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      assertEquals(5.2, r.getWidth(), DELTA);
   }

   @Test
   public void testRectangleSetWidth1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      r.setWidth(7.5);
      assertEquals(7.5, r.getWidth(), DELTA);
   }

   @Test
   public void testRectangleGetHeight1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      assertEquals(4.6, r.getHeight(), DELTA);
   }

   @Test
   public void testRectangleSetHeight1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      r.setHeight(8.9);
      assertEquals(8.9, r.getHeight(), DELTA);
   }

   @Test
   public void testRectangleGetTopLeftCorner1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      assertEquals(new Point (5,6), r.getTopLeft());
   }

   @Test
   public void testRectangleGetColor1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      assertEquals(Color.BLACK, r.getColor());
   }

   @Test
   public void testRectangleSetColor1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      r.setColor(Color.RED);
      assertEquals(Color.RED, r.getColor());
   }

   @Test
   public void testRectangleGetArea1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      assertEquals(23.92, r.getArea(), DELTA);
   }

   @Test
   public void testRectangleGetPerimeter1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);

      assertEquals(19.6, r.getPerimeter(), DELTA);
   }

   @Test
   public void testRectangleTranslate1()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (5,6), Color.BLACK);
      r.translate(new Point(1,1));
      assertEquals(new Point (6,7), r.getTopLeft());
   }

   @Test
   public void testRectangleTranslate2()
   {
      Rectangle r = new Rectangle(5.2,4.6, new Point (-5,-6), Color.BLACK);
      r.translate(new Point(1,1));
      assertEquals(new Point (-4,-5), r.getTopLeft());
   }

   @Test
   public void testTriangleGetArea1()
   {
      Triangle t = new Triangle(new Point (1,1), new Point (2,3), new Point (4,5), Color.BLACK);
      assertEquals(-1, t.getArea(), DELTA);
   }

   @Test
   public void testTriangleGetArea2()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(18.5, t.getArea(), DELTA);
   }

   @Test
   public void testTriangleTranslate1()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      t.translate(new Point(1,1));
      assertEquals(new Point(0,3), t.getVertexA());
      assertEquals(new Point(-4,-4), t.getVertexB());
      assertEquals(new Point(3,-1), t.getVertexC());
   }

   @Test
   public void testTriangleGetVertexA()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(new Point(-1,2), t.getVertexA());
   }


   @Test
   public void testTriangleGetVertexB()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(new Point(-5,-5), t.getVertexB());
   }

   @Test
   public void testTriangleGetVertexC()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(new Point(2,-2), t.getVertexC());
   }


   @Test
   public void testTriangleSetColor()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      t.setColor(Color.RED);
      assertEquals(Color.RED, t.getColor());
   }

   @Test
   public void testTriangleGetColor()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(Color.BLACK, t.getColor());
   }


   @Test
   public void testTriangleGetPerimeter1()
   {
      Triangle t = new Triangle(new Point (-1,2), new Point (-5,-5), new Point (2,-2), Color.BLACK);
      assertEquals(20.678030854162458, t.getPerimeter(), DELTA);
   }

   @Test
   public void testTriangleGetPerimeter2()
   {
      Triangle t = new Triangle(new Point (1,1), new Point (2,3), new Point (4,5), Color.BLACK);
      assertEquals(10.06449510224598, t.getPerimeter(), DELTA);
   }

   @Test
   public void testConvexPolygonGetVertex1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      assertEquals(new Point(4,5), p.getVertex(0));
   }

   @Test
   public void testConvexPolygonGetVertex2()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      assertEquals(new Point (1,1), p.getVertex(2));
   }

   @Test
   public void testConvexGetColor1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      assertEquals(Color.BLACK, p.getColor());
   }

   @Test
   public void testConvexSetColor1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      p.setColor(Color.RED);
      assertEquals(Color.RED, p.getColor());
   }

   @Test
   public void testConvexGetArea1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      assertEquals(7.0, p.getArea(), DELTA);

   }

   @Test
   public void testConvexGetPerimeter1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      assertEquals(11.72865690108165, p.getPerimeter(), DELTA);

   }

   @Test
   public void testConvexTranslate1()
   {
      ConvexPolygon p = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      p.translate(new Point(1,1));
     // ConvexPolygon exp = new ConvexPolygon(new Point[]{new Point (5,6), new Point (2,4), new Point (2,2), new Point (4,2)}, Color.BLACK);
      assertEquals(new Point (5,6), p.getVertex(0));
      assertEquals(new Point (2,4), p.getVertex(1));
      assertEquals(new Point(2,2), p.getVertex(2));
      assertEquals(new Point(4,2), p.getVertex(3));

   }


   @Test
   public void testWorkSpaceAreaOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), 
                 Color.BLACK));

      assertEquals(114.2906063, ws.getAreaOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpacePerimeterOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));
      assertEquals(61.09516775478293, ws.getPerimeterOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpaceGetSize()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));
      assertEquals(3, ws.size(), DELTA);
   }

   @Test
   public void testWorkSpaceGet()
   {
      WorkSpace ws = new WorkSpace();

      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      ws.add(r1);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));
      assertEquals(r1, ws.get(0));
   }

   @Test
   public void testWorkSpaceGetCircles()
   {
      WorkSpace ws = new WorkSpace();
      List<Circle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
                 Color.BLACK));
      ws.add(c2);

      expected.add(c1);
      expected.add(c2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getCircles());
   }

   @Test
   public void testWorkSpaceGetRectangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Rectangle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      Rectangle r2 = new Rectangle(1.4, 5.8, new Point(5, 6), Color.BLACK);

      ws.add(r1);
      ws.add(r2);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK));
      ws.add(new Circle(1.11, new Point(-5, -3), Color.RED));

      expected.add(r1);
      expected.add(r2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getRectangles());
   }

   @Test
   public void testWorkSpaceGetTriangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Triangle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Triangle t1 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK);
      Triangle t2 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
              Color.BLACK);

      ws.add(t1);
      ws.add(t2);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Rectangle(1.4, 5.8, new Point(5, 6), Color.BLACK));
      ws.add(new Circle(1.11, new Point(-5, -3), Color.RED));

      expected.add(t1);
      expected.add(t2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getTriangles());
   }

   @Test
   public void testWorkSpaceGetConvexPolygons()
   {
      WorkSpace ws = new WorkSpace();
      List<ConvexPolygon> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      ConvexPolygon p1 = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK);
      ConvexPolygon p2 = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.RED);

      ws.add(p1);
      ws.add(p2);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Rectangle(1.4, 5.8, new Point(5, 6), Color.BLACK));
      ws.add(new Circle(1.11, new Point(-5, -3), Color.RED));

      expected.add(p1);
      expected.add(p2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getConvexPolygons());
   }

   @Test
   public void testGetShapesByColor()
   {
      WorkSpace ws = new WorkSpace();
      List<Shape> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Circle c1 = new Circle(1.11, new Point(-5, -3), Color.RED);
      ConvexPolygon p1 = new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.RED);

      ws.add(c1);
      ws.add(p1);
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Rectangle(1.4, 5.8, new Point(5, 6), Color.BLACK));
      ws.add(new ConvexPolygon(new Point[]{new Point (4,5), new Point (1,3), new Point (1,1), new Point (3,1)}, Color.BLACK));

      expected.add(c1);
      expected.add(p1);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getShapesByColor(Color.RED));
   }

   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getRadius", "setRadius", "getCenter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getWidth", "setWidth", "getHeight", "setHeight", "getTopLeft");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testTriangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertexA", "getVertexB", "getVertexC");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class, Point.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Triangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testConvexPolygonImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertex");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[] {int.class});

      verifyImplSpecifics(ConvexPolygon.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   private static void verifyImplSpecifics(
      final Class<?> clazz,
      final List<String> expectedMethodNames,
      final List<Class> expectedMethodReturns,
      final List<Class[]> expectedMethodParameters)
      throws NoSuchMethodException
   {
      assertEquals("Unexpected number of public fields",
         0, clazz.getFields().length);

      final List<Method> publicMethods = Arrays.stream(
         clazz.getDeclaredMethods())
            .filter(m -> Modifier.isPublic(m.getModifiers()))
            .collect(Collectors.toList());

      assertEquals("Unexpected number of public methods",
         expectedMethodNames.size(), publicMethods.size());

      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodReturns.size());
      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodParameters.size());

      for (int i = 0; i < expectedMethodNames.size(); i++)
      {
         Method method = clazz.getDeclaredMethod(expectedMethodNames.get(i),
            expectedMethodParameters.get(i));
         assertEquals(expectedMethodReturns.get(i), method.getReturnType());
      }
   }


}


