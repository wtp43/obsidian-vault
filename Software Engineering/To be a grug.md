---
dg-publish: true
tags: 
created: ""
---
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# To be a grug

## The Eternal Enemy: Complexity
- complexity very very bad
- readability over complexity

## Saying No
- say no to complexity
- "no, grug not build that feature"
- "no, grug not build that abstraction"
- note: this is good engineering advice but bad career advice: "yes" is magic word for more shiny rock and put in charge of large tribe of developer
- sad but true: learn "yes" then learn blame other grugs when fail, ideal career advice
- but grug must to grug be true and "no" is magic grug word. Hard to say at first especially if you nice grug and don't like disappoint people (many such grugs!) but easier over time even though shiny rock pile not as high as might otherwise be
- is ok: how many shiny rock grug really need anyway?

## Saying ok
- sometimes compromise necessary or no shiny rock
- in this situation, grug recommend "ok"
- "ok, grug build that feature"
- then grug spend time think of 80/20 solution to problem and build that instead
- "80 want with 20 code" solution maybe not have all bell-whistle that project manager want, maybe a little ugly but work and deliver most value
- sometimes best just not tell project manager and do it 80/20
- easier forgive than permission. project managers mind like butterfly at times overworked, often forget what even feature supposed to do or move on or quit or get fired grug see many such cases 

## Factoring your code
- next strategy very harder: break code base up properly
- here is hard give general advice because each system so different
- however, one thing grug come to believe: not factor your application too early!
- early on in project, everything very abstract and like water
- grug try not to factor in early part of project and then at some point, good cut-points emerge from code base

## Testing
- grug prefer write most tests after prototype phase when code has begun firm up
- grug must here be very disciplined
- grug experience that ideal tests are not unit test or either end-to-end-test, but in-between test
- unit tests fine but break as implementation change (much compared to api) and make refactor hard and frankly, many bugs anyway often due to interactions other code
- grug writ unit test mostly at start of project, help get things going but not get too attached or expect value long time
- end to end tests good, show whole system work, but hard to understand when rbeak and drive grug crazy very often
- **in-between tests**, "integration tests" high level enough test correctness of system, low level enough, with good debugger, easy to se what break
- small, well curated end-to-end test suite is created to be kept working religiously on pain of clubbing
- focus of important end-to-end test on most common UI features and few most important edge cases, but not too many or become impossible maintain then ignored
- also, grug dislike mocking in test, prefer only when absolute necessary to (rare/never) and coarse grain mocking (cut points/systems) only at that
- one exception "first test" dislike by grug: when bug found. grug always try first reproduce bug with regression test then fix bug, this case only for some reason work better

> [!info]+ Regression Test
> Regression testing is a type of software testing conducted after a code update to ensure that the update introduced no new bugs. This is because new code may bring in new logic that conflicts with the existing code, leading to defects.

## Chesterton's Fence
- wise grug shaman chesterton once say:
	- here exists in such a case a certain institution or law; let us say, for the sake of simplicity, a fence or gate erected across a road. The more modern type of reformer goes gaily up to it and says, “I don’t see the use of this; let us clear it away.” To which the more intelligent type of reformer will do well to answer: “If you don’t see the use of it, I certainly won’t let you clear it away. Go away and think. Then, when you can come back and tell me that you do see the use of it, I may allow you to destroy it.”
- many older grug learn this lesson well not start tearing code out willy nilly, no matter how ugly look
- humility not often come big brained or think big brained easily or grug even, but grug often find "oh, grug no like look of this, grug fix" lead many hours pain grug and no better or system worse even
- grug not say no improve system ever, quite foolish, but recommend take time understand system first especially bigger system is and is respect code working today even if not perfect
- here tests often good hint for why fence not to be smashed

## Microservices
- grug wonder why big brain take hardest problem, factoring system correctly, and introduce network call too
- seem very confusing to grug
- Premature and excessive fragmenting into unmaintainable and operationally microservices is the bane of operability convenience

