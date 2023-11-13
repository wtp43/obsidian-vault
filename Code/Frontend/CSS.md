---
dg-publish: true
---
>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# HTML¢

## Tags

### Header
`<h1> This is the title </h1>`
	- Headers go up to h6

### Paragraph
`<p> Hello World </p>` 
	- paragraph: only text goes in here

### Anchor
`<a href="https://www.google.com"> Google </a>`
	- Anchor: a link to somewhere else

### Division
 ```css
 <div style="width: 100px; height: 100px; background-color: red;"></div>
```
<div style="width: 100px; height: 100px; background-color: red;"></div>
	- Division: Generic container tag for grouping together other things. 

### Span
```css
<p> This is <span style= "text-decoration: underline"> Important</span> </p>
```
<p> This is <span style= "text-decoration: underline"> Important</span> </p>
	- Span: Container for text


### Lists
`<ol>, <ul>, <li>`
	- Ordered list, unordered Iist, list item

### Button
```css
<button> Enter </button>
```
<button> Enter </button>

### Image
```css
<img src="http://pets-images.dev-apis.com/pets/dog25.jpg"
	alt="an adorable puppy"/>
```

<img src="http://pets-images.dev-apis.com/pets/dog25.jpg"
	alt="an adorable puppy"/>
	 - img tags are self closing

### Input and Textarea
```css
<input />
<input type="color" />
```
<input  
/>
<input type="color">
input tags are self closing, types: text, color, file, number, datetime-local, radio, checkbox

`<textarea> </textarea>`
	- Same as input but for more text


### Select and option
```css
<select>
	<option value="seattle">Seattle </option>
	<option value="new york">New York </option>
</select>
```
<select>
	<option value="seattle">Seattle </option>
	<option value="new york">New York </option>
</select>
	- Select and options 

### Form
`<form>`
	`<input placeholder= "Num 1"/>`
	`<textarea id="response"> <textarea>
`</form>`
	- Form: Group of html tags 

### Table
```css
<table>
  <tbody>
    <tr>
      <td>(0,0)</td>
      <td>(1,0)</td>
    </tr>
    <tr>
      <td>(0,1)</td>
      <td>(1,1)</td>
    </tr>
  </tbody>
</table>
```
<table>
  <tbody>
    <tr>
      <td>(0,0)</td>
      <td>(1,0)</td>
    </tr>
    <tr>
      <td>(0,1)</td>
      <td>(1,1)</td>
    </tr>
  </tbody>
</table>

### Navbar
```css
<nav>
  <ul class="nav-list">
    <li class="nav-list-item">
      <a class="nav-link" href="/">Home</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/news">Newsfeed</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/about">About</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/contact">Contact</a>
    </li>
  </ul>
</nav>
```
<nav>
  <ul class="nav-list">
    <li class="nav-list-item">
      <a class="nav-link" href="/">Home</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/news">Newsfeed</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/about">About</a>
    </li>
    <li class="nav-list-item">
      <a class="nav-link" href="/contact">Contact</a>
    </li>
  </ul>
</nav>
	- unordered list can be replaced using divs inside of divs and use classes to differentiate them

## HTML Examples
### Blog Post

```html
<div class="social-feed">

  <div class="social-post">
    <h2 class="user-name">@sassy_pants_mcgee</h2>
    <h3 class="posted-date">Posted 15m ago</h3>
    <img
         class="profile-picture"
         src="http://pets-images.dev-apis.com/pets/dog25.jpg"
         alt="a doggy"
         style="width:128px;height:128px;"
         /
    <p class="social-post-text">
      Doggy 1.
    </p>
  </div>
  
  <div class="social-post">
    <h2 class="user-name">@TailCurious</h2>
    <h3 class="posted-date">Posted 18m ago</h3>
    <img
         class="profile-picture"
         src="http://pets-images.dev-apis.com/pets/dog26.jpg"
         alt="a different doggy"
         style="width:128px;height:128px;"
         />
    <p class="social-post-text">
      Doggy 2.
    </p>
  </div>
  
</div>
```

<div class="social-feed">

  <div class="social-post">
    <h2 class="user-name">@sassy_pants_mcgee</h2>
    <h3 class="posted-date">Posted 15m ago</h3>
    <img
         class="profile-picture"
         src="http://pets-images.dev-apis.com/pets/dog25.jpg"
         alt="a doggy"
         style="width:128px;height:128px;"
         />
    <p class="social-post-text">
      Doggy 1.
    </p>
  </div>
  
  <div class="social-post">
    <h2 class="user-name">@TailCurious</h2>
    <h3 class="posted-date">Posted 18m ago</h3>
    <img
         class="profile-picture"
         src="http://pets-images.dev-apis.com/pets/dog26.jpg"
         alt="a different doggy"
         style="width:128px;height:128px;"
         />
    <p class="social-post-text">
      Doggy 2.
    </p>
  </div>
  </div>


## Structure of HTML document

```html
<!DOCTYPE html>
<html lang="en">

	<head> 
		<meta charset="UTF-8" /> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
		<title>My Blog</title> 
	</head> 
		
	<body> 
		<!-- all your content will go here --> 
		<a href="another-page.html">About</a>
	</body>

</html>
```
- `<html lang="en"></html>`
	- root tag
- `<head></head>`
	- contains all meta data: character sets, browser resizing, where css is located, favicon
- `<meta>`
	- - `name="viewport" content="width=device-width, initial-scale=1.0"` - Lets browser know how to handle mobile devices like phones and small tablets. Otherwise browser may output a really zoomed out view of your website. 
- `<title></title>`
	- Title of browser tab


## Attributes
- `class`, `id` are universal and can be applied to nearly all tags
- `class` is more useful than `id` because it is reusable
- `id` is unique. Use sparingly and only when you want to make sure something stays unique


## Some notes on HTML
- Split ext using `p` tags


# External CSS/JS

## Referencing CSS/JS
```html
<html>

 <head>
   <link rel="stylesheet" href="styles.css">
 </head>
 
 <body>
   <h3>External CSS</h3>
   <script src="myJSscript.js"></script>
 </body>
</html>
```

- External script references can be placed in the head or body. 
- Imported script will behave as if it was written exactly where the `<script>` tag is located



```css
<style>
	.red-style {
		color: red;
	}
</style>
```

