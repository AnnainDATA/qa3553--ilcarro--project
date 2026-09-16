| Part              | Meaning                                                       | Example                           |
| ----------------- | ------------------------------------------------------------- | --------------------------------- |
| `(?=.*\d)`        | must contain **at least one digit**                           | `5`                               |
| `(?=.*[a-z])`     | must contain **at least one lowercase letter**                | `a`, `m`, `z`                     |
| `(?=.*[A-Z])`     | must contain **at least one uppercase letter**                | `A`, `M`, `Z`                     |
| `(?=.*[@$#^&*!])` | must contain **at least one special character** from the list | `@`, `$`, `#`, `^`, `&`, `*`, `!` |
| `(?=.*[a-zA-Z])`  | must contain **a letter** — lowercase or uppercase            | `a` or `A`                        |
| `.{8,}`           | the password must contain **at least 8 characters**           | `Abc123!x`                        |

🔐 In short, the password must contain:
🔢 at least 1 digit
🔡 at least 1 lowercase letter
🔠 at least 1 uppercase letter
🔣 at least 1 special character: @ $ # ^ & * !
📏 at least 8 characters

Valid example: Test123! ✅

Invalid example: test123! ❌ — no uppercase letter.