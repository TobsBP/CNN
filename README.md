# Câmera de Reconhecimento de Números

Reconhecimento em tempo real de números (1-4) usando webcam com features HOG e classificador SVM.

Pressione **Espaço** para capturar um frame, o número detectado é salvo em `resultado.txt`. Pressione **Espaço** novamente para sobrescrever com uma nova detecção. Pressione **Q** para sair.

## Estrutura do Projeto

```
cnn/
├── main.py            # App da webcam - captura e prediz ao pressionar tecla
├── train.py           # Script de treino - constrói o modelo SVM
├── number_model.pkl   # Modelo treinado (gerado pelo train.py)
├── resultado.txt      # Arquivo de saída com o último número detectado
├── dataset/
│   ├── 1/             # Imagens do número 1 (.jpeg)
│   ├── 2/             # Imagens do número 2 (.jpeg)
│   ├── 3/             # Imagens do número 3 (.jpeg)
│   └── 4/             # Imagens do número 4 (.jpeg)
└── pyproject.toml
```

## Como Executar no Windows

### Pré-requisitos

- **Python 3.12+** - Baixe em [python.org](https://www.python.org/downloads/)
  - Durante a instalação, marque **"Add Python to PATH"**
- **Webcam** conectada ao seu computador

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd cnn
```

### 2. Instale o Poetry (gerenciador de pacotes)

Abra o **PowerShell** e execute:

```powershell
pip install poetry
```

### 3. Instale as dependências

```powershell
poetry install
```

### 4. Prepare o dataset

Coloque suas imagens de treino dentro da pasta `dataset/`, organizadas por número:

```
dataset/
├── 1/
│   ├── img1.jpeg
│   ├── img2.jpeg
│   └── ...
├── 2/
│   └── ...
├── 3/
│   └── ...
└── 4/
    └── ...
```

As imagens devem estar no formato `.jpeg`.

### 5. Treine o modelo

```powershell
poetry run python train.py
```

Isso gera o arquivo `number_model.pkl`.

### 6. Execute a aplicação

```powershell
poetry run python main.py
```

### Controles

| Tecla   | Ação                                                      |
|---------|-----------------------------------------------------------|
| `Espaço`| Captura frame, prediz número, salva em resultado.txt      |
| `Q`     | Encerra a aplicação                                       |

## Gerando um Executável (.exe)

Para criar um `.exe` standalone para Windows (não precisa de Python para rodar):

```powershell
poetry run pyinstaller --onefile --add-data "number_model.pkl;." main.py
```

O executável estará na pasta `dist/`.

> **Nota:** Certifique-se de treinar o modelo primeiro (`train.py`) antes de gerar o executável.
