import argparse
import requests
import json
import csv
import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from utils import logger

USER_AGENT = "AutomateIt-Scraper/1.0 (+https://github.com/automate-it)"

def check_robots_txt(url):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    rp = RobotFileParser()
    try:
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch(USER_AGENT, url)
    except Exception:
        # If robots.txt fails to load, be conservative
        return True

def scrape_page(url, selector, attr=None):
    if not check_robots_txt(url):
        logger.warn(f"Disallowed by robots.txt: {url}")
        return []

    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.select(selector)
        
        results = []
        for el in elements:
            if attr:
                val = el.get(attr)
            else:
                val = el.get_text(strip=True)
            if val:
                results.append(val)
        return results
    except Exception as e:
        logger.error(f"Error scraping {url}: {e}")
        return []

def save_results(results, output_file):
    if not results:
        return

    ext = Path(output_file).suffix.lower()
    if ext == '.json':
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)
    elif ext == '.csv':
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Content"])
            for r in results:
                writer.writerow([r])
    else:
        logger.error("Unsupported output format. Use .json or .csv")

def main():
    parser = argparse.ArgumentParser(description="Configurable web scraper.")
    parser.add_argument("--url", required=True, help="URL to scrape")
    parser.add_argument("--selector", required=True, help="CSS selector")
    parser.add_argument("--attr", help="Attribute to extract (default: text)")
    parser.add_argument("--output", help="Output file (CSV/JSON)")
    parser.add_argument("--limit", type=int, help="Max results")
    parser.add_argument("--delay", type=float, default=1.0, help="Crawl delay")
    parser.add_argument("--follow", action="store_true", help="Follow links in results")

    args = parser.parse_args()
    
    logger.info(f"Starting scrape: {args.url}")
    
    all_results = set()
    results = scrape_page(args.url, args.selector, args.attr)
    
    if args.follow and not args.attr:
        # Attempt to follow links if they look like URLs
        to_follow = [r for r in results if r.startswith('http') or r.startswith('/')]
        for link in to_follow:
            if args.limit and len(all_results) >= args.limit:
                break
            
            full_link = urljoin(args.url, link)
            logger.info(f"Following: {full_link}")
            time.sleep(args.delay)
            
            sub_results = scrape_page(full_link, args.selector, args.attr)
            all_results.update(sub_results)
    else:
        all_results.update(results)

    final_results = list(all_results)
    if args.limit:
        final_results = final_results[:args.limit]

    logger.info(f"Scrape completed. Found {len(final_results)} items.")
    
    if args.output:
        from pathlib import Path
        save_results(final_results, args.output)
        logger.info(f"Results saved to {args.output}")
    else:
        for r in final_results:
            print(r)

if __name__ == "__main__":
    main()
