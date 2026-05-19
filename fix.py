import os

filepath = 'c:/Users/paulg/graciegray.co.uk/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if line.strip() == '<h2>Supporting the whole family, not just the new arrival.</h2>':
        new_lines.append(line)
        new_lines.append('            </div>\n')
        new_lines.append('            <div class=\"pillars-grid stagger-children\">\n')
        new_lines.append('                <div class=\"pillar fade-up\">\n')
        new_lines.append('                    <div class=\"pillar-icon\">&#128118;</div>\n')
        new_lines.append('                    <h3>Baby-led care</h3>\n')
        new_lines.append('                    <p>Expert care for your newborn, giving you the space to be fully present with your older children — reassuring them of their vital place in the family.</p>\n')
        new_lines.append('                </div>\n')
        new_lines.append('                <div class=\"pillar fade-up\">\n')
        new_lines.append('                    <div class=\"pillar-icon\">&#127912;</div>\n')
        new_lines.append('                    <h3>Child-led support</h3>\n')
        new_lines.append('                    <p>Engaging, interactive activities with your older children so you can enjoy completely guilt-free, uninterrupted bonding time with your new baby.</p>\n')
        new_lines.append('                </div>\n')
        new_lines.append('                <div class=\"pillar fade-up\">\n')
        new_lines.append('                    <div class=\"pillar-icon\">&#128156;</div>\n')
        new_lines.append('                    <h3>Whole family care</h3>\n')
        new_lines.append('                    <p>Birth trauma support, antenatal preparation, and full-family integration — helping your family find its new rhythm together.</p>\n')
        new_lines.append('                </div>\n')
        new_lines.append('            </div>\n')
        new_lines.append('        </div>\n')
        new_lines.append('    </section>\n')
        new_lines.append('\n')
        new_lines.append('    <!-- Pull Quote -->\n')
        new_lines.append('    <section class=\"pull-quote\">\n')
        new_lines.append('        <div class=\"container fade-up\">\n')
        new_lines.append('            <blockquote style=\"max-width: 800px; margin: 0 auto; font-size: 1.8rem; line-height: 1.4;\">\"A woman, as long as she lives, will remember how she was made to feel at her birth.\"</blockquote>\n')
        new_lines.append('            <cite style=\"margin-top: 1.5rem; display: block;\">— Anna Verwaal</cite>\n')
        new_lines.append('        </div>\n')
        new_lines.append('    </section>\n')
        new_lines.append('\n')
        new_lines.append('    <!-- About Preview -->\n')
        new_lines.append('    <section class=\"about-preview\">\n')
        new_lines.append('        <div class=\"container\">\n')
        new_lines.append('            <div class=\"about-grid\">\n')
        new_lines.append('                <div class=\"about-image fade-up\">\n')
        new_lines.append('                    <img src=\"assets/images/gracie-bench-newborn.jpg\" alt=\"Gracie Gray Norland Nanny holding newborn baby in Bath Somerset\" class=\"img-soft\" style=\"width: 100%; height: 400px; object-fit: cover;\">\n')
        new_lines.append('                </div>\n')
        new_lines.append('                <div class=\"about-text fade-up\">\n')
        new_lines.append('                    <span class=\"accent-text\">Grace\\'s Story</span>\n')
        new_lines.append('                    <h2>13 years of experience. A Norland education. A mother\\'s understanding.</h2>\n')
        new_lines.append('                    <p>Gracie is a mother of three. Having her first child young, and navigating an unexpected medical diagnosis of bilateral talipes with her eldest, gave her a profound, lived understanding of the hospital system and the fears of a new mother when birth doesn\\'t go to plan.</p>\n')
        new_lines.append('                    <p>As a Norland Nanny awarded the prestigious Principal Award — the highest-standing student of her year — she brings the global gold standard of childcare directly into your home.</p>\n')
        new_lines.append('                    <ul class=\"credentials-list\">\n')
        new_lines.append('                        <li>Norland Diploma</li>\n')
        new_lines.append('                        <li>Principal Award</li>\n')
        new_lines.append('                        <li>BA Hons</li>\n')
        
    elif i > 82 and i < 84:
        pass # Skip the corrupted lines
    else:
        new_lines.append(line)

# Remove lines 83 to 89 manually
with open(filepath, 'w', encoding='utf-8') as f:
    for line in new_lines:
        f.write(line)

print('Done')
