from PIL import Image

def converter_rgb_para_cmyk(caminho_imagem_entrada, caminho_imagem_saida):
    try:
        imagem_rgb = Image.open(caminho_imagem_entrada)
        imagem_cmyk = imagem_rgb.convert('CMYK')
        imagem_cmyk.save(caminho_imagem_saida)

        print(f"Imagem convertida com sucesso e salva em: {caminho_imagem_saida}")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")


caminho_entrada = r'/home/pedro/Documents/opob/rgbtocmyk/aurora.jpg'
caminho_saida = r'/home/pedro/Documents/opob/rgbtocmyk/auroracmyk.jpg'

converter_rgb_para_cmyk(caminho_entrada, caminho_saida)