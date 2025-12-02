import time
from typing import Dict, Optional

# ANSI color codes
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class Clock:
    def __init__(self):
        self._timers: Dict[str, float] = {}
    
    def start(self, timer_id: str) -> None:
        """Start a timer with the given ID"""
        self._timers[timer_id] = time.time()
        
    
    def stop(self, timer_id: str, label: Optional[str] = None) -> float:
        """Stop a timer and print the elapsed time. Returns elapsed time in ms."""
        if timer_id not in self._timers:
            raise ValueError(f"Timer '{timer_id}' was never started")
        
        start_time = self._timers[timer_id]
        elapsed = (time.time() - start_time) * 1000
        
        display_label = label if label else timer_id
        print(f"{CYAN}{display_label}{RESET}: {YELLOW}{elapsed:.2f}ms{RESET}")
        
        del self._timers[timer_id]
        return elapsed
    
    def reset(self) -> None:
        """Reset all timers"""
        self._timers.clear()

# Global clock instance
clock = Clock()
