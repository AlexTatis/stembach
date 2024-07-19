use std::{
    collections::HashMap,
    fs, sync::{Arc, Mutex},
};

use macroquad::prelude::*;
use rayon::prelude::*;
use square::Square;

mod square;

const UNIT_LENGTH: f32 = 50.0; // Real pixels of every square

#[macroquad::main("BasicShapes")]
async fn main() {
    let text = String::from("A");
    let scale_factor = 6.0 * text.chars().count() as f32; // Factor used for scaling every set into the current iteration font size

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

        for i in 0..5 {
            let tmp_set: Arc<Mutex<Vec<Square>>> = Arc::new(Mutex::new(vec![]));

            union_set.par_iter_mut().for_each(|set|for (char_index, character) in text.chars().enumerate() {
                let bitmap: &Vec<u8> = font
                    .get(&character.to_string())
                    .expect("[!]: Character not recognized. Check the string given");

                for (row_index, bit) in bitmap.into_iter().enumerate().rev() {
                    for column_index in 0..5 {
                        if (bit >> column_index & 1) != 0 {
                            let mut tmp = set.clone();

                            tmp.scale(1.0 / scale_factor);

                            tmp.translate(Vec2::new(
                                UNIT_LENGTH / scale_factor.powi(i)
                                    * (column_index + char_index * 7) as f32,
                                UNIT_LENGTH / scale_factor.powi(i) * (12 - row_index) as f32,
                            ));

                            tmp_set.lock().unwrap().push(tmp);
                        }
                    }
                }
            });

            union_set = Arc::try_unwrap(tmp_set).unwrap().into_inner().unwrap();
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
