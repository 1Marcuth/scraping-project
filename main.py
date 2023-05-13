from modules import input_, scraper, image_maker
from utils.logger import get_logger

def main():
    content = {}

    logger = get_logger()

    input_.ask_island_type(content, logger)
    scraper.scrape_island(content, logger)
    image_maker.make_island_images(content, logger)

    #print(content)

if __name__ == "__main__":
    main()