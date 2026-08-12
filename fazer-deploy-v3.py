"""Monta um pacote do site para upload manual no Cloudflare Pages.

O deploy normal sai do git (push na `main` publica). Este script serve para
publicar sem passar pelo repositório — em outro projeto Pages, por exemplo.
Deixa pronto:

    deploy-v3/              pasta para arrastar no Pages
    nex-v3-cloudflare.zip   mesma coisa empacotada, para arrastar de uma vez

Rodar depois de qualquer alteração no site:

    python fazer-deploy-v3.py

Os dois saem do zero a cada execução e ficam fora do git (são derivados).
"""

import io
import os
import re
import shutil
import zipfile

ORIGEM = "index.html"
PASTA = "deploy-v3"
ZIP = "nex-v3-cloudflare.zip"


def montar_pasta(html):
    if os.path.isdir(PASTA):
        shutil.rmtree(PASTA)
    os.makedirs(os.path.join(PASTA, "assets"))

    # Varre o arquivo inteiro, não só os src/href: os isométricos dos cartões
    # de segmento só aparecem como texto no script, atrás de {{ sg.iso }}.
    assets = sorted(set(re.findall(r"assets/[\w\-\.]+", html)))

    io.open(os.path.join(PASTA, "index.html"), "w", encoding="utf-8", newline="").write(html)
    shutil.copy2("support.js", os.path.join(PASTA, "support.js"))
    for a in assets:
        shutil.copy2(a, os.path.join(PASTA, a))
    return assets


def empacotar():
    # O index.html precisa ficar na raiz do zip: se tudo for parar dentro de
    # uma pasta, o Pages pode publicar o site em /deploy-v3/ em vez da raiz.
    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, _, arquivos in os.walk(PASTA):
            for a in sorted(arquivos):
                caminho = os.path.join(raiz, a)
                z.write(caminho, os.path.relpath(caminho, PASTA))


def main():
    html = io.open(ORIGEM, encoding="utf-8").read()

    if 'name="robots" content="noindex"' in html:
        aviso = "com noindex (nao vai ser indexada no Google)"
    else:
        aviso = "SEM noindex (vai ser indexada no Google)"

    assets = montar_pasta(html)
    empacotar()

    peso = sum(
        os.path.getsize(os.path.join(r, f))
        for r, _, fs in os.walk(PASTA)
        for f in fs
    )
    # Sem caracteres fora do ASCII: o console do Windows usa cp1252 e um "->"
    # bonitinho derruba o script inteiro com UnicodeEncodeError.
    print(f"{PASTA}/  ->  index.html + support.js + {len(assets)} imagens, {peso / 1024 / 1024:.2f} MB")
    print(f"{ZIP}  ->  {os.path.getsize(ZIP) / 1024 / 1024:.2f} MB")
    print(f"\nA pagina vai {aviso}.")
    print("No Cloudflare: Workers & Pages > Create > Pages > Upload assets, e arrastar o zip.")


if __name__ == "__main__":
    main()
