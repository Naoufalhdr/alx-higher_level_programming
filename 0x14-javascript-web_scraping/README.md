# 0x14. JavaScript - Web Scraping

## Description

This project involves web scraping using JavaScript. You will learn how to read and manipulate JSON data, use the `request` and `fetch` APIs, and read/write files using the `fs` module. This project aims to provide practical experience with web scraping and handling JSON data in JavaScript.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why JavaScript programming is amazing.
- Manipulate JSON data.
- Use the `request` and `fetch` APIs.
- Read and write files using the `fs` module.

## Requirements

- **Editors**: vi, vim, emacs
- **Node Version**: All scripts will be interpreted on Ubuntu 20.04 LTS using Node (version 14.x)
- **Coding Style**: Your code should be semistandard compliant. Use the AirBnB style guide and ensure semicolons are used.
- **File Requirements**: 
  - All files should end with a new line.
  - The first line of all your files should be `#!/usr/bin/node`.
  - All files must be executable.
  - The length of your files will be tested using `wc`.
  - Do not use `var`.

## Setup

### Install Node 14

```sh
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

```sh
$ sudo npm install semistandard --global
```

### Install request module

```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Readme

Write a script that reads and prints the content of a file.

- **File**: `0-readme.js`
- **Usage**: 
  ```sh
  ./0-readme.js <file path>
  ```

### 1. Write me

Write a script that writes a string to a file.

- **File**: `1-writeme.js`
- **Usage**: 
  ```sh
  ./1-writeme.js <file path> "<string>"
  ```

### 2. Status code

Write a script that displays the status code of a GET request.

- **File**: `2-statuscode.js`
- **Usage**: 
  ```sh
  ./2-statuscode.js <URL>
  ```

### 3. Star wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- **File**: `3-starwars_title.js`
- **Usage**: 
  ```sh
  ./3-starwars_title.js <movie ID>
  ```

### 4. Star wars Wedge Antilles

Write a script that prints the number of movies where the character "Wedge Antilles" is present.

- **File**: `4-starwars_count.js`
- **Usage**: 
  ```sh
  ./4-starwars_count.js <API URL>
  ```

### 5. Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

- **File**: `5-request_store.js`
- **Usage**: 
  ```sh
  ./5-request_store.js <URL> <file path>
  ```

### 6. How many completed?

Write a script that computes the number of tasks completed by user ID.

- **File**: `6-completed_tasks.js`
- **Usage**: 
  ```sh
  ./6-completed_tasks.js <API URL>
  ```

### 7. Who was playing in this movie? (Advanced)

Write a script that prints all characters of a Star Wars movie.

- **File**: `100-starwars_characters.js`
- **Usage**: 
  ```sh
  ./100-starwars_characters.js <movie ID>
  ```

### 8. Right order (Advanced)

Write a script that prints all characters of a Star Wars movie in the same order of the list "characters" in the `/films/` response.

- **File**: `101-starwars_characters.js`
- **Usage**: 
  ```sh
  ./101-starwars_characters.js <movie ID>
  ```

## Author

- Written by [Naoufalhdr]

## License

- This project is licensed under the [ALX Program](https://www.alxafrica.com/).

## Acknowledgments

- Special thanks to the ALX community for their continuous support and guidance.
