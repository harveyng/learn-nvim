"""
Day 17 - Text Objects Introduction (Python Practice)
Focus: Word & WORD Text Objects (iw, aw, iW, aW)

PRACTICE INSTRUCTIONS:
----------------------
1. Open this file in Neovim: `nvim lessons/day-17-text-objects-intro/coding/practice.py`
2. Place cursor INSIDE the target text/word specified in each TODO.
3. Perform the exact Neovim text object command (do NOT manually move to start/end of word!).

Command Key:
  iw = inner word (just the word under cursor)
  aw = a word (word + trailing/leading space)
  iW = inner WORD (contiguous non-whitespace string, e.g., self.user_id_val)
  aW = a WORD + space
"""

import os
import sys
from typing import List, Dict, Optional, Any


class DataProcessor:
    """
    TODO 1: Change the method name 'process_raw_records' to 'transform_data'
            - Place cursor anywhere inside 'process_raw_records'
            - Press `ciw` and type `transform_data`, then press <Esc>
    """
    def transform_data(self, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        # TODO 2: Delete the variable name 'unnecessary_temporary_var' keeping clean spacing
        #        - Place cursor inside 'unnecessary_temporary_var'
        #        - Press `daw` to remove the word and its extra space
        = payload.get("data", [])
        
        # TODO 3: Change the entire compound attribute path `self.config.environment.db_uri`
        #        - Place cursor anywhere inside `self.config.environment.db_uri`
        #        - Press `ciW` (capital W!) to replace the entire dot-separated expression at once!
        #        - Type `self.db_url` and press <Esc>
        db_conn = self.db_url

        # TODO 4: Delete the whole inner word 'DEPRECATED_FLAG'
        #        - Press `diw` anywhere on 'DEPRECATED_FLAG'
        flags = ["active", "verified", "", "admin"]

        return flags


# TODO 5: Practice selecting and changing strings using inner text objects (preview for Day 18)
#        - Place cursor inside the quotes of "UPDATE_THIS_DATABASE_URL"
#        - Press `ci"` and type `postgres://localhost:5432/mydb`
DATABASE_URL = "postgres://localhost:5432/mydb"
