[View code on GitHub](https://github.com/ergoplatform/ergo/.autodoc/docs/json/ci)

The `import_gpg.sh` script in the `.autodoc/docs/json/ci` folder is responsible for setting up GPG2 for reading passphrase from parameters and importing a GPG signing key. This is particularly useful in automating the signing process without requiring manual input of the passphrase, which can be beneficial in a continuous integration/continuous deployment (CI/CD) pipeline for signing and releasing new versions of a software package.

The script starts by creating a directory called `~/.gnupg` and setting its permissions to 700. It then configures the `gpg.conf` file with the following options:

- `use-agent`: Tells GPG to use the agent for passphrase handling.
- `pinentry-mode loopback`: Allows the agent to prompt for the passphrase on the command line.
- `allow-loopback-pinentry`: Enables the loopback pinentry mode.

After configuring GPG, the script sets the permissions of all files in the `~/.gnupg` directory to 600, ensuring that only the owner can read and write to them.

Next, the script decodes the GPG signing key, which should have been previously exported with the command `gpg --export-secret-keys [id] | base64 | pbcopy` and stored as a GitHub repository secret under the name `GPG_SIGNING_KEY`. The `printf` command reads the value of the `GPG_SIGNING_KEY` environment variable and pipes it to the `base64 --decode` command, which decodes the base64-encoded key and writes it to the `~/.gnupg/private.key` file.

Finally, the script imports the private key into GPG using the following command:

```bash
gpg --no-tty --batch --yes --import ~/.gnupg/private.key
```

The command options have the following effects:

- `--no-tty`: Tells GPG not to use the terminal for input or output.
- `--batch`: Runs GPG in non-interactive mode.
- `--yes`: Automatically answers "yes" to any prompts.

This script is likely used in conjunction with other parts of the project that require GPG signing, such as releasing a software package. By automating the GPG setup and key import process, the project can streamline its CI/CD pipeline and ensure that new software releases are signed and verified without manual intervention.
