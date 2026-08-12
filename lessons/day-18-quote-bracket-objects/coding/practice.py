"""
Day 18 - Quote & Bracket Text Objects (Python Practice)
Focus: Inner vs Around Quotes and Brackets (i", a", i', a', i(, a(, i[, a[, i{, a{)

PRACTICE INSTRUCTIONS:
----------------------
1. Open this file in Neovim: `nvim lessons/day-18-quote-bracket-objects/coding/practice.py`
2. Place cursor INSIDE quotes or brackets anywhere on the target line.
3. Perform the exact Neovim command specified in the TODO comment.

Command Key:
  ci"  = change inner double quotes (replaces string content)
  da"  = delete around double quotes (removes string + quotes)
  ci'  = change inner single quotes
  ci(  = change inner parentheses (replaces parameter list / expression)
  da(  = delete around parentheses (removes parameters AND parenthesized pair)
  ci{  = change inner dictionary / set / code block
  da{  = delete around dictionary / set / code block
  ci[  = change inner list / array items
  da[  = delete around list / array items
"""

import os
from typing import List, Dict


# TODO 1: Change the database URL string from "sqlite:///old_database.db" to "postgresql://localhost:5432/app_db"
#        - Place cursor ANYWHERE inside "sqlite:///old_database.db"
#        - Press `ci"` -> type `postgresql://localhost:5432/app_db` -> press <Esc>
DATABASE_URL = "postgresql://localhost:5432/app_db"


# TODO 2: Delete the outdated default string key 'DEPRECATED_KEY' along with its quotes
#        - Place cursor inside 'DEPRECATED_KEY'
#        - Press `da'` (notice how the single quotes AND surrounding space/token are deleted!)
API_KEYS = ['primary_v1', 'secondary_v2']


# TODO 3: Replace the parameter list inside `(self, host, port, timeout, debug)` with `(self, config_obj)`
#        - Place cursor ANYWHERE inside the function definition parentheses
#        - Press `ci(` -> type `self, config_obj` -> press <Esc>
def connect_service(self, config_obj):
    pass


# TODO 4: Delete the entire dictionary argument `{ "retry": 3, "backoff": 1.5 }` including braces
#        - Place cursor ANYWHERE inside `{ "retry": 3, "backoff": 1.5 }`
#        - Press `da{` (or `da}`)
client_options = configure_client()


# TODO 5: Replace all elements in the list `[100, 200, 300, 400]` with `[500, 600]`
#        - Place cursor ANYWHERE inside `[100, 200, 300, 400]`
#        - Press `ci[` -> type `500, 600` -> press <Esc>
status_codes = [500, 600]
