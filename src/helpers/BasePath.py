import sys
from pathlib import Path

class BasePath:
    def get_base_path(self) -> str:
        if getattr(sys, 'frozen', False):
            application_path = Path(sys._MEIPASS)
        elif __file__:
            application_path = Path(__file__).parent.parent.parent

        return str(application_path)