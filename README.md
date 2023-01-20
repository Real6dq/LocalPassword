# LocalPassword

This project is a simple cloudless password generator that includes a GUI :)

## Featuers
- Impossible to find the master password.
- Cloudless, doesn't get saved anywhere.
- Secure, uses SHA256 & shuffles the password well.
- Open source, anyone could modify it, it's MIT license.

## Requirements
- Python 3 (Installed by default)
- Tkinter (Installed by default)
- ctypes (Installed by default & Windows only)

## Pre-built executable
- Go to releases, install the first one.


## Run from the source
1. Install the required packages if they are not installed by default.
2. Run the script by using `python main.py`
3. Enter the length, name, password, birthdate, and website in the corresponding fields
4. Click the "Generate" button
5. The generated password will be displayed in the label below the input fields and also copied to the clipboard.

## Note
- The logic of the provided code might not be the most secure way to generate a password, it is just an example.
- This code works only on Windows systems and you should use different libraries for other platforms.
- This is not tested in Windows 11, only Windows 10.
