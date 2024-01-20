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

# Typescript
---
- **Static Checking**: Detects errors in code without running 
- The type system itself has no bearing on how your program runs
	- TS compiler erases types before producing compiled code
### Pitfalls of Javascript
- `(==)` coerces its operands
- JS allows accessing properties which aren't present instead of throwing an error
## Defining Types
- Primitive types
- boolean, bigint, null, number, string, symbol, undefined, any, unknown(ensure user declares the type), void(function with undefined return), never(it's not possible that this type could happen)
### Interface
```ts
interface User {
	name: string;
	id: number;
}

const user: User = {
	name: "Daisy",
	id: 0,
};

class UserAccount {
	name : string;
	id: number;

	constructor(name: string, id: number){
		this.name = name;
		this.id = id;
	}
}
const user: User = new UserAccount("Daisy", 0);

function f(x: number): number {

}
```
### Composing Types
- Union (combine types)
- `typeof s === `
```ts
type LockStates = "locked" | "unlocked";
function getLength(obj: string | string[]){
	return obj.length
}

Generics
type StringArray = Array<string>;
interface Backpack<Type> {
	add: (obj: Type) => void;
	get: () => Type;
}

//Shortcut to tell TS there is a constant called 'backpack'
//and to not worry about where it came from
declare const backpack: Backpack<string>;
const object = backpack.get();


```

### Structural Type System
- Type checking focuses on the shape that values have
- Shape-matching only requires a subset of the object's fields to match
- There is no difference between how classes and objects conform to shapes

### Optional Properties
```ts
interface Obj {
	x: number;
	status?: number;
}
```

# Related
