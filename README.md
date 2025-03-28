# 🐢 Turtle Spirograph

A colorful spirograph generator created with Python's Turtle graphics module.

## 📝 Description

This fun little project uses Python's Turtle graphics to create beautiful, colorful spirograph patterns. Each circle in the spirograph is drawn with a random color, creating a mesmerizing visual effect.

## ✨ Features

- 🌈 Random colors for each circle
- 🔄 Customizable angle increments
- 🖼️ Beautiful circular patterns
- 🖱️ Click to exit when you're done enjoying the art

## 🚀 How to Run

1. Make sure you have Python installed on your system
2. No additional packages needed - the project uses built-in modules
3. Run the program:
   ```
   python main.py
   ```
4. Click anywhere on the window to exit when the drawing is complete

## 🛠️ Customization

You can easily customize the spirograph by modifying the parameters in `main.py`:

- Change the `degree` parameter in the `spirograph()` function call to adjust the angle between circles
- Modify the circle radius (currently set to 100) in the `tim.circle(100)` line
- Adjust the turtle's speed, pensize, or starting color

## 🔄 How It Works

The program creates a spirograph by drawing circles at different angles. For each iteration, it:

1. Selects a random RGB color
2. Draws a complete circle
3. Rotates by the specified angle
4. Repeats until a full 360° rotation is achieved

Enjoy creating your own mathematical art! 🎨
