---
dg-publish: true
---
# Building Blocks of a Web Application

There are a few things you need to consider when building modern applications. Such as:

- **User Interface** - how users will consume and interact with your application.
- **Routing** - how users navigate between different parts of your application.
- **Data Fetching** - where your data lives and how to get it.
- **Rendering** - when and where you render static or dynamic content.
- **Integrations** - what third-party services you use (CMS, auth, payments, etc) and how you connect to them.
- **Infrastructure** - where you deploy, store, and run your application code (Serverless, CDN, Edge, etc).
- **Performance** - how to optimize your application for end-users.
- **Scalability** - how your application adapts as your team, data, and traffic grow.
- **Developer Experience** - your team’s experience building and maintaining your application.

# Frameworks
- Used to build apps
## MVC Architecture
### Model
- Stores info about content/structure of app
- Upon receiving user input data from the Controller, it communicates any required interface updates to the View component.
### View
- App's front-end
- View receives user input, communicates it to the controller for processing
- Updates itself according to instructions from Model
### Model
- Receives user input from view and modifies Model 
## Isomorphic Frameworks
- Frameworks that support both front end and back end 
- Lazo.js, meteor.js, Rendr



# Microservice Architecture
 Architectural style that structures an application as a collection of services that are
![[Pasted image 20231108174314.png]]


# Front-end

## React
- Meta React frameworks
	- Next.js: A React framework that gives you building blocks to create web applications. By framework, we mean Next.js handles the tooling and configuration ...
- React is a component-based front-end library responsible only for the view layer of the application
### Next.js
- Next.js is a complete full-stack framework built on top of React.js. You can use Next.js to create basic blog websites up to full-blown, full-stack applications and APIs.

Next.js is a react server side framework, which some advantages. But its main selling point is that it renders react server side.
It’s also built on top of Nodejs, so you could refer to it as a node js framework as well.
Nodejs on the other hand is a JavaScript runtime, which allows you to run JavaScript outside a web browser and on places like a server.
node is the basis for next, without node there will be no next.
NextJS simply provides an easy way to write server side ReactJS code, and have it rendered on the server and the browser.

## CSS Frameworks

### Styled-Components (Most readable)
https://github.com/styled-components/styled-components

### Tailwind (Fastest)
- https://headlessui.com/react/tabs
- https://www.tailwindtap.com/components

## Figma


# Backend Languages

## Node.Js
- https://frontendmasters.com/courses/node-js-v3/
- Node.js is an open-source and cross-platform runtime environment for executing JavaScript code outside a browser. 
- Used to create server-side web applications
- Asynchronous event-driven JavaScript runtime (environment that can run JS outside of browsers)
- Designed to build scalable network applications
	- ie: Handle connections concurrently
- Node.js is not a programming language. Rather, it’s a runtime environment that’s used to run JavaScript outside the browser.
- Neither is Node.js a framework (a platform for developing software applications).

### How it works
- "Single Threaded Event Loop Architecture"
[![Nodejs-Architecture](https://kinsta.com/wp-content/uploads/2021/03/Nodejs-Architecture-1024x576.png)](https://kinsta.com/wp-content/uploads/2021/03/Nodejs-Architecture.png)
Request -> Event Queue 
Single threaded event loop to process event queue requests
Event loop checks if the request requires a blocking (I/O) operation.
Yes -> event loop assigns worker from thread pool.
No -> 

Node.js uses fewer threads than multi-threaded languages#
When one needs to process data-intensive tasks, then using multi-threaded languages like Java makes much more sense. But for real-time applications, Node.js is the obvious choice.


### Useful Node.js Packages
- Express.js
	- Web framework for node.js
- Socket.io
	- Real-time, bidirectional, event-based communication
- Moment
	- Parse dates
- Forever
	- CLI tool for continuously running scripts
- Async
	- Utility module for asynchronous JS
- Mocha
	- JS test framework

# Rust
## Rocket (Web framework for Rust)
- https://rocket.rs/
- Type safe


# Backend Frameworks
- Express (works on top of nodejs)
- NextJS (works on top of nodejs)
- Django
- Ruby on Rails (MVC)
- Laravel (for PHP)
- Spring (for Java)


# Fonts
 - Inter typeface: https://rsms.me/inter/

# Notifications
- Firebase cloud messaging

# Devops

## Docker


# Networks
## Network layers
1. Application Layer
	1. Process-to-process communication across the internet
2. Transport Layer
	1. Connecting applications on the internet using sockets (gateways to a process)
3. Network Layer
	1. Any machine to machine
4. Data Link Layer
	1. Transmitting data from machine to machine that are 1 link away from each other
5. Physical Layer
	1. Hardware
## Switches
- Facilitate connection between devices/end-systems on a network
- Switches store pre-determined paths between end-systems and forwards packets through them
## Router
- Additional capacity of a switch allowing lookups for destination addresses 
	- Determines the shortest/least busy path
## TCP - Transmission Control Protocol
 - Transport layer protocol
## HTTP & HTTPS
- Application layer protocol, built on top of TCP
- Dictates how messages from a client/server are structured/exchanged
- HTTP ensures messages are being delivered intact and in time (ensures TCP is used)
- 'S' for secured
## Ports
- Endpoints where messages arrive on an end-system
- HTTP port = 80
- Ports above 1024 are open ports 
## Internet Protocol
- Network layer protocol
- Assigns addresses to devices to make them discoverable
## DNS - Domain Name System
- DNS resolution: loop up domain name on DNS server and obtain corresponding IP address

# Databases
## SQL
 - relational

## NoSQL
 - non-relational 
 - flexible schema
 - list of json objects

## Redis (NoSql)
- In-memory: operates in RAM memory
- Works alongside relational databases
- Used for caching, calculating/storing values permanently and/or temporarily
- Reduce querying to PostgresSQLH
![[Pasted image 20231108172329.png]]

# Web Caching
- Design feature of HTTP, can be done by browser.
- Data can be cached at several different points in the path between client and server
- Web caching caches certain requests with higher probability of being requested
- Subsequent requests for cached content can be fulfilled from a cache closer to the user instead of going all the way back to the web server
- Redis, Memcached
![[Pasted image 20231108172630.png]]

# Client Side
- Code on the 'client' side that handles how website looks, how it requests data from a server, how it interacts with temporary and local storage on client machine
# Server-side
1. Delivering and storing information efficiently
3. Controlling access to content
4. Storing session/state information
	1. Handling user input
5. Notifying and communicating
6. Analyzing data
- Common server-side languages: JS, python, PJP, ruby, c#


# Basic JS
## Document Object Model
- Object that represents the document as nodes that can be manipulated through JS