# Challenge 1: Cookie Monster's Admin Panel - Walkthrough

**Category:** Web / Broken Authentication  
**Difficulty:** Easy  
**Flag:** `NCAE{this_is_the_flag}`

---

## Challenge Overview

You are a new intern at **SuperSecureCorp** and you have been given access to the company news feed. However, your account is stuck in "Guest Mode," so you can only see the lunch menu. The CEO, *C. Monster*, says only administrators can see the "Real News."

The website is stateless and relies on a cookie named `role` to determine your privileges.

---

## Solution

The vulnerability allows users to escalate their privileges by simply modifying the value of the `role` cookie stored in their browser.

### Method 1: Developer Tools (Recommended)

1.  **Open Developer Tools**: Press `F12` or right-click the page and select **Inspect**.
2.  **Navigate to Storage**: Go to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
3.  **Find Cookies**: Expand the **Cookies** section in the left sidebar and click on the domain (e.g., `http://localhost`).
4.  **Locate the Cookie**: Find the cookie named `role`. Its value will currently be set to `guest`.
5.  **Modify the Cookie**: Double-click the value `guest` and change it to `admin`.
6.  **Refresh the Page**: Reload the webpage (`F5` or `Ctrl+R`).
7.  **Get the Flag**: The server will now read your cookie as `role=admin` and display the "Real News" section containing the flag.

### Method 2: Command Line (cURL)

You can also solve this challenge using `curl` by sending the expected cookie header manually.

```bash
curl -b "role=admin" http://localhost
```

The response will contain the HTML for the admin view, which includes the flag.

---

## Why this works

The application relies entirely on the client (the user's browser) to tell it what role the user has via the `role` cookie. It does not verify this claim against a session on the server. Since users have full control over their own cookies, they can change the value to anything they want.

A secure implementation would use a **CRYPTOGRAPHICALLY SIGNED** session cookie (like Flask's built-in sessions) that cannot be modified without knowing the secret key, or store the session state on the server side tied to a random session ID.
