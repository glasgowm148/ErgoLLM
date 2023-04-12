[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/src/main/resources/swagger-ui)

The `.autodoc/docs/json/src/main/resources/swagger-ui` folder contains essential files for the ergo project's API documentation, specifically for rendering the Swagger UI interface and handling OAuth2 authentication.

`index.html` is the front-end file for the Swagger UI documentation tool. It renders the interactive API documentation in the user's web browser. The file includes links to CSS and image files for styling the interface, and a `div` element with the ID `swagger-ui` where the interface is rendered. The `script` tags at the bottom load the Swagger UI JavaScript files and initialize the interface with various options, such as the location of the API documentation file, the HTML element ID, deep linking, presets, plugins, and layout. This interface allows developers to explore the project's API, learn about endpoints, parameters, and responses, test the API, and generate client code in various programming languages.

`oauth2-redirect.html` is responsible for handling OAuth2 authentication in the Swagger UI. The script in this file retrieves OAuth2 parameters from the URL and handles the authentication flow. It is used by the Swagger UI to authenticate the user and obtain an access token for accessing the API. The code checks if the state parameter matches the one sent by the server to prevent CSRF attacks. If the authentication flow is "accessCode" or "authorizationCode," it checks for the code parameter in the URL, sets the code in the OAuth2 object, and calls the callback function with the authentication and redirect URL parameters. If the code parameter is not present, it calls the error callback function with an error message. If the authentication flow is not "accessCode" or "authorizationCode," it calls the callback function with the token and validation parameters.

Example usage of `oauth2-redirect.html`:

```html
<!doctype html>
<html lang="en-US">
<body onload="run()">
</body>
</html>
<script>
    // ... (script content from the summary above)
</script>
```

In summary, the code in this folder plays a crucial role in the ergo project's API documentation by providing a user-friendly interface for developers to interact with the API and handling OAuth2 authentication for secure access.
