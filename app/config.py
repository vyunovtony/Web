from dataclasses import dataclass, field


@dataclass
class Config:
    url: str = field(default="https://api.hh.ru/vacancies")
    params: dict = field(
        default_factory=lambda: {
            "text": "python Django Flask",
            "area": ["1", "2"],
            "only_with_salary": True,
        }
    )
    headers: dict = field(
        default_factory=lambda: {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    )


def get_config() -> Config:
    return Config()
