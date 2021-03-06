# Harmonious

Harmonious is a cross-platform puzzle game written using the [Processing](https://processing.org/) library.

## Features

<details>
<summary>Graphing calculator</summary>
<br>
Well, kind of. Has support for second degree polynomial equations, with range from -10.0 to 10.0.
</details>

<details>
<summary>Beautiful animations</summary>
<br>
Beauty is subjective. But I think they're pretty cool.
</details>

<details>
<summary>Random level generator</summary>
<br>
Bored of the default levels? Create your own with customizable parameters!
</details>

## Installation

Head over to [releases](https://github.com/mizly/Harmonious/releases) and install the latest version with the instructions provided there. The latest version of [Java](http://java.com/download) is also required!

More advanced users who wish to modify the files directly should first install [Processing 3.5.4](https://github.com/processing/processing/releases/tag/processing-0270-3.5.4), then install [processing.py](https://github.com/jdf/processing.py), an extension for Processing that enables Python support. The code has not been tested on Processing 4+, so it is highly recommended to stay on Processing 3.5.4.

## Usage

Simply double click on the executable that is included within [releases](https://github.com/mizly/Harmonious/releases)!


## Known Bugs

<details>
<summary>Random level animation breaking</summary>
<br>
Specifically spamming the transition breaking the main level selection screen and the random level generator will sometimes cause a visual glitch.
</details>

<details>
<summary>Random level pass condition not met</summary>
<br>
Sometimes even when you get the correct answer, it might not register as such.
</details>

<details>
<summary>Pressing ESC closes the game</summary>
<br>
This isn't a bug but a built-in feature of Processing that has no way to be turned off.
</details>

## Cheat Codes
<details>
<summary>Games are hard. So you can find the solutions here!</summary>
<br> 
Level 1: 1   
<br>
Level 2: -2  
<br>
Level 3: 1, 1
<br>
Level 4: 3, -0.5
<br>
Level 5: 1, 0, 1
<br>
Level 6: -5, 9, 9
<br>
Level 7: 4, -9, -3
<br>
Level 8: -0.5, 1, -8.5

You're on your own for the random level. I probably don't know the answers either.
</details>

## Support
Get in touch with me at Mizly#1738 on Discord for support or bug reports.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Sources
This project would not be possible without the following:

[Processing reference](https://processing.org/reference/) - A general official wiki for everything Processing related. I used this extensively as Processing had lots of functions and methods that I would not be able to figure out otherwise.

[Stack Overflow](https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python) - Helped me figure out the screen resolution, which was useful for scaling the elements' positions and sizes.

[Stack Overflow (again)](https://stackoverflow.com/questions/68986409/inverting-colors-within-shape-in-processing) - Helped me figure out the invert colour effect using ```blendMode(DIFFERENCE)```, which applies the effect on an area defined by a shape.

[Processing Foundation Discourse](https://discourse.processing.org/t/blendmode-difference-in-p2d-p3d/17541) - Helped me figure out how to invert colour similarly to ```blendMode(DIFFERENCE)``` using P2D/P3D, an OpenGL powered graphics engine which could provide better performance.

[DelftStack](https://www.delftstack.com/howto/python/python-call-function-from-a-string/#:~:text=call%20the%20function.-,Use%20locals()%20and%20globals()%20to%20Call%20a%20Function,of%20the%20given%20source%20code.) - Helped me figure out how to call a function from a string name, which was useful as I had lots of repetitive function names like ```level1, level2, level3```, etc...

[Florida State University](https://www.math.fsu.edu/~rabert/TeX/parabola/parabola.html), [Math Stack Exchange](https://math.stackexchange.com/questions/3029005/drawing-bezier-curve-from-a-parabola) - Helped me figure out how to graph a degree 2 (parabola) polynomial equations using a bezier curve, which was necessary for the game to function properly.

Last but not least, big thanks to [Xiang](https://github.com/Rifltz) for helping me with some of the animations and giving valuable feedback!



