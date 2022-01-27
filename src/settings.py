import json
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    installers_output_directory: str

    def __post_init__(self) -> None:
        path = Path(self.installers_output_directory)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        self.installers_output_directory = str(path.absolute())


def get_settings() -> Settings:
    settings = json.load(open('config.json'))
    return Settings(**settings)
