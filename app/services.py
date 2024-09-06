from dataclasses import dataclass
from datetime import datetime
import json
import httpx


@dataclass
class HHParser:
    url: str
    params: dict
    headers: dict

    def parse(self) -> httpx.Response:
        r = httpx.get(url=self.url, params=self.params, headers=self.headers)
        return r


@dataclass
class HHFilter:
    salary: str = "USD"

    def filter(self, items: list[dict]) -> list[dict]:
        filtered = []
        for item in items["items"]:
            filtered.append(
                {
                    "url": item["alternate_url"],
                    "salary": {
                        "from": item["salary"]["from"],
                        "to": item["salary"]["to"],
                        "currency": item["salary"]["currency"],
                    },
                    "company": item["employer"]["name"],
                    "city": item["address"]["city"] if item.get('address') else None,
                }
            )

        return [item for item in filtered if item["salary"]["currency"] == "USD"]


@dataclass
class WebScrappingService:
    parser: HHParser
    filter: HHFilter

    def execute(self) -> list[dict]:
        data = self.parser.parse()
        print(data.url)
        result = self.filter.filter(data.json())
        return result


def save_to_json_file(data: list[dict]):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"vacancies_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Данные сохранены в файл: {filename}")
