from config import get_config
from services import HHParser, WebScrappingService, HHFilter, save_to_json_file


def main():
    config = get_config()
    parser = HHParser(url=config.url, params=config.params, headers=config.headers)
    filter = HHFilter()

    data = WebScrappingService(parser=parser, filter=filter).execute()

    save_to_json_file(data)


if __name__ == "__main__":
    main()
