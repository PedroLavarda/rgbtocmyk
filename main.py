from PIL import Image
import os

def converter_rgb_para_cmyk(caminho_imagem_entrada, caminho_imagem_saida):
    """
    Converte uma imagem RGB para o espaço de cores CMYK.

    Args:
        caminho_imagem_entrada (str): O caminho para a imagem RGB de entrada.
        caminho_imagem_saida (str): O caminho para salvar a imagem CMYK convertida.
    """
    try:
        # Abre a imagem de entrada
        imagem_rgb = Image.open(caminho_imagem_entrada)

        # Converte a imagem para o modo CMYK
        imagem_cmyk = imagem_rgb.convert('CMYK')

        # Salva a nova imagem
        imagem_cmyk.save(caminho_imagem_saida)

        print(f"Imagem convertida com sucesso e salva em: {caminho_imagem_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo de imagem não foi encontrado em '{caminho_imagem_entrada}'")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")

if __name__ == '__main__':
    # --- Exemplo de Uso ---

    caminho_entrada = r'D:\Meus Documentos\Desktop\pasta\Vscode\fds\arara3.jpg'
    caminho_saida = r'D:\Meus Documentos\Desktop\pasta\Vscode\fds\arara3cmyk.jpg'

    # Verifica se o arquivo de entrada de exemplo existe antes de tentar converter
    if not os.path.exists(caminho_entrada):
        print(f"Por favor, crie um arquivo de imagem chamado '{caminho_entrada}' no mesmo diretório deste script para testar.")
    else:
        # Chama a função para realizar a conversão
        converter_rgb_para_cmyk(caminho_entrada, caminho_saida)