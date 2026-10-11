from pathlib import Path
from html import escape as e
import json
import re
root=Path(__file__).parent;dist=root/'dist';projects=json.loads((root/'content.json').read_text());images=json.loads((root/'images.json').read_text())
resume='/assets/resume.pdf'
def shell(title,body,prefix="../"):
 document = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Mishthi Mahajan</title><meta name="description" content="Mishthi Mahajan’s research portfolio: history, numismatics, epigraphy, heritage conservation, and museum studies."><link rel="stylesheet" href="/style.css?v=10"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' rx='6' fill='%23dcc19b'/%3E%3Ctext x='6' y='29' font-family='Georgia' font-size='29' fill='%23302f28'%3EM%3C/text%3E%3C/svg%3E"></head><body class="{'home-page' if title == 'Research & Heritage' else 'case-study'}"><a class="skip" href="#main">Skip to content</a><div class="page"><header><a class="brand" href="/" aria-label="Mishthi Mahajan home"><span>Mishthi</span><span>Mahajan</span></a><nav aria-label="Main navigation"><a href="/#work">My work</a><a href="/#about">About</a><a href="/#contact">Contact</a><a class="resume" href="{resume}" target="_blank" rel="noopener">Résumé ↗</a></nav></header><main id="main">{body}</main><footer><span>© Mishthi Mahajan</span></footer></div></body></html>'''
 return re.sub(r'(\b(?:href|src)=["\'])/(?!/)', lambda m: m.group(1) + prefix, document)

def img(name,alt='',lazy=True):return f'<img src="/assets/{name}" alt="{e(alt)}"'+(' loading="lazy"' if lazy else '')+'>'
groups=[('Historical research','Reading the past through images, objects, and inscriptions.',projects[:3]),('Heritage in practice','Documenting, conserving, and interpreting cultural heritage.',projects[3:])]
work_groups=''
project_labels=['Economic narratives in art','Mughal coin hoard of Patur','Naneghat inscription of Naganika','St. Xavier’s conservation plan','IZRAZ Art Museum']
project_summaries=['Tracing Mumbai’s economic transformation through European paintings.','Photographing and cataloguing 3,600 Mohurs from the Surat mint.','Reading royal identity, ritual, and changing letterforms at Naneghat.','A 68-page action plan informed by field surveys and material analysis.','A 55-page museum proposal covering collections, conservation, and visitor experience.']
for group_index,(title,description,items) in enumerate(groups):
 rows=''
 for p in items:
  i=int(p['n'])-1
  rows+=f'''<a class="project-row" href="/{p['slug']}/"><span class="project-number">{p['n']}</span><div class="project-thumb">{img(p['image'],p['subtitle'])}</div><div class="project-summary"><span class="project-type">{p['type']}</span><h4>{project_labels[i]}</h4><p>{project_summaries[i]}</p><span class="project-cta">View project <span aria-hidden="true">↗</span></span></div></a>'''
 work_groups+=f'''<section class="work-group" aria-labelledby="work-group-{group_index}"><div class="group-heading"><span class="hand">0{group_index+1}</span><h3 id="work-group-{group_index}">{title}</h3><p>{description}</p><span class="group-count">{len(items)} projects</span></div><div class="project-list">{rows}</div></section>'''
