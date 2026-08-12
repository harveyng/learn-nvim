"""
Day 43 - Buffer Management (Python Practice)
Focus: Managing multiple open files, buffers, and splits in Neovim

PRACTICE EXERCISES:
-------------------
Essential Commands:
  :ls or :buffers  -> List all open buffers (ID, name, indicators like %a or #h)
  :b <name_or_id>  -> Switch to buffer matching name or ID (e.g. :b main or :b 2)
  :bnext or :bn    -> Switch to next buffer
  :bprev or :bp    -> Switch to previous buffer
  :bd              -> Delete (close) current buffer without quitting Neovim
  :sp <file>       -> Horizontal split screen
  :vsp <file>      -> Vertical split screen
  Ctrl-w h/j/k/l   -> Move focus between split windows
  Ctrl-w =         -> Equalize split window sizes
"""

# Practice Buffer Navigation Flow:
# --------------------------------
# 1. Open multiple files in Neovim at once:
#    `nvim lessons/day-43-buffer-management/coding/practice.py lessons/day-31-macro-recording/coding/practice.py`
#
# 2. Check open buffers:
#    Type `:ls` and hit <Enter>
#
# 3. Jump between buffers using partial name autocomplete:
#    Type `:b macro` and press <Tab> then <Enter>
#
# 4. Open vertical split:
#    Type `:vsp lessons/day-17-text-objects-intro/coding/practice.py`
#
# 5. Move between left and right window split:
#    Press `Ctrl-w h` (move left) or `Ctrl-w l` (move right)

def buffer_management_demo():
    print("Welcome to Neovim Buffer & Window Management!")
    print("Mastering buffers turns Neovim into a high-speed multi-file IDE.")

if __name__ == "__main__":
    buffer_management_demo()
