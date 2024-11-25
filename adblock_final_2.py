import os
import platform
import sys
import time
import csv
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from multiprocessing import Pool

# Set paths to ad-blocker extensions depending on the platform
if platform.system() == "Darwin":  # macOS
    paths = [
        "/Users/anish/Documents/Privacy/Privacy Project/CFHDOJBKJHNKLBPKDAIBDCCDDILIFDDB_4_8_0_0_adblock_plus.crx",
        "/Users/anish/Documents/Privacy/Privacy Project/CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_60_0_0_ublock.crx",
        "/Users/anish/Documents/Privacy/Privacy Project/GIGHMMPIOBKLFEPJOCNAMGKKBIGLIDOM_6_9_3_0_adblock.crx",
        "/Users/anish/Documents/Privacy/Privacy Project/MLOMIEJDFKOLICHCFLEJCLCBMPEANIIJ_10_4_10_0_ghostery.crx"
    ]
elif platform.system() == "Windows":  # Windows
    paths = [
        r"C:\adblock_extensions\CFHDOJBKJHNKLBPKDAIBDCCDDILIFDDB_4_8_0_0_adblock_plus.crx",
        r"C:\adblock_extensions\CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_60_0_0_ublock.crx",
        r"C:\adblock_extensions\GIGHMMPIOBKLFEPJOCNAMGKKBIGLIDOM_6_9_3_0_adblock.crx",
        r"C:\adblock_extensions\MLOMIEJDFKOLICHCFLEJCLCBMPEANIIJ_10_4_10_0_ghostery.crx"
    ]

# Function to measure page load time
def get_page_load_time(driver, url):
    start_time = time.time()
    driver.get(url)
    end_time = time.time()
    return end_time - start_time

# Function to capture and count blocked ads/trackers based on DOM elements
ad_keywords = [
    'ad', 'ads', 'adservice', 'admanager', 'adserver', 'doubleclick', 'googlesyndication', 'googletagmanager',
    'google-analytics', 'googleadservices', 'facebook.net', 'connect.facebook.net', 'fbcdn', 'analytics',
    'track', 'tracking', 'pixel', 'cdn-cgi', 'adroll', 'quantserve', 'scorecardresearch', 'criteo', 'taboola',
    'outbrain', 'moatads', 'advertising', 'promo', 'affiliates', 'banners', 'click', 'impression', 'openx',
    'pubmatic', 'rubiconproject', 'yieldmanager', 'adsafeprotected', 'adsrvr', 'adition', 'gumgum', 'adtech',
    'eyeota', 'mathtag', 'bkrtx', 'bidswitch', 'casalemedia', 'contextweb', 'lijit', 'mookie1', 'rfihub',
    'simpli.fi', 'sitescout', 'spotxchange', 'tapad', 'teads', 'thetradedesk', 'turn', 'viglink', 'zedo',
    'bounceexchange', 'exelator', 'sharethrough', 'tidaltv', 'advert', 'sponsor', 'adsystem', 'adserver',
    'adsrv', 'adsco', 'adbanner', 'adserving', 'ads-img', 'adimg', 'adscript', 'banner', 'popunder', 'popads',
    'clickserve', 'mediaplex', 'advertisement', 'serving-sys', 'googlesyndication', 'googleleadservices',
    'omtrdc.net', '2o7.net', 'omtrdc', 'omtrk', 'statse.webtrendslive.com', 'optimizely', 'mixpanel', 'krxd.net',
    'mxpnl.com', 'newrelic', 'nr-data.net', 'doubleverify', 'ads-twitter.com', 'analytics.twitter.com', 'adblade',
    'adsonar', 'adzerk', 'liverail', 'quantserve', 'quantcount', 'googletagservices', 'semasio.net', 'agkn.com',
    'everesttech.net', 'marinsm.com', 'yahoo.com', 'yimg', 'brightcove', 'demdex', 'tags.tiqcdn', 'tiqcdn',
    'truste', 'trustarc', 'privacymgmt', 'cdn.permutive', 'permutive', 'trkn.us', 'bouncex', 'ml314.com',
    'zopim', 'hotjar', 'segment', 'heapanalytics', 'kissmetrics', 'cdn.segment', 'cdn.heapanalytics', 'cdn.kissmetrics',
    'snap.licdn', 'wcfbc.net', 'adsymptotic.com', 'contextweb.com', 'weborama', 'adform', 'revcontent', 'revjet',
    'ads-twitter', 'cloudfront', 'cdn', 'tags', 'beacon', 'marketing', 'advertisement', 'adserver', 'adnetwork',
    'googletag', 'adadvisor', 'advertising.com', 'yieldlab', 'adition', 'tradedoubler', 'serving-sys', 'rlcdn',
    'adsrvr.org', '3lift', 'amgdgt', 'appnexus', 'bidder', 'bnmla', 'bouncex', 'bttrack', 'buzzfeed', 'chartbeat',
    'colossusssp', 'consensu', 'cookie-script', 'creativecdn', 'ctasnet', 'ctrln', 'deepintent', 'dntx', 'doublepimp',
    'emxdgt', 'everestjs', 'getclicky', 'glanceguide', 'glpals', 'infolinks', 'inmobi', 'inspixel', 'instinctiveads',
    'kargo', 'kik', 'listtrac', 'lockerdome', 'logrocket', 'mediago', 'mediaiq', 'mopub', 'navegg', 'nuggad', 'ob',
    'onetrust', 'parrable', 'pubgears', 'purch', 'reachlocal', 'revsci', 'rfihub', 'rlcdn', 'rockyou', 'ru4', 'sbscorecard',
    'scorecard', 'securitag', 'simpli', 'sovrn', 'spotx', 'springserve', 'sslapis', 'tapestry', 'tapjoy', 'tend', 'trion',
    'turnto', 'viglink', 'visualdna', 'weewatch', 'webtrekk', 'xplosion', 'zeotap', 'zemanta', 'zergnet', 'ad.insert',
    'adview', 'adservice', 'adx', 'adclick', 'sponsored', 'adsbygoogle', 'partner', 'affiliate', 'exponential',
    'nend', 'adnxs', 'prosperent', 'acxiom', 'advertorial', 'advertisements', 'medianet', 'valueclick',
    'carbonads', 'adscale', 'adition', 'medialets', 'flashtalking', 'connatix', 'gumgum', 'bidtellect', 'adtheorent',
    'mopub', 'tapad', 'drawbridge', 'bidtellect', 'inmobi', 'celtra', 'advertisingcloud', 'clickagy', 'distillery',
    'truoptik', 'capterra', 'dianomi', 'admixer', 'zenaps', 'adengage', 'plista', 'justpremium', 'indexexchange',
    'magnite', 'sharethrough', 'stackadapt', 'triplelift', 'verizonmedia', 'yandex', 'trustpilot', 'trustbadge'
]

