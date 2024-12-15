# Mandelbrot Set Visualization

This repository contains code for generating and visualizing the Mandelbrot set using Python. The visualization is created by iterating over complex numbers and applying color schemes based on the convergence of the iterations.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Mandelbrot set is a two-dimensional set with a relatively simple definition that exhibits great complexity, especially as it is magnified. It is popular for its aesthetic appeal and fractal structures. The set is defined in the complex plane as the complex numbers c for which the function f_c(z) = z^2 + c does not diverge to infinity when iterated starting at z=0, i.e., for which the sequence f_c(0),f_c(f_c(0)), etc., remains bounded in absolute value.

## Installation
To run the code in this repository, you need to have Python installed. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/RaviMosalpuri/MandelbrotSet.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MandelbrotSet
    ```
3. Run the Python script:
    ```bash
    python MandelbrotSet.py
    ```
4. The generated image will be saved as `output.png` in the project directory.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References:
1. https://medium.com/swlh/visualizing-the-mandelbrot-set-using-python-50-lines-f6aa5a05cf0f
2. https://www.geeksforgeeks.org/mandelbrot-fractal-set-visualization-in-python/
3. https://en.wikipedia.org/wiki/Mandelbrot_set

## Output image:
![output_powercolor](https://github.com/user-attachments/assets/f159f056-ac02-441c-8c03-3c207785947e)
