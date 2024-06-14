use macroquad::prelude::*;
use std::f32::consts::SQRT_2;

#[derive(Debug, Clone, Copy)]
pub struct Square {
    x: f32,
    y: f32,
    l: f32,
    angle: f32,
    color: Color,
}

impl Square {
    pub fn draw(&self) {
        draw_poly(
            self.x + self.l / 2.0,
            screen_height() - self.y - self.l / 2.0,
            4,
            self.l / SQRT_2,
            self.angle,
            self.color,
        )
    }

    pub fn new(x: f32, y: f32, l: f32, angle: f32, color: Color) -> Self {
        Self {
            x,
            y,
            l,
            angle: angle + 45.0,
            color,
        }
    }

    pub fn rotate(&mut self, angle: f32) {
        self.angle += angle;
    }

    pub fn translate(&mut self, v: Vec2) {
        self.x += v.x;
        self.y += v.y;
    }

    pub fn scale(&mut self, n: f32) {
        self.l *= n;
    }
}
