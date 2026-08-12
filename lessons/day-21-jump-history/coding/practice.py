"""
Day 21 - Jump History & Navigation Trail (Python Practice)
Focus: Time-traveling through your edit trail with Ctrl-o and Ctrl-i

PRACTICE EXERCISES:
-------------------
Jump List Commands:
  Ctrl-o  -> Jump back to PREVIOUS cursor location in jump list (Older location)
  Ctrl-i  -> Jump forward to NEXT cursor location in jump list (Newer location)
  :jumps  -> Display current jump history list

What creates a jump entry?
  - Search jumps (`/`, `?`, `*`, `#`)
  - Line jumps (`:45`, `G`, `gg`)
  - Mark jumps (`` `a ``)
"""

class PaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def process_payment(self, amount: float) -> bool:
        # TODO 1: Search for `verify_transaction` using `/verify_transaction` + Enter
        return self.verify_transaction(amount)

    def refund_payment(self, transaction_id: str) -> bool:
        # TODO 2: Jump to line 40 directly using `:40` + Enter
        return True

    def verify_transaction(self, amount: float) -> bool:
        if amount <= 0:
            return False
        return True

# TODO 3: After performing jumps above, press `Ctrl-o` multiple times to jump BACK 
#        through your exact cursor trail, then `Ctrl-i` to jump FORWARD!
