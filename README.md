# Password Strength & Security Awareness

## Project Overview
Password Strength & Security Awareness is a beginner-friendly cybersecurity mini project that checks basic characteristics of a test password and helps users learn safer password practices.

The application classifies a password as **Weak**, **Medium**, or **Strong** based on five simple checks. It is an educational tool and is not a replacement for professional password-auditing tools.

## Live Application
https://password-security-awareness-nfhxowt9rrceuyfjrvw22d.streamlit.app/

## Technologies Used
- **Python** — password-checking logic
- **Streamlit** — web application interface
- **GitHub** — source-code repository
- **Streamlit Community Cloud** — online deployment

## Features
- Password input field
- Password strength score out of 5
- Weak, Medium, or Strong classification
- Individual requirement checks
- Password security tips
- Project information section

## Password Strength Checking
The app checks these five requirements. Each satisfied requirement earns one point.

| Requirement | Description | Score |
|---|---|---:|
| Length | At least 8 characters | 1 |
| Uppercase | At least one uppercase letter (A–Z) | 1 |
| Lowercase | At least one lowercase letter (a–z) | 1 |
| Number | At least one digit (0–9) | 1 |
| Special character | At least one non-alphanumeric character | 1 |
| **Maximum score** | | **5/5** |

### Result Categories
- **Weak:** 0–2 points
- **Medium:** 3–4 points
- **Strong:** 5 points

## Security Tips
- Use a long password or passphrase.
- Avoid using your name, birthday, or other personal information.
- Do not reuse the same password across important accounts.
- Never share passwords with other people.
- Enable two-factor authentication (2FA) where available.
- Consider using a reputable password manager.

## Run Locally
1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the dependency:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```

## Project Details
- **Student:** Dhanush Devendra
- **Course:** TY BSc Information Technology
- **College:** SIWS College
- **Project:** Password Strength & Security Awareness

## Privacy and Responsible Use
Use only test passwords. Do not enter real, banking, work, or other sensitive passwords. In a Streamlit application, entered values are sent to the app server for processing; do not treat this educational demo as a secure password-storage or password-auditing service.

## Future Scope
Possible future improvements include better detection of common passwords, a password generator, more detailed guidance, and carefully designed breach-checking functionality.

## Disclaimer
This project is intended for educational cybersecurity awareness only. Its simple scoring rules do not guarantee that a password is secure.
