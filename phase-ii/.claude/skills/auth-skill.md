---
name: auth-skill
description: Implement secure authentication systems including signup, signin, password hashing, JWT tokens, and Better Auth integration.
---

# Auth Skill – Secure Authentication System

## Instructions

1. **User Registration (Signup)**
   - Accept email and password
   - Validate input
   - Hash passwords before storing
   - Prevent duplicate accounts

2. **User Login (Signin)**
   - Verify credentials
   - Compare hashed passwords
   - Return auth response
   - Handle invalid credentials

3. **Password Security**
   - Use bcrypt or argon2
   - Never store plaintext passwords
   - Enforce minimum password length

4. **JWT Tokens**
   - Generate JWT on login
   - Include user ID in token
   - Set expiration
   - Sign using shared secret

5. **Better Auth Integration**
   - Enable JWT plugin
   - Share secret with backend
   - Attach JWT to every API request

6. **Authorization**
   - Verify JWT on backend
   - Extract user identity
   - Enforce user-level access
