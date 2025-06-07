from bs4 import BeautifulSoup
import requests
import os

save_images = 'Images/'
if not os.path.exists(save_images):
    os.makedirs(save_images)

def download_images(query):
    query = "vbbsss"
    url = f"https://www.google.com/search?q={query}&client=tablet-android-samsung-ss&sca_esv=9c007220e9a9c47a&udm=2&biw=655&bih=730&sxsrf=AE3TifOk3hoz8s8jooirryqRwqGii8f4gw%3A1749148221409&ei=PeJBaIbpGJiVseMPndviiAM&oq={query}&gs_lp=EgNpbWciBnZiYnNzcyoCCAAyBxAjGCcYyQJI9A5QAFgAcAF4AJABAJgBAKABAKoBALgBAcgBAJgCAaACA5gDAIgGAZIHATGgBwCyBwC4BwDCBwMwLjHIBwI&sclient=img"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    image_tags = soup.find_all('img')
    image_tags = image_tags[1:]


    downloaded_images = []
    i = 0

    for image in image_tags:
        image_url = image.get('src')
        if image_url:
            if image_url.startswith('/'):
                image_url = "https://www.google.com" + image_url
            try:
                image_data = requests.get(image_url).content
                filename = f"image_{i+1}.jpg"
                filepath = os.path.join(save_images, filename)
                with open(filepath, "wb") as file:
                    file.write(image_data)
                print(f"Downloaded: {filename}")
                downloaded_images.append(filename)
                i += 1
            except Exception as e:
                print(f"Error downloading image {i+1}: {e}")
    return downloaded_images
