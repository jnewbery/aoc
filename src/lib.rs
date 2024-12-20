pub mod utils {
    
    #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
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
}
