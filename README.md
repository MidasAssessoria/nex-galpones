# NEX Galpones Paraguay — site institucional

Site estático da NEX Galpones Paraguay (Grupo NEX · operação paraguaia da Rótula Metalúrgica). Conteúdo em espanhol (es-PY).

## Estrutura

| Arquivo | O que é |
| --- | --- |
| `index.html` | **Site oficial (v1)** — SPA de 5 páginas (Inicio, Empresa, Tecnología, Obras, Contacto) sobre o runtime próprio `support.js`. É o `.dc.html` de antes, renomeado para ser servido na raiz do domínio |
| `v2.html` | **Versão-conceito editorial (v2)** — one-page standalone, com `noindex` enquanto não substituir a v1 |
| `support.js` | Runtime do template (gerado — não editar à mão) |
| `assets/` | Imagens do site (heros otimizados, portadas, isométricos) |
| `uploads/` | Material de origem (apresentação comercial, imagens curadas) |

## Rodar localmente

```bash
python -m http.server 8788
```

Depois abrir <http://localhost:8788/> (v1) ou <http://localhost:8788/v2.html> (v2).

## Deploy

Hospedado no Cloudflare Pages, conectado a este repositório: cada push na `main` publica automaticamente. Site estático puro — sem framework, sem build command, output na raiz (`/`).

## Pendências antes de publicar

- Trocar os placeholders de contato: `wa.me/595000000000` e `+595 21 000 000`
- Configurar `ENDPOINT_FORMULARIO` no script da v1 (sem endpoint, o formulário abre o cliente de e-mail do visitante com a solicitação pronta)
- Definir o domínio final nas metas `og:` e no `canonical`
