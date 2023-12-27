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

## JSX
- JS vs JSX
	- class - className
	- for - htmlFor

## Hooks
- when you type in input, React detects that a DOM event happens
- React then thinks something may have changed and runs a re-render. 
- **hook**: gets caught every time render function gets called. Are stateful
- hooks rely on strict ordering (they are called in the same order every single time)
	- all hooks have to run on each render
- **do not put hooks inside if statements or loops**
- `const [state, setState] = useState(initialState);`
- hooks can only be used in functional components not class components
### Updating Objects/Arrays in state
- States are read-only in React
- **Replace** rather than **mutate** existing objects

```js
const [form, setForm] = useState({
firstName: 'Barbara',
lastName: 'Hepworth',
email: 'bhepworth@sculpture.com',
});
  
<input
  value={form.firstName}
  onChange={e => {
	setForm({
	  ...form, 
	  firstName: e.target.value
	});
  }}
/>
```
**Note: syntax ...form**

### Avoid recreating initial state
- Pass function instead of calling it
```js
const [todos, setTodos] = useState(createInitialTodos()); 
const [todos, setTodos] = useState(createInitialTodos); 
```
## Rendering Lists
```javascript
ARRAY.map(x => 
	<li>{x}</li>
);
```


# Other
### Array destructuring
`const [x,y] = f();`
### Updater function
```js
function handleClick() {  
	setAge(age + 1); // setAge(42 + 1)  
	setAge(age + 1); // setAge(42 + 1)  
	setAge(age + 1); // setAge(42 + 1)
}
function handleClick() {  
	setAge(age => age + 1); // setAge(42 + 1)  
	setAge(age => age + 1); // setAge(42 + 1)  
	setAge(age => age + 1); // setAge(42 + 1)
}
```
