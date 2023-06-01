[View code on GitHub](https://github.com/ergoplatform/ergo/src/main/scala/org/ergoplatform/GlobalConstants.scala)

The `GlobalConstants` object is a singleton that holds constants used throughout the Ergo Platform project. Specifically, it defines a constant `ApiDispatcher` which is the name of the dispatcher for actors processing API requests. This is done to avoid any potential conflicts between the actors processing blockchain data and those processing API requests.

This object can be used in other parts of the Ergo Platform project to ensure consistency and avoid hardcoding values. For example, if an actor needs to process API requests, it can use the `ApiDispatcher` constant to ensure it is using the correct dispatcher.

Here is an example of how the `ApiDispatcher` constant could be used in an actor:

```scala
import akka.actor.Actor
import akka.actor.ActorLogging
import akka.dispatch.Dispatchers

class ApiActor extends Actor with ActorLogging {
  // Use the ApiDispatcher for this actor
  implicit val ec = context.system.dispatchers.lookup(GlobalConstants.ApiDispatcher)

  def receive = {
    case request: ApiRequest =>
      // Process the API request
  }
}
```

In this example, the `ApiActor` uses the `ApiDispatcher` constant to set the execution context for the actor. This ensures that the actor is using the correct dispatcher for processing API requests.

Overall, the `GlobalConstants` object is a simple but important part of the Ergo Platform project that helps ensure consistency and avoid potential conflicts.
## Questions: 
 1. What is the purpose of the `GlobalConstants` object?
   - The `GlobalConstants` object holds constants needed around the whole Ergo Platform.

2. What is the `ApiDispatcher` constant used for?
   - The `ApiDispatcher` constant is used as the name of the dispatcher for actors processing API requests, to avoid clashing between blockchain processing and API actors.

3. Is the `GlobalConstants` object a singleton?
   - Yes, the `GlobalConstants` object is a singleton, as indicated by the use of the `object` keyword instead of `class`.