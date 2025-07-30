import re #ferramenta chamada expressões regulares (regex) 
#para procurar padrões em textos (como datas, palavras, etc.)”.
from typing import List #certas funções vão retornar listas de palavras

class ManipuladorTexto:
    def __init__(self, caminho_arquivo: str):
        self.caminho = caminho_arquivo
        self.texto = self._ler_arquivo()

    def _ler_arquivo(self) -> str:
        with open(self.caminho, 'r', encoding='utf-8') as f:
            return f.read()

    def palavras_comecam_com(self, letra: str) -> List[str]:
        return re.findall(rf'\b{letra}\w*', self.texto, re.IGNORECASE)

    def palavras_contem_letra(self, letra: str) -> List[str]:
        return re.findall(rf'\b\w*{letra}\w*\b', self.texto, re.IGNORECASE)

    def substituir_virgulas(self) -> str:
        return self.texto.replace(',', '.')

    def extrair_datas(self) -> List[str]:
        return re.findall(r'\d{2}/\d{2}/\d{4}', self.texto)

    def __len__(self) -> int:
        """Retorna o número de palavras no texto"""
        return len(re.findall(r'\b\w+\b', self.texto))

    def __str__(self) -> str:
        return f"Manipulador de texto do arquivo '{self.caminho}'"

