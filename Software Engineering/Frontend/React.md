---
dg-publish: true
---
---

>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Intermediate React

## Managing State
https://react.dev/learn/managing-state

https://react.dev/
# Basic React

## 3 React Core Concepts
### Components
```js
//index.html

<script type="text/jsx">
  const app = document.getElementById("app")
 
  function Header() {
     return (<h1>Develop. Preview. Ship.</h1>)
   }
	function HomePage() {
	  return (
	    <div>
	      {/* Nesting the Header component */}
	      <Header />
	    </div>
	  );
	}
   

  const root = ReactDOM.createRoot(app);
  root.render(<HomePage />);
</script>

```

- Modular, reusable function that **returns UI elements**
- Capitalized functions to distinguish from plain HTML and JS
- To render components to the DOM, they are passed through the `root.render()` method
### Props
#### Displaying Data with Props
```js
<Header title = "React" />

function Header(props) {
	console.log(title) // { title: "React"}
}

// Object destructuring
function Header({ title }) {
	// Add {} to allow regular JavaScript directly inside JSX markup
	return <h1>{title}</h1>
}
```
- Used to pass information as properties to React components
- Props are passed as objects
#### Iterating Through Lists
```js
function HomePage() {
  const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];
 
  return (
    <div>
      <Header title="Develop. Preview. Ship." />
      <ul>
        {names.map((name) => (
          <li>{name}</li> 
          //<li key={name}>{name}</li>
          //key={name} is fine here because all the items in names are unique
        ))}
      </ul>
    </div>
  );
}
```

- If you run this code, React will give us a warning about a missing `key` prop. This is because React needs something to uniquely identify items in an array so it knows which elements to update in the DOM.
- Use item ID
### State
#### Interactivity with State through Event Handlers
```js
function HomePage() {
  // ...
 
  function handleClick() {
    console.log("increment like count")
  }
 
  return (
    <div>
      {/* ... */}
	  <button onClick={handleClick}>Like</button>
    </div>
     )
   }
```

#### State and Hooks
```js
const [state, setState] =  React.useState(0);
```

- Hooks allow you to add additional logic such as **state** to your components
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

### useEffect
```js
useEffect(()=>{
		   
}, [a,b]); // Runs again if a or b are different
```
- the Effect runs after the initial render and after re-renders with changed dependencies
- if no dependencies are given, it is re-rendered every time
- if an empty dependency array is given `[]`, it will only run after the initial render
## Rendering Lists
```javascript
ARRAY.map(x => 
	<li>{x}</li>
);
```

# Other
### Promise
- Object that represents the eventual completion/failure of an asynchronous operation and its resulting value
### Async function and await
- Use await in async functions. Async ensures the function returns a promise and wraps non promises in it
- await waits until promise settles and returns its result

### Async=Concurrency != Parallelism
- blocked vs at the same time
- 1 processor vs multiple processors
- Why it makes more sense to use asynchronous code for web API's
	- Many users but the serve is waiting for their not so good connection to send their requests
	- And then waiting again for the response to come back, resulting in lots of waiting
 - lots of waiting -> use concurrency
 - else -> parallelism
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
	setAge(a => a + 1); // setAge(42 + 1)  
	setAge(a => a + 1); // setAge(43 + 1)  
	setAge(a => a + 1); // setAge(44 + 1)
}
```




