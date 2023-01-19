
# Structure

The array should be part of an observable class

The array should consist of nonobservable structs


You can use a struct instead of a class. Because of a struct's value semantics, a change to a person's name is seen as a change to Person struct itself, and this change is also a change to the people array so @Published will send the notification and the View body will be recomputed.

In general, creating a custom view for the items in a List/ForEach allows each item in the collection to be monitored for changes.