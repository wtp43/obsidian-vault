---
dg-publish: true
---
# UI
https://apps.apple.com/us/app/zenti-meditation-timer/id1587887322
- list row view 
- timer view
- Timer completes, show celebration animation
- launch screen gradient
- app icon
- Collapsible list of tags on todo page
- Categories show progressbar
- UI Inspiration (https://github.com/roman-luzgin/TodoAppSwiftUI3)
	- https://betterprogramming.pub/build-a-to-do-app-in-swiftui-using-the-new-ios-15-features-afe5650a24a9

# Features
- Heap 
	- https://www.kodeco.com/586-swift-algorithm-club-heap-and-priority-queue-data-structure
	- Update priority on move (newPriority = previousitem.priority)
	- Must be a stable sort
- Sorted by priority
- Implement due date
- Idle timer (start idle timer when on todo list page)
	- automatically start work timer when idle timer completes
- Show by tags (collapsible list_)
	- include, exclude
- Automate priority (due date)
- Score feature
- Show Stats
	- By time period (7, 14, 30) 
- Total points counter


```
RadialGradient(
	gradient: Gradient(colors: [Color.accentColor, Color("SecondaryAccentColor")]),
	center: .center,
	startRadius: 5,
	endRadius: 500)
	.ignoresSafeArea()
```