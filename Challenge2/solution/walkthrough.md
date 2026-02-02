# Challenge 2: The VIP Velvet Rope - Walkthrough

**Category:** Web / Client-Side Security  
**Difficulty:** Easy  
**Flag:** `NCAE{client_side_security_is_no_security}`

---

## Challenge Overview

You are presented with a "Club NCAE" website featuring a "VIP Lounge Entrance." There is a button to enter, but it is grayed out and unclickable.

A comment in the HTML source code mocks the user:
> "Heh, these n00bs will never get in. I put a disabled attribute on the button! Unbreakable security!"

The goal is to bypass this restriction and access the VIP area.

---

## Solution

The "security" for this challenge is entirely client-side, relying on a simple HTML attribute to prevent the user from clicking the submit button. There are no actual server-side checks preventing access to the VIP route.

### Method 1: Developer Tools (Recommended)

1.  **Inspect the Button**: Right-click the "ENTER VIP LOUNGE" button and select **Inspect** (or press `F12` to open Developer Tools).
2.  **Find the Attribute**: Locate the `<button>` element in the Elements tab. You will see the `disabled` attribute:
    ```html
    <button type="submit" class="vip-btn" disabled>ENTER VIP LOUNGE</button>
    ```
3.  **Remove the Attribute**: Double-click on the word `disabled` and delete it, or right-click the element and select "Edit as HTML" to remove the attribute.
4.  **Click the Button**: The button will immediately become active (clickable). Click it to submit the form.
5.  **Get the Flag**: You will be successfully redirected to the VIP page, where the flag is displayed.

### Method 2: Direct URL Access

Since the form submits a POST request to `/vip`, but the server route also accepts GET requests (visible in `app.py` if source is available, or guessable), you can simply type the URL directly into your browser:

1.  Navigate to `http://localhost:5000/vip` (or whatever host/port the challenge is running on).
2.  The server will render the VIP page with the flag.

---

## Why this works

Client-side controls (like HTML `disabled` attributes, Javascript validation, or hiding elements) are for user experience, **not security**. An attacker has full control over the client (browser) and can modify any HTML, CSS, or Javascript code running on their machine.

A secure implementation would require the server to verify the user's authorization (e.g., checking a session cookie or token) before rendering the sensitive content on the `/vip` route.
