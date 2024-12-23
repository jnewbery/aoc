pub mod utils {
    use std::fmt;
    
    #[derive(Clone, Copy, PartialEq, Eq, Hash, Ord, PartialOrd)]
    pub struct Point {
        pub x: i32,
        pub y: i32,
    }

    // Implement addition on Point
    impl std::ops::Add for Point {
        type Output = Point;

        fn add(self, other: Point) -> Point {
            Point { x: self.x + other.x, y: self.y + other.y }
        }
    }

    // Implement multiplication by a scalar on points (i32, i32)
    impl std::ops::Mul<i32> for Point {
        type Output = Point;

        fn mul(self, scalar: i32) -> Self {
            Point { x: self.x * scalar, y: self.y * scalar }
        }
    }

    // Implement scalar multiplication on points (i32, i32)
    impl std::ops::Mul<Point> for i32 {
        type Output = Point;

        fn mul(self, point: Point) -> Point {
            Point { x:self * point.x, y:self * point.y }
        }
    }

    impl Point {
        pub fn turn_left(&self) -> Point {
            Point { x: -self.y, y: self.x }
        }

        pub fn turn_right(&self) -> Point {
            Point { x: self.y, y: -self.x }
        }
    }

    // Implement print for maze
    impl fmt::Debug for Point {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "({}, {})", self.x, self.y)?;
            Ok(()) // Return success
        }
    }

    #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Ord, PartialOrd)]
    pub struct Position {
        pub location: Point,
        pub direction: Point,
    }

    impl Position {
        pub fn new(location: Point, direction: Point) -> Self {
            Position { location, direction }
        }

        pub fn turn_left(&self) -> Self {
            Position { location: self.location, direction: self.direction.turn_left() }
        }

        pub fn turn_right(&self) -> Self {
            Position { location: self.location, direction: self.direction.turn_right() }
        }

        pub fn forward(&self) -> Self {
            Position { location: self.location + self.direction, direction: self.direction }
        }
    }
}