## Tools
- grug love tool
- tool allow grug brain to create code that not possible otherwise by doing thinking for grug
- grug always spend time in new place learning tools around him to maximize productivity
- learn tools for two weeks make development often twice faster and often have dig around ask other developers help, no docs
- code completion in IDE allow grug not have remembered all API
- good debugger worth weight in shiny rocks
- grug always recommend new programmer learn available debugger very deeply, features like conditional break points, expression evaluation, stack navigation, etc teach new grug more about computer than university class often
- grug say never be not improve tooling

## Type Systems
- grug very like type systems make programming easier

## Expression Complexity

grug once like to minimize lines of code much as possible. write code like this:

```js
  if(contact && !contact.isActive() && (contact.inGroup(FAMILY) || contact.inGroup(FRIENDS))) {
    // ...
  }
```

over time grug learn this hard debug, learn prefer write like so:

```js
  if(contact) {
    var contactIsInactive = !contact.isActive();
    var contactIsFamilyOrFriends = contact.inGroup(FAMILY) || contact.inGroup(FRIENDS);
    if(contactIsInactive && contactIsFamilyOrFriends) {
        // ...
    }
  }
```
club fight start with other developers attack and grug yell: "easier debug! see result of each expression more clearly and good name! easier understand conditional expression! EASIER DEBUG!"

## DRY

[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) mean Don't Repeat Self, powerful maxim over mind of most developers

grug respect DRY and good advice, however grug recommend balance in all things, as gruggest big brain aristotle recommend

grug note humourous graph by Lea Verou correspond with grug passion not repeat:

