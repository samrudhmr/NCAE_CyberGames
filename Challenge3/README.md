# Challenge 3: Manual Deployment & Verification

Since Docker is unavailable, follow these steps to run and verify the challenge manually.

## Prerequisites
- Python 3.x installed
- `pip` installed

## 1. Setup Environment
Open your terminal (PowerShell or Command Prompt) and navigate to the `Challenge3` directory:
```powershell
cd C:\Users\samte\Downloads\NCAE_Cybergames\Challenge3
```

Install the required Python packages:
```powershell
pip install -r requirements.txt
```

## 2. Start the Application
Run the Flask server:
```powershell
python app.py
```
You should see output indicating the server is running on `http://127.0.0.1:5000`.

## 3. Verify the Vulnerability
1.  Open your web browser and go to `http://127.0.0.1:5000`. You will see the **Department of Redundancy Homepage**.
2.  Click the **"Proceed to Login Access"** button to go to the login page.
3.  Try to type a long password in the input field. Notice it stops after 10 characters.
4.  Right-click the input field and select **Inspect**.
5.  In the Developer Tools, find the `<input>` tag and locate `maxlength="10"`.
6.  Double-click `maxlength="10"` and delete it (or change it to `5000`).

## 4. Exploit and Get the Flag
1.  You need a password of exactly 500 characters.
2.  Generate the payload using Python in a separate terminal:
    ```powershell
    python -c "print('A'*500, end='')" | clip
    ```
    *(Note: This copies 500 'A's to your clipboard)*
3.  Go back to the browser, paste the content into the password field.
4.  Click **Authenticate**.
5.  **Bonus Round**: You will be asked to confirm several times. Just keep clicking "OK".
6.  The page will crash to a **Fake Error Screen**.
7.  Look closely at the "Stack Trace" on the error screen to find the flag: `flag{html_cant_stop_me}`.
