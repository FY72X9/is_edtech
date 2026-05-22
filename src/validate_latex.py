import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

TEX = r"d:\BINUS Works\Codes\research_banks\research\is_edtech\docs\latex\paper\main.tex"
IMGS = r"d:\BINUS Works\Codes\research_banks\research\is_edtech\images"

with open(TEX, encoding='utf-8') as f:
    tex = f.read()

errors = []

# 1. Balanced environments
for env in ['document','abstract','table','table*','figure','figure*',
            'equation','thebibliography','itemize']:
    b = len(re.findall(r'\\begin\{' + re.escape(env) + r'\}', tex))
    n = len(re.findall(r'\\end\{'   + re.escape(env) + r'\}', tex))
    if b != n:
        errors.append(f'UNBALANCED [{env}]: {b} begin / {n} end')

# 2. Em dash in non-comment lines
for i, line in enumerate(tex.split('\n'), 1):
    s = line.strip()
    if '\u2014' in s and not s.startswith('%'):
        errors.append(f'EM DASH line {i}: {s[:70]}')

# 3. Citation / bibitem consistency
cites   = set(re.findall(r'\\cite\{(b\d+)\}', tex))
bibkeys = set(re.findall(r'\\bibitem\{(b\d+)\}', tex))
for k in sorted(cites - bibkeys):
    errors.append(f'MISSING bibitem: {k}')
for k in sorted(bibkeys - cites):
    errors.append(f'ORPHAN bibitem (uncited): {k}')

# 4. Figure files
for ref in re.findall(r'\\includegraphics\[.*?\]\{([^}]+)\}', tex):
    base = os.path.basename(ref)
    found = any(os.path.exists(os.path.join(IMGS, base + ext))
                for ext in ('', '.png', '.jpg', '.pdf'))
    if not found:
        errors.append(f'MISSING image file: {base}')

lines = tex.split('\n')
print(f'Lines  : {len(lines)}')
print(f'Chars  : {len(tex):,}')
print(f'Cites  : {sorted(cites)}')
print(f'Bib    : {sorted(bibkeys)}')
print()
if errors:
    print(f'{len(errors)} error(s):')
    for e in errors:
        print(f'  {e}')
else:
    print('All checks passed -- no structural errors found.')
