"""
Day 25 - Visual Block Operations (Python Practice)
Focus: Vertical Column Editing with Ctrl-v (I, A, c, d)

PRACTICE EXERCISES:
-------------------
Visual Block Mode:
  Ctrl-v    -> Start Visual Block mode
  j / k     -> Move vertically across lines
  I         -> Insert text BEFORE selected column across ALL lines (press <Esc> to apply!)
  A         -> Append text AFTER selected column / end of line (press <Esc> to apply!)
  c         -> Change selected block across all lines
  d         -> Delete selected vertical block
"""

# TODO 1: Add comment symbol `# ` to the beginning of all 5 lines below using Visual Block
##        Steps:
##          - Move cursor to start of line 1 (`# TODO 1...` below)
##          - Press `Ctrl-v`
##          - Press `4j` (highlight column 1 down 5 lines)
##          - Press `I` (capital I)
#          - Type `# `
#          - Press `<Esc>` (watch Neovim insert `# ` on all 5 lines automatically!)

import json
import logging
import sys
import time
import os

# TODO 2: Comment out these environment variables by adding `EXPORT_` prefix using Visual Block
#        Steps:
#          - Cursor at start of `DB_HOST`
#          - `Ctrl-v 3j` -> `I` -> type `EXPORT_` -> `<Esc>`

EXPORT_DB_HOST = "localhost"
EXPORT_DB_PORT = "5432"
EXPORT_DB_USER = "admin"
EXPORT_DB_PASS = "secret"

# TODO 3: Append trailing comma `,` to all dictionary keys at once using Visual Block
#        Steps:
#          - Cursor on first string `'name'`
#          - `Ctrl-v 3j $` -> `A` -> type `,` -> `<Esc>`
user_dict = {
    'name': "Alice",
    'role': "Developer",
    'team': "Backend",
    'status': "Active",
}
