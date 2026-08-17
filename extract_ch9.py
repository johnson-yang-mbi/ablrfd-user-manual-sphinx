import docx
import os

doc = docx.Document('docs/source/ABLRFD Users Manual.docx')
paras = doc.paragraphs

# Chapter 9: Technical Questions and Revision Requests
# Para 12892 (H1 heading) through end of document
SECTIONS = [
    (12892, len(paras), '9.1', 'Technical Questions and Revision Requests',
     '9.1-technical-questions-and-revision-requests'),
]


def convert_section(start_para, end_para, sec_num, sec_title):
    lines = []
    lines.append(f'## {sec_num} &emsp; {sec_title}')
    lines.append('')

    i = start_para
    while i < end_para:
        para = paras[i]
        style = para.style.name
        text = para.text

        if style in ('Heading 1', 'Heading 2'):
            i += 1
            continue

        if style in ('Normal', 'Body Text', 'Body Text Indent'):
            if not text.strip():
                if lines and lines[-1] != '':
                    lines.append('')
                i += 1
                continue
            t = text.replace('\t', ' ').strip()
            if t:
                lines.append(t)
                lines.append('')
            i += 1
            continue

        # Any other style
        if text.strip():
            lines.append(text.strip())
            lines.append('')
        i += 1

    return '\n'.join(lines)


out_dir = 'docs/source/chapter-09'
os.makedirs(out_dir, exist_ok=True)

index_content = '''```{raw} latex
\\clearpage
```

# Chapter 9 — Technical Questions and Revision Requests

```{toctree}
:maxdepth: 1

9.1-technical-questions-and-revision-requests
```
'''

with open(out_dir + '/index.md', 'w', encoding='utf-8') as f:
    f.write(index_content)
print('Written: index.md')

for start_p, end_p, sec_num, sec_title, filename in SECTIONS:
    content = convert_section(start_p, end_p, sec_num, sec_title)
    filepath = out_dir + '/' + filename + '.md'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {filename}.md ({len(content)} chars)')

print('Done!')
