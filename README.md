# NEX Galpones Paraguay — site institucional

Site estático da NEX Galpones Paraguay (Grupo NEX · operação paraguaia da Rótula Metalúrgica). Conteúdo em espanhol (es-PY).

## Estrutura

| Arquivo | O que é |
| --- | --- |
| `index.html` | **Site oficial** — SPA de 3 páginas (Inicio, Tecnología, Contacto) sobre o runtime próprio `support.js`. É a antiga v3: sem as páginas Obras e Empresa, sem nenhuma foto de obra e sem citar a Rótula pelo nome. No lugar do portfólio, uma lâmina de anatomia — isométrico acotado com as peças numeradas |
| `v1.html` | **Versão anterior (v1)** — as 5 páginas originais (Inicio, Empresa, Tecnología, Obras, Contacto), com o portfólio de 17 obras. Conservada como referência, com `noindex` |
| `v2.html` | **Versão-conceito editorial (v2)** — one-page standalone, com `noindex` |
| `support.js` | Runtime do template (gerado — não editar à mão) |
| `assets/` | Imagens do site (heros otimizados, portadas, isométricos) |
| `uploads/` | Material de origem (apresentação comercial, imagens curadas) |

Só o `index.html` é indexável. As outras duas versões continuam acessíveis por link direto, para comparar.

## Rodar localmente

```bash
python -m http.server 8788
```

Depois abrir <http://localhost:8788/> (site atual), <http://localhost:8788/v1.html> ou <http://localhost:8788/v2.html>.

## Deploy

Hospedado no Cloudflare Pages, conectado a este repositório: cada push na `main` publica automaticamente. Site estático puro — sem framework, sem build command, output na raiz (`/`).

### Pacote para upload manual (opcional)

Se for preciso publicar o site em outro projeto Pages sem passar pelo git (*Create application › Pages › Upload assets*):

```bash
python fazer-deploy-v3.py
```

O script monta `deploy-v3/` com o `index.html`, o `support.js` e só as 14 imagens que a página usa — o `assets/` completo tem mais de 100 arquivos — e empacota tudo em `nex-v3-cloudflare.zip`, com o `index.html` na raiz do arquivo (dentro de uma pasta, o Pages publicaria o site em um subcaminho). Pasta e zip ficam fora do git de propósito: são derivados.

## Pendências antes de publicar

- Trocar os placeholders de contato: `wa.me/595000000000` e `+595 21 000 000`
- Configurar `ENDPOINT_FORMULARIO` no script do site (sem endpoint, o formulário abre o cliente de e-mail do visitante com a solicitação pronta)
- Definir o domínio final nas metas `og:` e no `canonical`
