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

# Rendering
## Server Side Rendering 
https://yudhajitadhikary.medium.com/client-side-rendering-vs-server-side-rendering-in-react-js-next-js-b74b909c7c51
### Server Components
By default, Next.js uses server components
- **Performance**: Can be cached on server
	- Moves data fetching to server, closer to data source (improve performance by reducing fetching time and # of requests client makes)
- **Secure**: Keep sensitive data on server
- **Initial Page Load and First Contentful Paint (FCP)**: Generate HTML on the server to allow users to view the page immediately instead of waiting for client to download/parse/execute JS 
- **Streaming**: Allow rendering to be split into chunks and streamed to client as they become ready
#### Server Components Rendering Process
- Work is split into chunks
- Chunk rendered in two steps:
	- React renders server components into **React Server Component Payload(RSC Payload)**
	- Next.js uses RSC Payload and Client Component JS instructions to render HTML on the server
- Then on the client:
	- HTML is used immediately to show a fast non interactive preview of the route (on initial page load only)
	-  RSC Payload used to reconcile the Client and Server Component trees, and update DOM
	- JS instructions are used to hydrate ("attach" React to existing HTML rendered by React in a server environment) Client Components and make app interactive
### Static Rendering
- Routes are rendered at **build time** or in the background after data revalidation
- Result is cached and can be pushed to a Content Delivery Network(CDN)

> [!info]+ Content Delivery Network (CDN)
> A group of servers spread out over many locations. These servers store duplicate copies of data so that servers can fulfill data requests based on which servers are closest to the respective end-users. CDNs make for fast service less affected by high traffic.

### Dynamic Rendering
- Routes are rendered for each user at request time
- Useful when route has data that is personalized to the user
### Streaming
https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming
- Use `loading.js` and UI components with **React Suspense**
## Client Components
- Allow interactivity (use states, effects, event listeners)
- Have access to browser APIs: geolocation, localStorage

## Caching
| Mechanism | What | Where | Purpose | Duration |
| ---- | ---- | ---- | ---- | ---- |
| [Request Memoization](https://nextjs.org/docs/app/building-your-application/caching#request-memoization) | Return values of functions | Server | Re-use data in a React Component tree | Per-request lifecycle |
| [Data Cache](https://nextjs.org/docs/app/building-your-application/caching#data-cache) | Data | Server | Store data across user requests and deployments | Persistent (can be revalidated) |
| [Full Route Cache](https://nextjs.org/docs/app/building-your-application/caching#full-route-cache) | HTML and RSC payload | Server | Reduce rendering cost and improve performance | Persistent (can be revalidated) |
| [Router Cache](https://nextjs.org/docs/app/building-your-application/caching#router-cache) | RSC Payload | Client | Reduce server requests on navigation | User session or time-based |
### Request Memoization (React Feature)
- Extends `fetch` API
- Allows you to call a fetch function for the same data in multiple places in a React component tree while only executing it once
```ts
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch('https://.../item/1')
  return res.json()
}
 
// This function is called twice, but only executed the first time
const item = await getItem() // cache MISS
 
// The second call could be anywhere in your route
const item = await getItem() // cache HIT
```

### Request Memoization 

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