import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

nav_links = """        <div>
            <a href="about.html" style="color: var(--navy); text-decoration: none; margin-right: 30px; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">About Us</a>
            <a href="https://narrowgate.dev" target="_blank" style="color: var(--navy); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">Blog</a>
        </div>"""

css_mobile_nav = """        @media (max-width: 900px) {
            nav { padding: 20px; flex-direction: column; gap: 20px; align-items: center; }
            nav > div:first-child { flex-direction: column; text-align: center; gap: 10px; }
            nav > div:first-child > div { margin-left: 0 !important; font-size: 0.6rem !important; }"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update logo link to "/"
    content = content.replace('href="index.html"', 'href="/"')

    # 2. Add links to other pages
    if file != 'index.html':
        # Replace the right-side nav item with the standard links
        # Match from <div style="font-size: 0.7rem... > to </div> right before </nav>
        content = re.sub(
            r'<div style="font-size:[^>]*>.*?</div>\s*</nav>',
            nav_links + '\n    </nav>',
            content,
            flags=re.DOTALL
        )
        
        # 3. Add mobile CSS if not present
        if 'nav > div:first-child' not in content:
            content = content.replace('@media (max-width: 900px) {', css_mobile_nav)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating navs and CSS.")
