"""
Day 31 - Macro Recording (Python Practice)
Focus: Automating repetitive tasks with `q[register]` and `@`

PRACTICE EXERCISES:
-------------------
Macro Workflow:
  1. `qa`       -> Start recording macro into register 'a' (status bar shows 'recording @a')
  2. Perform edit steps carefully
  3. `j0` or `+` -> Move to the beginning of the next item/line
  4. `q`        -> Stop recording
  5. `@a`       -> Play macro once
  6. `5@a`      -> Repeat macro 5 times!
"""

# TODO 1: Convert raw API field strings into Python dataclass fields with type hints `str`
#        Raw format:   name
#        Target format: name: str = ""
#
# Macro steps to record on the line 'username':
#   - `qa`          (start recording in register 'a')
#   - `A: str = ""` (append at end of line)
#   - `<Esc>`       (exit insert mode)
#   - `j0`          (move to beginning of next line)
#   - `q`           (stop recording)
#
# Then replay with `4@a` to convert all remaining lines instantly!

class UserProfile:
    username
    email
    first_name
    last_name
    avatar_url


# TODO 2: Convert dictionary key-value list into Python keyword arguments in a dictionary function call
# Macro exercise: Convert `key = value` lines to `'key': value,`
# Try recording macro `qb`:
#   - `I'` then `<Esc>`
#   - `f=` then `ci=` to `': ` then `<Esc>`
#   - `A,` then `<Esc>`
#   - `j0` then `q`
# Run `3@b` to format all 4 items!

raw_data = dict(
    host = "localhost"
    port = 5432
    dbname = "production"
    user = "admin"
)
