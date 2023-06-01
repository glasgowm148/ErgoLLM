[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/scala/org/ergoplatform/http)

The `.autodoc/docs/json/src/main/scala/org/ergoplatform/http` folder contains three Scala files that define the HTTP service, node panel route, and Swagger route for the Ergo platform.

`ErgoHttpService.scala` defines the main HTTP service for the Ergo platform. It combines several routes together and handles rejections, exceptions, and CORS requests. The class takes in three parameters: `apiRoutes`, `swaggerRoute`, and `panelRoute`. To use this class, create an instance of `ErgoHttpService` with the required routes and bind it to an HTTP server:

```scala
val apiRoutes = Seq[ApiRoute](... // define API routes here)
val swaggerRoute = SwaggerRoute(...)
val panelRoute = NodePanelRoute(...)
val ergoHttpService = ErgoHttpService(apiRoutes, swaggerRoute, panelRoute)
val bindingFuture = Http().bindAndHandle(ergoHttpService.compositeRoute, "localhost", 8080)
```

`NodePanelRoute.scala` defines a route for the Ergo node's web panel. It serves the `index.html` file from the `panel` directory in the classpath and all the static files (CSS, JavaScript, images) from the same directory. To use this class, create an instance of `NodePanelRoute`, combine its route with other routes, and bind them to an HTTP server:

```scala
val nodePanelRoute = NodePanelRoute()
val routes = nodePanelRoute.route ~ otherRoutes
Http().bindAndHandle(routes, "localhost", 8080)
```

`SwaggerRoute.scala` provides a route for serving Swagger UI and Swagger configuration files. It takes two parameters: `RESTApiSettings` and `swaggerConfig`. The class defines three routes: one for serving the Swagger configuration file, one for serving the Swagger UI `index.html` file, and one for serving all other Swagger UI files. To use this class, create an instance of `SwaggerRoute` with the required parameters, combine its route with other routes, and bind them to an HTTP server:

```scala
val swaggerConfig = """{...}""" // Swagger configuration string
val restApiSettings = RESTApiSettings()
val swaggerRoute = SwaggerRoute(restApiSettings, swaggerConfig)
val routes = swaggerRoute.route ~ otherRoutes
Http().bindAndHandle(routes, "localhost", 8080)
```

In summary, this folder contains the necessary code to define the main HTTP service, node panel route, and Swagger route for the Ergo platform. These classes can be used to start the HTTP server and serve the API, Swagger UI, and node panel to clients.
