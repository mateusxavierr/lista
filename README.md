# 🛒 Lista de Compras (CLI) com Lixeira — Python

Aplicativo de linha de comando para **gerenciar uma lista de compras**, com suporte a **lixeira** (recuperação de itens apagados) e **persistência em JSON**.  
Os arquivos `lista.json` e `lixeira.json` são criados automaticamente **na mesma pasta do script**.

## 🚀 Funcionalidades
- ➕ Adicionar itens à lista.  
- ❌ Apagar itens por índice (vai para a **lixeira**).  
- 📜 Listar itens da lista.  
- 🗑️ Acessar a lixeira para:  
  - Recuperar um item por índice.  
  - Recuperar todos os itens.  
  - Esvaziar a lixeira.  
- 💾 Persistência automática em JSON.  

## 📂 Estrutura dos Arquivos
```
list.py         # Script principal (CLI)
lista.json      # Lista de compras
lixeira.json    # Itens apagados (lixeira)
```

## ▶️ Como Executar
1. Garanta que você tem **Python 3.10+** instalado.  
2. No terminal, execute:
   ```bash
   python3 list.py
   ```

## 🧭 Menu Principal
```
1 - Inserir
2 - Apagar
3 - Listar
4 - Lixeira
5 - Sair
```

### 🗑️ Submenu da Lixeira
```
1 - Voltar
2 - Recuperar um
3 - Recuperar tudo
4 - Esvaziar lixeira
```

## ⚡ Exemplo de Uso
```
Lista de compras: selecione uma opção
1 - Inserir
2 - Apagar
3 - Listar
4 - Lixeira
5 - Sair

> 1
Digite o que deseja inserir: Arroz

> 3
0 - Arroz
```

## 🛠️ Tecnologias
- Python 3  
- Módulo padrão `json`  
- Módulo padrão `os`  

## 🗺️ Melhorias Futuras
- Ordenar e editar itens.  
- Marcar itens como concluídos.  
- Buscar/filtrar por texto.  
- Exportar/Importar CSV.  

## 📄 Licença
Projeto livre para estudos e uso pessoal.
