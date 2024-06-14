use macroquad::prelude::*;

#[derive(Debug, Clone, Copy)]
struct Rectangle {
    x: f32,
    y: f32,
    w: f32,
    h: f32,
    color: Color,
}

impl Rectangle {
    fn draw(&self) {
        draw_rectangle(
            self.x,
            screen_height() - self.y - self.h,
            self.w,
            self.h,
            self.color,
        )
    }

    fn new(x: f32, y: f32, w: f32, h: f32, color: Color) -> Self {
        Self { x, y, w, h, color }
    }

    fn rotate(&mut self, angle: f32) {

        let v_center = Vec2::new(self.x + self.w / 2.0, self.y + self.h / 2.0);
        let rotation = Affine2::from_angle_translation(angle, v_center);

        let v = rotation.transform_point2(Vec2::new(self.x, self.y) - v_center);

        self.x = v.x;
        self.y = v.y;
    }

    fn translate(&mut self, v: Vec2) {
        self.x += v.x;
        self.y += v.y;
    }

    fn scale(&mut self, n: f32) {
        self.w *= n;
        self.h *= n;
    }
}

fn transform_1(rectangle: &mut Rectangle) {
    rectangle.translate(Vec2::new(0.0, rectangle.h));
    rectangle.rotate(45.0);
}


#[macroquad::main("BasicShapes")]
async fn main() {
    loop {
        clear_background(BLACK);

        let mut union_set = vec![Rectangle::new(0.0, 0.0, 60.0, 60.0, GREEN)];

        for set in &mut union_set {
            transform_1(set);
        }

        for set in union_set {
            set.draw();
        }

        draw_text(
            "IFS Attractor - Alejandro Campo & Álvaro Vázquez",
            20.0,
            20.0,
            30.0,
            WHITE,
        );

        next_frame().await
    }
}
