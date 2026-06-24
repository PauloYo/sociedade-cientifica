import reflex as rx

from ..utils.api import get


class SearchState(rx.State):
    query: str = ""
    results: list[dict] = []
    loading: bool = False

    def set_query(self, v: str):
        self.query = v

    async def search(self):
        q = self.query.strip()
        if not q:
            self.results = []
            return
        self.loading = True
        yield
        try:
            raw = (await get(f"/documentos/{q}")).get("response", [])
            flat = []
            seen_ids = set()
            for doc in raw:
                doc_id = doc.get("_id", "")
                if doc_id in seen_ids:
                    continue
                seen_ids.add(doc_id)
                area = doc.get("nomArea", "")
                for p in doc.get("pesquisa", []):
                    flat.append({
                        "tipo": "Pesquisa",
                        "titulo": p.get("nomPesq", ""),
                        "subtitulo": p.get("crdn", {}).get("nomCrdn", ""),
                        "area": area,
                        "link": "/areas",
                    })
                for p in doc.get("publicacao", []):
                    flat.append({
                        "tipo": p.get("dscTipoPubl", "Publicação").capitalize(),
                        "titulo": p.get("nomTitPubl", ""),
                        "subtitulo": str(p.get("numAnoPubl", "")),
                        "area": area,
                        "link": "/publicacoes",
                    })
                for s in doc.get("software", []):
                    flat.append({
                        "tipo": "Software",
                        "titulo": s.get("nomSoft", ""),
                        "subtitulo": s.get("nomRespSoft", ""),
                        "area": area,
                        "link": "/softwares",
                    })
            self.results = flat
        except Exception as e:
            print(f"Erro na busca: {e}")
            self.results = []
        self.loading = False
        yield
