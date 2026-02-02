# Challenge 3: The Passive-Aggressive Login - Walkthrough

## Challenge Description
The goal is to submit a password that is exactly 500 characters long to the "Department of Redundancy". However, the input field stops accepting characters after 10.

## Vulnerability Analysis
The restriction is implemented entirely on the client-side using the HTML `maxlength` attribute. This is a common mistake where developers rely on frontend validation for security or business logic constraints without enforcing them properly or understanding that the client can be manipulated.

## Solution
1. **Navigate to the Challenge**: Open the web application at `http://localhost:5000`. You will see the Department of Redundancy Homepage.
2. **Access Login**: Click on "Proceed to Login Access" to reach the form.
3. **Inspect the Input Field**: Right-click on the password input box and select "Inspect" (or "Inspect Element").
4. **Locate the Restriction**: In the Elements tab of the Developer Tools, find the `<input>` tag. You will see `maxlength="10"`.
   ```html
   <input type="password" id="password" name="password" maxlength="10" placeholder="Enter exactly 500 characters" required>
   ```
4. **Bypass the Restriction**: Double-click on `maxlength="10"` and delete it, or change the value to something larger (e.g., `1000`).
5. **Generate the Payload**: You need a string of exactly 500 characters. You can generate this using Python:
   ```python
   print("A" * 500)
   ```
6. **Submit**: Copy the generated string, paste it into the now-unrestricted password field, and click "Authenticate".
7. **Navigate the Trap**: The success page will present several "Confirm" dialogs. Click "OK" through all of them.
8. **Find the Flag**: The page will seemingly crash with a fake "Server Panic" error. Read the stack trace on the screen to find the flag:
   `flag{html_cant_stop_me}`
