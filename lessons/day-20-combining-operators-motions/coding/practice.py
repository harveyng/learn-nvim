"""
Day 20 - Combining Operators & Motions (Python Practice)
Focus: Composability ( [operator] + [motion / text object] )

PRACTICE EXERCISES:
-------------------
Operators:
  d = delete
  c = change
  y = yank (copy)
  gU = uppercase
  gu = lowercase
  = = auto-indent

Motions / Text Objects:
  i" / a" = inner / around double quotes
  i( / a( = inner / around parentheses
  i[ / a[ = inner / around brackets
  i{ / a{ = inner / around curly braces
  ip      = inner paragraph
"""

# TODO 1: Change the contents inside quotes from "INVALID_HOST" to "127.0.0.1"
#        - Cursor inside "INVALID_HOST" -> press `ci"` -> type `127.0.0.1` -> press <Esc>
HOST = "127.0.0.1"
PORT = 8080

# TODO 2: Delete everything inside the function arguments `(self, req, res, logger, tracer)`
#        - Cursor inside parentheses -> press `ci(` -> type `self, request` -> press <Esc>
def handle_request(self, request):
    pass

# TODO 3: Uppercase the dictionary key 'content_type'
#        - Cursor on 'c' in 'content_type' -> press `gUiw`
HEADERS = {
    'CONTENT_TYPE': 'application/json',
    'authorization': 'Bearer token123'
}

# TODO 4: Delete the whole dictionary argument including surrounding brackets `{ ... }`
#        - Cursor inside `{ ... }` -> press `da{` or `da}`
config_override = dict()

# TODO 5: Auto-indent the poorly indented function below
#        - Cursor inside function -> press `v` then `ap` (select paragraph) -> press `=`
def ugly_indented_function():
    x = 10
    y = 20
    z = x + y
return z
