<h1 align="center">WordSearchGenerator</h1>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## About ##

This proyect is a simple Word Search Generator written in python. It creates randomized word search puzzle in a square matrix

## Features ##

  * **Generating a matrix :** it creates a square grid to serve as the puzzle board.

  * **Placing words :** akes a list of words from a text file (words.txt) and randomly places them in the matrix in different directions:

    * Up to Down (vertical, top-to-bottom)
    * Down to Up (vertical, bottom-to-top)
    * Left to Right (horizontal, left-to-right)
    * Right to Left (horizontal, right-to-left)
    * Diagonals (planned for future implementation)

  * **Adjusting Dificulty :** Offers 4 difficulty levels that determine how many directional placements are used 
    * Level 1 = only vertical
    * Level 2 = vertical + reverse vertical
    * Level 3 = all 4 directions
    * Level 4 = all directions including diagonals [ **TODO** ]

  * **Filling empty spaces :** After placing words, it fills any remaining empty cells with random characters extracted from the word list to create a complete puzzle.

## Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)

## License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with by <a href="https://github.com/unisonos" target="_blank">Unisonos</a>

&#xa0;

