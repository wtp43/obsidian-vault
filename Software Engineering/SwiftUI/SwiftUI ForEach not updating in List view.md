---
dg-publish: true
---

Fix: 
`List { ... }.id(UUID())`

https://www.reddit.com/r/SwiftUI/comments/gb28lc/swiftui_foreach_not_updating_even_though/


Other possible solutions
- VIEWMODEL.objectWillChange.send()
- objectWillChange.send()


Common Mistakes

## Copy By Value
for item in items {
	- A copy of an array element is assigned to test variable
	- Use the actual index to modify array elements
```swift
for index in 0..<testings.count {
    testings[index].value = 15
}
```