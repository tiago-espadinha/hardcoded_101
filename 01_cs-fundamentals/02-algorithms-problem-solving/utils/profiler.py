import cProfile
import pstats
import io
from typing import Callable, Any

def profile_function(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Wraps cProfile for any function call and prints summary."""
    pr = cProfile.Profile()
    pr.enable()
    result = func(*args, **kwargs)
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(10)  # Top 10 stats
    print(s.getvalue())
    return result
