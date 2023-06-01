[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/streams/_global/assemblyOption/_global/streams/assembly/d1611456b2abd81a733bfc1664ba7823fb3afeb4_dir/swagger-ui)

The code in this folder is responsible for providing a user-friendly interface for developers to explore and test the API endpoints of the ergo project using Swagger UI. Swagger UI is a popular tool for generating interactive documentation for RESTful APIs.

The `index.html` file serves as the front-end for the Swagger UI documentation tool. It includes links to CSS and image files for styling the interface and a div element with an ID of "swagger-ui" where the interface will be rendered. The JavaScript code in the script section initializes the Swagger UI interface by creating a new instance of the SwaggerUIBundle object and passing in configuration options such as the API documentation URL, the DOM element ID, and various plugins and presets.

Example usage of `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Include CSS and image files for styling -->
</head>
<body>
    <div id="swagger-ui"></div>
    <script>
        // Initialize Swagger UI
        const ui = SwaggerUIBundle({
            url: "https://api.example.com/docs",
            dom_id: "#swagger-ui",
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIStandalonePreset
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout"
        });

        // Make the Swagger UI instance available globally
        window.ui = ui;
    </script>
</body>
</html>
```

The `oauth2-redirect.html` file contains a script for handling the OAuth2 authentication flow for the Swagger UI. The script retrieves the OAuth2 object from the parent window, checks the URL hash for a code, token, or error, and proceeds with the authentication flow if the state parameter matches the sent state. The script calls the callback function with the authentication object, token, and a flag indicating whether the state is valid, and then closes the window.

Example usage of `oauth2-redirect.html`:

```html
<!doctype html>
<html lang="en-US">
<body onload="run()">
</body>
</html>
<script>
    // OAuth2 object from parent window
    var oauth2 = window.opener.swaggerUIRedirectOauth2;

    function run () {
        // Authentication flow
        // ...

        // Callback function
        function callback(data) {
            console.log(data);
        }

        // Error callback function
        function errCb(data) {
            console.error(data);
        }

        // Set OAuth2 callback and error callback functions
        oauth2.callback = callback;
        oauth2.errCb = errCb;

        // Close window
        window.close();
    }
</script>
```

These files are essential for the ergo project as they provide an interactive and user-friendly way for developers to understand the API structure and test its functionality without writing any code. The code can be used as-is or modified to fit the specific needs of the project.
