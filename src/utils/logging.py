import logging
import traceback

from functools import wraps
from src.actions.take_screenshot_action import page_screenshot

logger = logging.getLogger(__name__)


def log_errors(context: str, message: str = ""):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger.info(message)

            try:
                return func(self, *args, **kwargs)
            
            except Exception as e:
                var = traceback.format_exc()

                logger.exception(f"{type(e).__name__} {message} error {context}: {e}")
                page_screenshot(page=self.page)
                logger.exception(var)

                raise e
        return wrapper
    return decorator
