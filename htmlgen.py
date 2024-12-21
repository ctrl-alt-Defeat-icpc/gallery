import os
from PIL import Image

IMG_FOLDER = 'img'
THUMBNAILS_FOLDER = 'thumbnails'
HTML_INDEX = 'index.html'

def getHtmlContent(image_html):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Logo Gallery</title>
  <style>
    /* General reset */
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Arial', sans-serif;
      background: linear-gradient(135deg, #6a11cb, #2575fc);
      color: #fff;
      text-align: center;
      padding: 20px;
    }}

    .container {{
      max-width: 1200px;
      margin: 0 auto;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}

    h1 {{
      font-size: 2.5rem;
      margin-bottom: 20px;
      color: #f3f3f3;
    }}

    p {{
      font-size: 1.2rem;
      margin-bottom: 20px;
      line-height: 1.6;
    }}

    .gallery {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }}

    .gallery img,
    .gallery video {{
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 12px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}

    .gallery img:hover,
    .gallery video:hover {{
      transform: scale(1.05);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }}

    footer {{
      margin-top: 20px;
      font-size: 0.9rem;
      color: rgba(255, 255, 255, 0.8);
    }}

    a {{
      color: #ffd700;
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to ctrl+alt+DEFEAT gallery page</h1>
    <p>Here are some amazing photos, GIFs, and short videos (maybe) in our contest. Click on any media to view it in its original size.</p>
    <div class="gallery">
    {image_html}
    </div>
    <footer>
      <p>Made with [love] by <a href="https://ctrl-alt-defeat-icpc.github.io/" target="_blank">ctrl+alt+DEFEAT team</a></p>
    </footer>
  </div>
</body>
</html>
"""

    return html_content

""" ---- comment ----
<!-- Image Section -->
<a href="./img/01.webp" target="_blank"><img src="./img/01.webp" alt="logo"></a>
<a href="./img/02.png" target="_blank"><img src="./img/02.png" alt="logo"></a>
<a href="./img/03.jpeg" target="_blank"><img src="./img/03.jpeg" alt="logo"></a>
<a href="./img/04.jpeg" target="_blank"><img src="./img/04.jpeg" alt="logo"></a>

<!-- GIF Section -->
<a href="./gifs/sample1.gif" target="_blank"><img src="./gifs/sample1.gif" alt="gif"></a>
<a href="./gifs/sample2.gif" target="_blank"><img src="./gifs/sample2.gif" alt="gif"></a>

<!-- Video Section -->
<video src="./videos/sample1.mp4" autoplay loop muted></video>
<video src="./videos/sample2.webm" autoplay loop muted></video>
"""

def makeThumbnails(img_folder=IMG_FOLDER, thumb_folder=THUMBNAILS_FOLDER):
    os.makedirs(thumb_folder, exist_ok=True)
    for img_file in sorted(os.listdir(img_folder)):
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            original_path = os.path.join(os.getcwd(), img_folder, img_file).replace("\\", "/")
            thumbnail_path = os.path.join(os.getcwd(), thumb_folder, img_file).replace("\\", "/")
            # Generate thumbnail if it doesn't exist
            if not os.path.exists(thumbnail_path):
                with Image.open(original_path) as img:
                    img.thumbnail((300, 200))  # Set thumbnail size
                    img.save(thumbnail_path, "WEBP")  # Save as lightweight format (e.g., WebP)
    
def createImgInHtml(img_folder=IMG_FOLDER, thumb_folder=THUMBNAILS_FOLDER, html_name=HTML_INDEX):
    image_tags = []
    for img_name in sorted(os.listdir(thumb_folder)):
        # <img src="./img/01.webp" alt="logo">
        img_tag = f'<img src="./{thumb_folder}/{img_name}" alt="photo">'
        if os.path.exists(os.path.join(os.getcwd(), img_folder, img_name)):
            # <a href="./img/01.webp" target="_blank"><img src="./img/01.webp" alt="logo"></a> 
            image_tags.append(f'<a href="./{img_folder}/{img_name}" target="_blank">{img_tag}</a>')
        else:
            image_tags.append(img_tag)
    
    image_html = '\n'.join(image_tags)
    with open(os.path.join(os.getcwd(), html_name), 'w') as f:
        f.write(getHtmlContent(image_html))

if __name__ == "__main__":
    makeThumbnails()
    createImgInHtml()
