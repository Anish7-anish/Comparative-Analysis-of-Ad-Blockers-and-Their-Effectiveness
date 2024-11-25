all_websites = [
    "https://www.google.com", "https://www.youtube.com", "https://www.amazon.com", "https://www.facebook.com", "https://www.wikipedia.org",
    "https://www.twitter.com", "https://www.instagram.com", "https://www.linkedin.com", "https://www.yahoo.com", "https://www.netflix.com",
    "https://www.reddit.com", "https://www.apple.com", "https://www.microsoft.com", "https://www.ebay.com", "https://www.bing.com",
    "https://www.office.com", "https://www.nytimes.com", "https://www.cnn.com", "https://www.hulu.com", "https://www.spotify.com",
    "https://www.paypal.com", "https://www.dropbox.com", "https://www.salesforce.com", "https://www.adobe.com", "https://www.etsy.com",
    "https://www.bestbuy.com", "https://www.target.com", "https://www.walmart.com", "https://www.homedepot.com", "https://www.lowes.com",
    "https://www.nike.com", "https://www.zara.com", "https://www.ikea.com", "https://www.costco.com", "https://www.chewy.com",
    "https://www.foxnews.com", "https://www.bbc.com", "https://www.aliexpress.com", "https://www.airbnb.com", "https://www.booking.com",
    "https://www.trivago.com", "https://www.expedia.com", "https://www.tripadvisor.com", "https://www.delta.com", "https://www.aa.com",
    "https://www.marriott.com", "https://www.hyatt.com", "https://www.ihg.com", "https://www.snapchat.com", "https://www.tiktok.com",
    "https://www.pinterest.com", "https://www.quora.com", "https://www.yelp.com", "https://www.mlb.com", "https://www.nfl.com",
    "https://www.nba.com", "https://www.espn.com", "https://www.nasdaq.com", "https://www.nyse.com", "https://www.coinbase.com",
    "https://www.binance.com", "https://www.kraken.com", "https://www.patreon.com", "https://www.gofundme.com", "https://www.kickstarter.com",
    "https://www.udemy.com", "https://www.coursera.org", "https://www.edx.org", "https://www.khanacademy.org", "https://www.skillshare.com",
    "https://www.ted.com", "https://www.codecademy.com", "https://www.github.com", "https://www.gitlab.com", "https://www.bitbucket.org",
    "https://www.digitalocean.com", "https://www.linode.com", "https://www.heroku.com", "https://www.cloudflare.com", "https://www.openai.com",
    "https://www.ibm.com", "https://www.oracle.com", "https://www.vmware.com", "https://www.cisco.com", "https://www.intel.com",
    "https://www.dell.com", "https://www.hp.com", "https://www.samsung.com", "https://www.sony.com", "https://www.lg.com",
    "https://www.tesla.com", "https://www.ford.com", "https://www.chevrolet.com", "https://www.honda.com", "https://www.toyota.com",
    "https://www.bmw.com", "https://www.mercedes-benz.com", "https://www.audi.com", "https://www.volkswagen.com", "https://www.hyundai.com"
]

# Split into 4 separate files
for i in range(4):
    with open(f'websites_machine_{i+1}.txt', 'w') as file:
        file.writelines(f"{website}\n" for website in all_websites[i*25:(i+1)*25])