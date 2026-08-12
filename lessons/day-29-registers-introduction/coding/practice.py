"""
Day 29 - Registers Introduction (Python Practice)
Focus: Named Registers, System Clipboard, and Yank Ring

PRACTICE EXERCISES:
-------------------
Register syntax: "[register][operator][motion]
Examples:
  "ayiw   = Yank inner word into register 'a'
  "ap     = Paste contents of register 'a' after cursor
  "+y     = Yank into system clipboard
  "+p     = Paste from system clipboard
  "0p     = Paste last yanked text (bypassing deletes!)
"""

# Register Storage Targets
user_model_code = ""
auth_service_code = ""

# TODO 1: Yank the string "def get_user(user_id):" into register 'a'
#        - Go to line below -> press `"ay$`
def get_user(user_id):
    return {"id": user_id, "role": "admin"}

# TODO 2: Yank the dictionary below into register 'b'
#        - Cursor inside dict -> press `"byi{`
DEFAULT_SETTINGS = {
    "timeout": 30,
    "retries": 3,
    "logging": True
}

# TODO 3: Paste register 'a' below this comment
#        - Cursor on line below -> press `"ap`
# PASTE_REGISTER_A_HERE:

# TODO 4: Paste register 'b' below this comment
#        - Cursor on line below -> press `"bp`
# PASTE_REGISTER_B_HERE:

# TODO 5: Demonstrate Yank Register "0 vs Unnamed Register ""
#        - Yank the text "IMPORTANT_SECRET_KEY" with `yiw`
#        - Delete the word "delete_me" with `dw` (this overwrites default register "")
#        - Paste "IMPORTANT_SECRET_KEY" using `"0p` (register 0 retains yanked text!)
val1 = "IMPORTANT_SECRET_KEY"
val2 = "delete_me"
# Target paste area:
