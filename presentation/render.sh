#!/bin/bash

uv run manim main.py FractalPres --disable_caching && uv run manim-slides FractalPres --hide-info-window
