---
dg-publish: true
tags: 
created: ""
---
---

>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Next.js
- File-system based router built on top of Server Components
- Client-side and Server-side rendering with client and server components
- Data fetching with async/await in Server components
- Uses page.tsx is equivalent to index.html
- Next.js uses file-system routing. Instead of using code to define the routes of your application, you can use folders and files
### File Structure
```js
/Project
index.html
main.js
app/
	layout.tsx  
	page.tsx
components/
	feature/
		feature.tsx
		feature.module.css
```



## Routing
![[Pasted image 20240116214405.png]]
![[Pasted image 20240116214420.png]]

- `page.js` makes route segments publicly accessible
### Route Handlers
 - Allow you to create custom request handlers for a given route using Web Request and Response API's

### Dynamic Routes
- Dynamic Segment: created by wrapping a folder's name in square brackets (`[data]`)
- Dynamic Segments are passed as the `params` prop to `layout`, `page`, `route` functions
- Catch-all segments, ie:`shop/[...slug]/page.js` matches `shop/.+`
- Optional Catch-all Segments, ie: `shop/[[...slug]]/page.js` matches `shop/*`
#### route.js
- `export async function GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS(request: Request){}`
- Route Handlers can be nested inside of `app` but there can't be a `route.js` file at the same route segment level as `page.js`
### Error Handling
- https://nextjs.org/docs/app/building-your-application/routing/error-handling

## Layouts
- UI shared between multiple pages
- Define a layout by `default exporting` a React component from a `layout.js` file
- The component should accept a `children` prop that will be populated with a child layout (if it exists) or a child page during rendering
```ts
export default function DashboardLayout({
  children, // will be a page or nested layout
}: {
  children: React.ReactNode
}) {
  return (
    <section>
      {/* Include shared UI here e.g. a header or sidebar */}
      <nav></nav>
 
      {children}
    </section>
  )
}
```

- A root layout is the top most layout in the root app directory used to define the <`html`> and <`body`> tags and other globally shared UI
- Properties of layouts:
	- Persist across routes and maintain state
### Templates
- Similar to layouts in that they wrap each child layout/page
- Differences to layouts: 
	- Templates create a new instance for each of their children on navigation
	- New instance of component is mounted, DOM elements recreated, state is not preserved, effects are re-synchornized
- Applications of Templates
	- Features that rely on useEffect and useState (per page feedback form, logging page views)

## Linking and Navigation
### `<Link>` Component 
- extends the HTML `<a>` tag
```ts
import Link from 'next/link'
 
export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}
```


## Server Side Rendering vs Client Side Rendering
https://yudhajitadhikary.medium.com/client-side-rendering-vs-server-side-rendering-in-react-js-next-js-b74b909c7c51


### Server Components
- 

# Javascript Essentials

### Functions
```js
function f(x){
	x = 1 //no effects globally
	x = {num: 1} //no effects globally
	x.num = 1 //affects parameter
}

Function Expressions + Closures
const f = function c(x){
	return x > 0 ? c(x-1) : 0
};

const createPet = function (name) {
  let sex;

  const pet = {
    // setName(newName) is equivalent to setName: function (newName)
    // in this context
    setName(newName) {
      name = newName;
    },

    getName() {
      return name;
    },

    getSex() {
      return sex;
    },

    setSex(newSex) {
      if (
        typeof newSex === "string" &&
        (newSex.toLowerCase() === "male" || newSex.toLowerCase() === "female")
      ) {
        sex = newSex;
      }
    },
  };

  return pet;
};

const pet = createPet("Vivie");
console.log(pet.getName()); // Vivie

pet.setName("Oliver");
pet.setSex("male");
console.log(pet.getSex()); // male
console.log(pet.getName()); // Oliver



```

- Items are always passed by "value"
- But the item that is passed by value is itself a reference ("call-by-sharing")
- If the parameter itself was changed, nothing would happen
- If the internals of the parameter were changed, it would propagate back up

### Arguments Object
- arguments of a function can be addressed as `arguments[i]`

```javascript
array.map((currElement, index, array) -> {

});
```

### Arrow Functions
- non-binding `this`
- An arrow function does not have its own `this`; the `this` value of the enclosing execution context is used. Thus, in the following code, the `this` within the function that is passed to `setInterval` has the same value as `this` in the enclosing function:

```js
function Person() {
  this.age = 0;

  setInterval(() => {
    this.age++; // `this` properly refers to the person object
  }, 1000);
}

const p = new Person();

```

## Arrays
- All standard built-in copy operations with any Javascript Objects create shallow copies

```js
const fruits = [];
fruits.push("a","b","c")
fruits[5] = "e"
console.log(Object.keys(fruits)); // ['0','1','2','5']
console.log(fruits.length); // 6

fruits.length = 10;
// empty slots such as fruits[8] empty (not even undefined)
// decreasing the length deletes elements


## For Each
colors.forEach((item, index) => {
  console.log(`${index}: ${item}`);
});
```

## Misc JS
### Template Literals
``` `some text ${expression}` ```
- Escape backtick in template literal by prefixing with `\`
- Newline characters inserted in the source are part of the template literal

### Ternary Operator
```js
const x = c1 ? val1 
	: c2 ?  val 2
	: c3 ? val 3
```
- can be chained

## ES Modules

### File Structure
```js
index.html
main.js
modules/
    canvas.js
    square.js
```

### Exporting Module Features
- Mark items with export if needed to be exported out of the module
- Only top level items can be exported

```js
export const name = "s";

export function f(){
}

//convenient end of file export
export { name, f};

```

### Importing features into your script
```js
import { name, f} from "./modules/feature.js";

## Using an import map to resolve module specifiers to urls

import { name, f } from "feature";


// Must be declared before any script elements that import modules
// Only applies to the current document
<script type="importmap">
  {
    "imports": {
      "shapes": "./shapes/square.js",
      "shapes/square": "./modules/shapes/square.js",
      "https://example.com/shapes/square.js": "./shapes/square.js",
      "https://example.com/shapes/": "/shapes/square/",
      "../shapes/square": "./shapes/square.js"
    }
  }
</script>


```

# HTML

- HTML tags can have custom data attribute prefixed with data-*