def get_blocked_ads_trackers(driver, ad_keywords):
    ad_count = 0
    tracker_count = 0
    retry_attempts = 3

    for _ in range(retry_attempts):
        try:
            potential_elements = driver.find_elements(By.XPATH, "//*[contains(@id, 'ad') or contains(@class, 'ad') or contains(@src, 'ad') or contains(@id, 'track') or contains(@class, 'track') or contains(@src, 'track')]")
            for element in potential_elements:
                outer_html = element.get_attribute('outerHTML')
                for keyword in ad_keywords:
                    if keyword in outer_html:
                        if 'track' in keyword or 'analytics' in keyword:
                            tracker_count += 1
                        else:
                            ad_count += 1
                        break
            break
        except StaleElementReferenceException:
            print("Encountered a stale element, retrying...")
            time.sleep(1)
    return ad_count, tracker_count

# Function to monitor CPU and memory usage
def get_system_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return cpu_usage, memory_usage

# Function to save results to CSV for each ad-blocker or no-extension case
def save_to_csv(data, extension_name):
    file_name = f'adblocker_effectiveness_{extension_name}.csv'
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Adjust headers based on whether it's an extension or no extension
        if extension_name == "no_extension":
            writer.writerow([
                "Website", "Page Load Time (s)", "Ads Found", "Trackers Found",
                "CPU Before (%)", "CPU After (%)", "Memory Before (%)", "Memory After (%)"
            ])
        else:
            writer.writerow([
                "Website", "Page Load Time (s)", "Ads Blocked", "Trackers Blocked",
                "CPU Before (%)", "CPU After (%)", "Memory Before (%)", "Memory After (%)"
            ])
        
        writer.writerows(data)

# Load list of websites to test from a given path
websites_file_path = "/Users/anish/Documents/Privacy/Privacy Project/websites_machine_4.txt"  # Replace this path as needed to specify which file to use
websites = []
try:
    with open(websites_file_path, 'r') as file:
        websites = [line.strip() for line in file]
except FileNotFoundError:
    print(f"Error: The file {websites_file_path} was not found. Please provide a valid path.")
    sys.exit(1)

def process_website(args):
    path, website, extension_name = args
    chrome_options = Options()
    if path:  # If path is None, run without extension
        chrome_options.add_extension(path)

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(180)
    driver.implicitly_wait(10)
    try:
        before_cpu, before_memory = get_system_usage()
        load_time = get_page_load_time(driver, website)
        ad_count, tracker_count = get_blocked_ads_trackers(driver, ad_keywords)
        after_cpu, after_memory = get_system_usage()

        if extension_name == "no_extension":
            print(f"Page load time for {website} with no ad-blocker: {load_time:.2f} seconds")
            print(f"Ads found: {ad_count}, Trackers found: {tracker_count}")
        else:
            print(f"Page load time for {website} with ad-blocker {extension_name}: {load_time:.2f} seconds")
            print(f"Ads blocked: {ad_count}, Trackers blocked: {tracker_count}")

        print(f"CPU Usage Before: {before_cpu}%, After: {after_cpu}%")
        print(f"Memory Usage Before: {before_memory}%, After: {after_memory}%")

        result = [
            website, load_time, ad_count, tracker_count,
            before_cpu, after_cpu, before_memory, after_memory
        ]
    except Exception as e:
        print(f"Error during testing {website} with {extension_name}: {e}")
        result = None
    finally:
        driver.quit()
    return (extension_name, result)

# Run the tests in parallel
if __name__ == "__main__":
    # Testing without any ad-blocker extension
    with Pool(processes=4) as pool:  # Run with 4 parallel processes
        args = [(None, website, "no_extension") for website in websites]
        results = pool.map(process_website, args)

    # Save results for no ad-blocker case
    no_extension_results = [result for extension_name, result in results if result is not None]
    save_to_csv(no_extension_results, "no_extension")

    # Testing with each ad-blocker extension
    for path in paths:
        extension_name = path.split('/')[-1].split('.')[0] if platform.system() == "Darwin" else path.split('\\')[-1].split('.')[0]
        with Pool(processes=4) as pool:  # Run with 4 parallel processes
            args = [(path, website, extension_name) for website in websites]
            results = pool.map(process_website, args)

        # Group results by extension name and save to CSV
        extension_results = [result for extension_name, result in results if result is not None]
        save_to_csv(extension_results, extension_name)