![code concerns over time](https://grugbrain.dev/over-time.png)

over time past ten years program grug not as concerned repeat code. so long as repeat code simple enough and obvious enough, and grug begin feel repeat/copy paste code with small variation is better than many callback/closures passed arguments or elaborate object model: too hard complex for too little benefit at times

hard balance here, repeat code always still make grug stare and say "mmm" often, but experience show repeat code sometimes often better than complex DRY solution

note well! grug encourage over literal developer not take does work line too serious, is joke
# [Separation of Concerns (SoC)](https://grugbrain.dev/#grug-on-soc)

**Similar things should go together**

[Separation of Concern (SoC)](https://en.wikipedia.org/wiki/Separation_of_concerns) another powerful idea over many developer mind, idea to separate different aspects of system into distinct sections code

canonical example from web development: separation of style (css file), markup (html file) and logic (javascript file)

here grug much more sour faced than DRY and in fact write big brained essay on alternative design principle [locality of behavior (LoB)](https://htmx.org/essays/locality-of-behaviour/) against SoC

grug much prefer put code on the thing that do the thing. now when grug look at the thing grug know the thing what the thing do, always good relief!

when separate of concern grug must often all over tarnation many file look understand what how button do, much confuse and time waste: bad!

# [Logging](https://grugbrain.dev/#grug-on-logging)

grug huge fan of logging and encourage lots of it, especially in cloud deployed. some non-grugs say logging expensive and not important. grug used think this way no more

funny story: grug learn idol [rob pike](https://en.wikipedia.org/wiki/Rob_Pike) working on logging at google and decide: "if rob pike working on logging, what grug do there?!?" so not pursue. turn out logging _very_ important to google so of course best programmer work on it, grug!

don't be such grug brain, grug, much less shiney rock now!

oh well, grug end up at good company anyway and rob pike dress habit [increasingly erratic](https://www.youtube.com/watch?v=KINIAgRpkDA), so all work out in end, but point stand: logging very important!

grug tips on logging are:

- log all major logical branches within code (if/for)
- if "request" span multiple machine in cloud infrastructure, include request ID in all so logs can be grouped
- if possible make log level dynamically controlled, so grug can turn on/off when need debug issue (many!)
- if possible make log level per user, so can debug specific user issue

last two points are especially handy club when fighting bugs in production systems very often

unfortunately log libraries often very complex (java, [why you do?](https://stackify.com/logging-java/)) but worth investing time in getting logging infrastructure "just right" pay off big later in grug experience

logging need taught more in schools, grug think

# [Optimizing](https://grugbrain.dev/#grug-on-optimizing)

ultra biggest of brain developer once say:

> premature optimization is the root of all evil

this everyone mostly know and grug in humble violent agreement with ultra biggest of big brain

grug recommend always to have concrete, real world perf profile showing specific perf issue before begin optimizing.

never know what actual issue might be, grug often surprise! very often!

beware only cpu focus: easy to see cpu and much big o notation thinking having been done in school, but often not root of all slowness, surprise to many including grug

hitting network equivalent of many, many millions cpu cycle and always to be minimized if possible, note well big brain microservice developer!

inexperienced big brain developer see nested loop and often say "O(n^2)? Not on my watch!"

complexity demon spirit smile


# [The Visitor Pattern](https://grugbrain.dev/#grug-on-visitor-pattern)

[bad](https://en.wikipedia.org/wiki/Visitor_pattern)

# [Front End Development](https://grugbrain.dev/#grug-on-front-end-development)

some non-grugs, when faced with web development say:

"I know, I'll split my front end and back end codebase up and use a hot new SPA library talking to a GraphQL JSON API back end over HTTP (which is funny because I'm not transferring hypertext)"

now you have two complexity demon spirit lairs

and, what is worse, front end complexity demon spirit even more powerful and have deep spiritual hold on entire front end industry as far as grug can tell

back end developers try keep things simple and can work ok, but front end developers make very complex very quickly and introduce lots of code, demon complex spirit

even when website just need put form into database or simple brochure site!

everyone do this now!

grug not sure why except maybe facebook and google say so, but that not seem very good reason to grug

grug not like big complex front end libraries everyone use

grug make [htmx](https://htmx.org) and [hyperscript](https://hyperscript.org) to avoid

keep complexity low, simple HTML, avoid lots javascript, the natural ether of spirit complexity demon

maybe they work for you, but no job post, sorry

react better for job and also some type application, but also you become alcolyte of complexity demon whether you like or no, sorry such is front end life

# [Fads](https://grugbrain.dev/#grug-on-fads)

grug note lots of fads in development, especially front end development today

back end better more boring because all bad ideas have tried at this point maybe (still retry some!)

still trying all bad ideas in front end development so still much change and hard to know

grug recommend taking all revolutionary new approach with grain salt: big brains have working for long time on computers now, most ideas have tried at least once

grug not saying can't learn new tricks or no good new ideas, but also much of time wasted on recycled bad ideas, lots of spirit complexity demon power come from putting new idea willy nilly into code base

# [Fear Of Looking Dumb](https://grugbrain.dev/#grug-on-fold)

note! very good if senior grug willing to say publicly: "hmmm, this too complex for grug"!

many developers Fear Of Looking Dumb (FOLD), grug also at one time FOLD, but grug learn get over: very important senior grug say "this too complicated and confuse to me"

this make it ok for junior grugs to admit too complex and not understand as well, often such case! FOLD major source of complexity demon power over developer, especially young grugs!

take FOLD power away, very good of senior grug!

note: important to make thinking face and look big brained when saying though. be prepare for big brain or, worse and much more common, _thinks_ is big brain to make snide remark of grug

be strong! no FOLD!

club sometimes useful here, but more often sense of humor and especially last failed project by big brain very useful, so collect and be calm

# [Impostor Syndrome](https://grugbrain.dev/#grug-on-imposter-syndrom)

grug note many such impostor feels in development

always grug one of two states: grug is ruler of all survey, wield code club like thor OR grug have no idea what doing

grug is mostly latter state most times, hide it pretty well though

now, grug make softwares of much work and [moderate open source success](https://star-history.com/#bigskysoftware/htmx&bigskysoftware/_hyperscript&Date) , and yet grug himself often feel not any idea what doing! very often! grug still fear make mistake break everyone code and disappoint other grugs, imposter!

is maybe nature of programming for most grug to feel impostor and be ok with is best: nobody imposter if everybody imposter

any young grug read this far probably do fine in program career even if frustrations and worry is always to be there, sorry
# Source
https://grugbrain.dev/
