---
dg-publish: true
---
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Pure React



## React Api/Dom
ReactDOM is needed to mount our application in the browser
Both React and ReactDOM are available over a CDN.

```html
<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
```

## React Components
### Function Component
- must return market (which is what React.createElement generates)
- component render functions have to be fast (called a lot)
- state can't be modified inside render function
	- this function must be pure. You don't know how or when the function will be called so it can't modify any ambient state.
- `React.createElement`   creates one instance of some component
		 - If you pass it a string, it will create a DOM tag with that as the string
		 - Second component  = attributes of tag/component (ie: id or even null)
- `document.getElementById` grabs existing element out of HTML document
- `ReactDOM.createRoot(container)` signals to React where we want it to render our app
- `App` is a class of components and we need to render one instance of a class
### Class Component

# Related
