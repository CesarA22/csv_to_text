import csv

def csv_to_text():   
    # Solicita o caminho do arquivo CSV
    caminho_csv = input("Digite o caminho do arquivo .CSV: ")
    
    # Solicita o caminho do arquivo de saída
    caminho_saida = input("Digite o caminho do arquivo de saída: ")

    try:
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)

            with open(caminho_saida, 'w', encoding='utf-8') as saida:
                for linha in leitor_csv:
                    # Processa o artigo
                    artigo = linha.get("Artigo ")

                    # Processa outros campos, substituindo '-' por ''
                    descricao = linha.get("Descrição", "").replace('-', '')
                    diametro = linha.get("Diâmetro mm", "").replace('-', '')
                    profundidade = linha.get("Profundidade do furo ou de perfuração", "").replace('-', '')
                    materia_prima = linha.get("Matéria Prima", "").replace('-', '')
                    norma_din = linha.get("Norma DIN ", "").replace('-', '')
                    norma_rosca = linha.get("Norma da Rosca", "").replace('-', '')
                    revestimento = linha.get("Revestimento", "").replace('-', '')
                    furo = linha.get("Furo (Cego/Passante)", "").replace('-', '')
                    type_form = linha.get("Type/Form", "").replace('-', '')
                    materiais = linha.get("Materiais", "").replace('-', '')
                    tipo_rosca = linha.get("Tipo de Rosca (Cortada / Laminada)", "").replace('-', '')
                    numero_facas = linha.get("Número de facas", "").replace('-', '')
                    forma_haste = linha.get("Forma da Haste", "").replace('-', '')
                    refrigeracao_interna = linha.get("Refrigeração Interna", "").replace('-', '')

                    texto = [
                        f"O artigo {artigo} é {descricao}",
                        f"O artigo {artigo} tem um diâmetro em mm de {diametro}",
                        f"O artigo {artigo} permite uma Profundidade do furo ou de perfuração {profundidade}",
                        f"O artigo {artigo} segue a Norma da Rosca {norma_rosca}",
                        f"O artigo {artigo} segue a Norma DIN {norma_din}",
                        f"O artigo {artigo} é usado para revestimento {revestimento}",
                        f"O artigo {artigo} usa a matéria-prima {materia_prima}",
                        f"O artigo {artigo} tem um furo (Cego/Passante) {furo}",
                        f"O artigo {artigo} tem um número de facas igual a {numero_facas}",
                        f"O artigo {artigo} tem tipo/forma {type_form}",
                        f"O artigo {artigo} tem tipo de Rosca {tipo_rosca}",
                        f"O artigo {artigo} tem forma da Haste {forma_haste}",
                        f"O artigo {artigo} tem refrigeração líquida {refrigeracao_interna}",
                        f"O artigo {artigo} é adequado para a furação dos seguintes materiais {materiais}"
                    ]
                    
                    for linha in texto:
                        saida.write(linha + '\n')

        print(f"Saída escrita com sucesso em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

csv_to_text()

