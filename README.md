# Wordie - online dictionary

Wordie is an online dictionary powerd by owlbot english dictionary api and python flask framework

## Description

On the main file there there are 2 functions. The 'home' function is going to get the 'index.html' file from the 'templates' folder when user first visit the website and if user enter a word to the input box and press search button or press enter in the keybaord using 'POST' method the program receive the word from the form call the look_up method and pass the data it received from theat function and pass it to the webpage as a variable. Second function gets the word from the user and look it up using 'request' package and return it as a json data format.

For the 'index.html' file in the templates folder there aren't any external css file because i've used bootstrap to style it. There is navigation bar only with a tile. After that there is a form to collect the word from the user. In the bottom there is  another colum to show the title, image and the description from the json data.

### Preview

<img src="https://user-images.githubusercontent.com/91461938/208255125-c838e019-fc6e-4fef-9355-6a5ec5901828.gif">