current_work='''<section class="current-work" aria-labelledby="current-work-title"><div class="current-role"><span class="work-status">Work in progress</span><h3 id="current-work-title">Current research</h3><p><strong>Associate Researcher</strong><br>The Earth News · Jammu, India</p></div><div class="current-project"><p class="eyebrow">Historiography · Political memory</p><h3><a href="/earth-news-research/">Gulab Singh and the Political Life of Historiographical Condemnation</a></h3><p>Examining competing historical interpretations of Gulab Singh and their role in public memory.</p><a class="text-link" href="/earth-news-research/">Explore ongoing research ↗</a></div></section>'''
body=f'''<section class="hero" aria-labelledby="intro-title"><div class="hero-copy"><div class="eyebrow">History · Heritage · Research</div><h1 id="intro-title">Piecing together<br>the stories<br><em>of our past.</em></h1><p>I’m Mishthi Mahajan. I explore the connections between people, places, and the material traces they leave behind.</p><a class="button" href="#work">Explore my work ↓</a></div><div class="collage"><figure class="polaroid">{img('home-0.jpg','Mishthi Mahajan',False)}</figure><div class="note"><span class="eyebrow">Research interests</span><p>Art &amp; archives<br>Objects &amp; inscriptions<br>People &amp; environments</p></div></div></section><section class="work" id="work"><div class="section-head"><div><h2>Selected work</h2></div></div>{current_work}{work_groups}</section><section class="about" id="about"><figure class="about-photo taped">{img('home-1.jpg','Mishthi Mahajan outdoors')}</figure><div><h2>About me</h2><p>I currently work as an Associate Researcher at The Earth News in Jammu, India.</p><p>My academic path began at the University of Delhi in History and Political Science and deepened at St. Xavier’s College, Mumbai, where I specialised in Ancient Indian History.</p><p>I bring together perspectives from archaeology, economics, ecology, and culture to reveal more layered historical narratives.</p><p>I aim to pursue a PhD in Environmental History, focusing on resource extraction and the ecological, cultural, and economic dimensions of human–environment relations.</p><p>Beyond research, you’ll find me trekking, experimenting in the kitchen, or exploring books that change how I see the world.</p></div></section><section class="contact" id="contact"><div><h2>Get in touch</h2><a class="email" href="mailto:mishthi2402@gmail.com">mishthi2402@gmail.com</a></div><aside><a href="https://www.linkedin.com/in/mishthimahajan" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{resume}" target="_blank" rel="noopener">Résumé ↗</a></aside></section>'''
(dist/'index.html').write_text(shell('Research & Heritage',body,prefix='./'))
for n,p in enumerate(projects):
 if p['slug']=='epigraphy-project':
  folder=dist/p['slug'];folder.mkdir(exist_ok=True)
  (folder/'index.html').write_text(shell(p['title'],(root/'case-epigraphy.html').read_text()))
  continue
 toc=''.join(f'<a href="#section-{i}">{e(s[0])}</a>' for i,s in enumerate(p['sections']))
 sections=''.join(f'<section id="section-{i}"><h2>{e(s[0])}</h2><p>{e(s[1])}</p></section>' for i,s in enumerate(p['sections']))
 gallery=''
 for i,name in enumerate(images[p['slug']]):
  label=f'Research plate {i+1}' if p['slug']=='epigraphy-project' else f'Figure {i+1}'
  gallery+=f'<figure><a href="/assets/{name}" target="_blank" rel="noopener" aria-label="Open {label.lower()} at full size">{img(name,label)}</a><figcaption>{label} · <a href="/assets/{name}" target="_blank" rel="noopener">View full size ↗</a></figcaption></figure>'
 report=f'<a class="button" href="{p["report"]}" target="_blank" rel="noopener">Read the complete report ↗</a>' if p.get('report') else ''
 nxt=projects[(n+1)%len(projects)]
 body=f'''<a class="breadcrumb" href="/#work">← All projects</a><section class="project-top"><div><span class="eyebrow">{p['n']} / {p['type']}</span><h1>{p['title']}</h1><p class="subtitle">{p['subtitle']}</p><p class="eyebrow">{p['tags']}</p>{report}</div><figure class="taped">{img(p['image'],p['subtitle'],False)}</figure></section><div class="project-layout"><aside class="contents"><span class="eyebrow">In this project</span>{toc}<a href="#project-gallery">Images</a></aside><article class="prose"><p class="intro">{p['intro']}</p>{sections}<section id="project-gallery"><h2>Images</h2><div class="gallery {'plates' if p['slug']=='epigraphy-project' else ''}">{gallery}</div></section>{report}</article></div><div class="next"><a href="/#work">← Back to selected work</a><a href="/{nxt['slug']}/">Next: {nxt['title']} →</a></div>'''
 folder=dist/p['slug'];folder.mkdir(exist_ok=True);(folder/'index.html').write_text(shell(p['title'],body))
print('Created homepage and five project pages.')

folder=dist/"earth-news-research";folder.mkdir(exist_ok=True)
(folder/"index.html").write_text(shell("Current research at The Earth News",(root/"case-earth-news.html").read_text()))

(dist/".nojekyll").touch()
