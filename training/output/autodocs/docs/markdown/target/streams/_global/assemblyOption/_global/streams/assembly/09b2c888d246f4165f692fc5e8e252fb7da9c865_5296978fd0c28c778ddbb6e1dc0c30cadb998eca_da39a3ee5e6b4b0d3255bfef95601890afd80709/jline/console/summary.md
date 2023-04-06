[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/target/streams/_global/assemblyOption/_global/streams/assembly/09b2c888d246f4165f692fc5e8e252fb7da9c865_5296978fd0c28c778ddbb6e1dc0c30cadb998eca_da39a3ee5e6b4b0d3255bfef95601890afd80709/jline/console)

The `CandidateListCompletionHandler.properties` file in the `jline/console/completer` folder is a part of the Ergo project and contains a set of constants related to displaying information to the user, specifically in the context of displaying possible completions for user input. These constants are likely used throughout the larger project to standardize the way information is displayed to the user and ensure consistency in the wording of prompts.

The file contains the following constants:

- `DISPLAY_CANDIDATES`: A string that asks the user if they want to display all possibilities. It includes a placeholder for the number of possibilities, which is likely filled in dynamically based on the context of the program.
- `DISPLAY_CANDIDATES_YES`: A string that represents the user's response to the `DISPLAY_CANDIDATES` prompt, indicating they want to see all possibilities.
- `DISPLAY_CANDIDATES_NO`: A string that represents the user's response to the `DISPLAY_CANDIDATES` prompt, indicating they do not want to see all possibilities.
- `DISPLAY_MORE`: A string that is likely used to prompt the user to display more information. It may be used in conjunction with the `DISPLAY_CANDIDATES` prompt to allow the user to see more information about the possibilities before making a decision.

These constants are likely used in the larger project to handle user input and display possible completions for that input. For example, if the user is typing a command and the program can suggest multiple completions, it may use the `DISPLAY_CANDIDATES` constant to ask the user if they want to see all possible completions. Based on the user's response, the program can then display the appropriate completions using the `DISPLAY_CANDIDATES_YES` and `DISPLAY_CANDIDATES_NO` constants.

Example usage:

```python
if user_input == DISPLAY_CANDIDATES_YES:
    display_all_possibilities()
else:
    display_top_possibilities()
```

In summary, the `CandidateListCompletionHandler.properties` file contains constants related to displaying possible completions for user input. These constants are used throughout the larger project to standardize the way information is displayed to the user and ensure consistency in the wording of prompts.
