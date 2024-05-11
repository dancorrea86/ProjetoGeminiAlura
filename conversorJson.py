import json
import os
import re

def md_to_json(md_file, json_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()

    title = md_file.split("\\")[-1].replace(".md", "")
    text = '\n'.join(text.splitlines()[1:])
    text = text.replace("\n", "")
    text = text.replace("​","")
    text = text.replace(" "," ")
    text = text.replace("–", "-")
    text = text.replace("–", "")
    text = text.replace("[[", "")
    text = text.replace("]]", "")
    



    data = {
        'titulo': title,
        'conteudo': text
    }

        # Carrega o conteúdo do arquivo JSON (se existir)
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = []

    # Adiciona o novo objeto de dados à lista
    existing_data.append(data)

   

    # Salva a lista atualizada no arquivo JSON
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Define o nome do arquivo JSON de saída
    output_file = "md_data.json"
    pasta = "./biblioteca"

    for filename in os.listdir(pasta):
        if filename.endswith('.md'):
            # Constrói o caminho completo do arquivo MD
            md_file = os.path.join(os.getcwd(), "biblioteca\\" + filename)
            
            # Converte o arquivo MD para JSON
            md_to_json(md_file, output_file)

    print(f"Arquivos MD convertidos para {output_file}")