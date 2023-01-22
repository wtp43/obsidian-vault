https://stackoverflow.com/questions/67977092/swiftui-initialzier-requires-string-conform-to-identifiable


The argument of `List` is required to be unique, that's the purpose of the `Identifiable` protocol

You can do

```swift
List(teams, id: \.self) { team in
```

but then **you** are responsible to ensure that the strings are unique. If not you will get unexpected behavior.

Better is to use a custom struct with an unique `id` conforming to `Identifiable`



ForEach returns a list of views vs for x in which is just a loop.