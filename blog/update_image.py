import re
import os

def update_img_tags_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to match <img src={require('./img/filename.jpg').default} alt="..." />
    pattern = re.compile(
        r'<img\s+src=\{require\(\'\.\/img\/(.*?)\'\)\.default\}\s+alt="(.*?)"(?:[^>]*)\/?>',
        re.IGNORECASE
    )

    def replacer(match):
        filename = match.group(1)
        alt_text = match.group(2)
        url = f"https://raw.githubusercontent.com/nifetency/nife-blog-content/main/blog/img/{filename}"
        return f"![{alt_text}]({url})"

    updated_content = pattern.sub(replacer, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"✔ Updated: {file_path}")

# Loop through all .mdx files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.mdx'):
        update_img_tags_in_file(filename)
