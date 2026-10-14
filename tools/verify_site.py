from pathlib import Path
from html.parser import HTMLParser
import sys
root=Path(__file__).resolve().parents[1]
class Scan(HTMLParser):
 def __init__(self): super().__init__();self.urls=[];self.headings=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('a','link','img','script'): self.urls.append((tag,a.get('href',a.get('src',''))))
  if tag=='h1':self.headings.append('h1')
errors=[]
for p in sorted(root.glob('*.html')):
 s=Scan();s.feed(p.read_text())
 if len(s.headings)!=1:errors.append(f'{p.name}: {len(s.headings)} h1 elements')
 for tag,u in s.urls:
  if not u or u.startswith(('mailto:','tel:','http:','https:','#','data:')):continue
  target=(root/u.split('?',1)[0].split('#',1)[0])
  if not target.exists():errors.append(f'{p.name}: broken {tag} {u}')
print(f'Validated {len(list(root.glob("*.html")))} pages')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('PASS: one H1 per page and all local asset and navigation targets exist')
