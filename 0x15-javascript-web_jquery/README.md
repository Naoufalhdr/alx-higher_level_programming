# 0x15. JavaScript - Web jQuery

## Description

This project involves learning how to use JavaScript and jQuery to manipulate the DOM, handle events, and make AJAX requests. You will work on a series of tasks that require you to dynamically modify HTML elements, style them, and interact with external APIs using jQuery.

## Learning Objectives

By the end of this project, you should be able to:

- Understand why jQuery makes front-end programming easier.
- Select HTML elements using JavaScript and jQuery.
- Differentiate between ID, class, and tag name selectors.
- Modify HTML element styles and content.
- Manipulate the DOM.
- Make GET and POST requests with jQuery AJAX.
- Bind and listen to DOM and user events.

## Requirements

- Editors: vi, vim, emacs
- Browser: Your files will be interpreted on Chrome (version 57.0)
- Code Style: Your code should be semistandard compliant with the flag `--global $: semistrand *.js --global`
- jQuery Version: Use jQuery version 3.x
- HTML Reload: HTML should not reload for each action; manipulate the DOM and update values dynamically
- README: A README.md file, at the root of the folder of the project, is mandatory

## Import jQuery

Include jQuery in your HTML files using the following script tag in the `<head>` section:

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## Tasks

### 0. No jQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). Use `document.querySelector` to select the HTML tag. Do not use the jQuery API.

**File:** 0-script.js

### 1. With jQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). Use the jQuery API and do not use `document.querySelector`.

File: 1-script.js

### 2. Click and turn red

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`. Use the jQuery API.

**File:** 2-script.js

### 3. Add .red class

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`. Use the jQuery API.

**File:** 3-script.js

### 4. Toggle classes

Write a JavaScript script that toggles the class of the `<header>` element between `red` and `green` when the user clicks on the tag `DIV#toggle_header`. Use the jQuery API.

**File:** 4-script.js

### 5. List of elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`. The new element must be `<li>Item</li>` and added to `UL.my_list`. Use the jQuery API.

**File:** 5-script.js

### 6. Change the text

Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`. Use the jQuery API.

**File:** 6-script.js

### 7. Star wars character

Write a JavaScript script that fetches the character name from the URL `https://swapi-api.alx-tools.com/api/people/5/?format=json` and displays it in the HTML tag `DIV#character`. Use the jQuery API.

**File:** 7-script.js

### 8. Star Wars movies

Write a JavaScript script that fetches and lists the title for all movies by using the URL `https://swapi-api.alx-tools.com/api/films/?format=json`. All movie titles must be listed in the HTML tag `UL#list_movies`. Use the jQuery API.

**File:** 8-script.js

### 9. Say Hello!

Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`. Use the jQuery API and ensure your script works when imported from the `<head>` tag.

**File:** 9-script.js

### 10. No jQuery - document loaded

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). Use `document.querySelector` to select the HTML tag. Ensure your script is imported from the `<head>` tag, not at the end of the HTML.

**File:** 100-script.js

### 11. List, add, remove

Write a JavaScript script that adds, removes, and clears `LI` elements from a list when the user clicks. The new element must be `<li>Item</li>` and added to `UL.my_list`. Use the jQuery API and ensure your script works when imported from the `<head>` tag.

**File:** 101-script.js

### 12. Say hello to everybody!

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language. Use the API service `https://www.fourtonfish.com/hellosalut/hello/`. The language code will be the value entered in the tag `INPUT#language_code`. The translation must be fetched when the user clicks on `INPUT#btn_translate` and displayed in the HTML tag DIV#hello. Use the jQuery API and ensure your script works when imported from the `<head>` tag.

**File:** 102-script.js

### 13. And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language. Use the API service `https://www.fourtonfish.com/hellosalut/hello/`. The language code will be the value entered in the tag `INPUT#language_code`. The translation must be fetched when the user clicks on `INPUT#btn_translate` or presses `ENTER` when the focus is on `INPUT#language_code`. The translation must be displayed in the HTML tag `DIV#hello`. Use the jQuery API and ensure your script works when imported from the `<head>` tag.

**File:** 103-script.js

## Author

This project is part of the ALX Software Engineering program.

- Name: [Naoufalhdr]
- GitHub: [https://github.com/Naoufalhdr/]
