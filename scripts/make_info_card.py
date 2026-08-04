import os

# This template creates a Neofetch-style terminal window in SVG format
SVG_TEMPLATE = """<svg width="490" height="230" viewBox="0 0 490 230" xmlns="http://www.w3.org/2000/svg">
  <style>
    .text {{ font-family: 'Courier New', Consolas, monospace; font-size: 14px; fill: #c9d1d9; }}
    .title {{ fill: #58a6ff; font-weight: bold; font-size: 16px; }}
    .key {{ fill: #7ee787; font-weight: bold; }}
    .line {{ opacity: 0; animation: slideIn 0.8s ease-out forwards; }}
    {keyframes}
    @keyframes slideIn {{
      0% {{ opacity: 0; transform: translateX(-15px); }}
      100% {{ opacity: 1; transform: translateX(0); }}
    }}
  </style>
  
  <!-- Terminal Background -->
  <rect width="490" height="230" fill="#0d1117" rx="8" ry="8" stroke="#30363d" stroke-width="1"/>
  
  <!-- Content Group -->
  <g transform="translate(25, 40)">
    {content}
  </g>
</svg>
"""

def generate_svg():
    # Your custom resume data mapped to the Neofetch layout
    lines = [
        ('<text class="text title">charan@github</text>', 0),
        ('<text class="text" y="15">----------------------------------</text>', 1),
        ('<text class="text" y="45"><tspan class="key">Now      </tspan><tspan>: AI Research Intern @ CHAI (IITM)</tspan></text>', 2),
        ('<text class="text" y="75"><tspan class="key">Edu      </tspan><tspan>: B.Tech CSBS @ KSRCT</tspan></text>', 3),
        ('<text class="text" y="105"><tspan class="key">Stack    </tspan><tspan>: Python, PyTorch, React, OpenCV, Unity</tspan></text>', 4),
        ('<text class="text" y="135"><tspan class="key">Highlight</tspan><tspan>: Google Student Ambassador (GSAP 2026)</tspan></text>', 5)
    ]
    
    content = ""
    keyframes = ""
    
    # Generate the staggered CSS delays and SVG elements
    for i, (html_line, delay_idx) in enumerate(lines):
        delay = delay_idx * 0.2  # 0.2 second stagger between each line printing
        keyframes += f".delay-{i} {{ animation-delay: {delay}s; }}\n    "
        content += f'<g class="line delay-{i}">{html_line}</g>\n    '
        
    final_svg = SVG_TEMPLATE.format(keyframes=keyframes, content=content)
    
    # Output the file to the root directory just like the guide expects
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "info-card.svg")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_svg)
        
    print(f"Success! Generated animated card at: {output_path}")

if __name__ == "__main__":
    generate_svg()
