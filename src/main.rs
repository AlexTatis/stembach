use std::{
    collections::HashMap,
    fs::{self},
};

use macroquad::prelude::*;
use square::Square;

mod square;

const UNIT_LENGTH: f32 = 40.0; // Real pixels of every square

struct Font {
    json: HashMap<String, Vec<u8>>,
}

impl Font {}

#[macroquad::main("BasicShapes")]
async fn main() {
    let text = String::from("BI-Gas");

    let file = fs::read_to_string("monogram-bitmap.json").expect("[!]: Font not found");
    let font: HashMap<String, Vec<u8>> =
        serde_json::from_str(file.as_str()).expect("[!]: Error on json desirialization");

    loop {
        clear_background(BLACK);

        let mut union_set = vec![square::Square::new(
            0.0,
            0.0,
            UNIT_LENGTH * 6.0 * text.chars().count() as f32,
            0.0,
            GREEN,
        )];

        for _i in 0..2 {
            
            let mut tmp_set: Vec<Square> = vec![];
            
            for set in &mut union_set {
                set.scale(1.0 / (6.0 * text.chars().count() as f32));

                for (char_index, character) in text.chars().enumerate() {
                    let bitmap: &Vec<u8> = font
                        .get(&character.to_string())
                        .expect("[!]: Character not recognized. Check the string given");

                    for (row_index, bit) in bitmap.into_iter().enumerate().rev() {
                        for column_index in 0..5 {
                            if (bit >> column_index & 1) != 0 {
                                let mut tmp = set.clone();

                                tmp.translate(Vec2::new(
                                    UNIT_LENGTH * (column_index + char_index * 7) as f32,
                                    UNIT_LENGTH * (12 - row_index) as f32,
                                ));

                                tmp_set.push(tmp);
                            }
                        }
                    }
                }
            }
        union_set = tmp_set;
        }


        union_set.into_iter().for_each(|x| x.draw());

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
