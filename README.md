# Renomeador de Arquivos

Este script Python renomeia arquivos em um diretório, removendo acentos, caracteres especiais e strings específicas. Ele também converte os nomes para minúsculas e substitui espaços por hífens.

## Funcionalidades

- **Remove Acentos**: Remove automaticamente acentos dos caracteres.
- **Remove Caracteres Especiais e Strings Específicas**: Personalize a remoção de caracteres e strings como `@`, `#`, `1900x800`, entre outros.
- **Converte para Minúsculas**: Todos os nomes de arquivos são convertidos para minúsculas.
- **Substitui Espaços por Hífens**: Espaços são substituídos por hífens (`-`).

## Como Usar

1. **Baixe o Script**: Copie o código do script para o seu computador.
2. **Coloque os Arquivos na Pasta Correta**: Coloque todos os arquivos que deseja renomear na mesma pasta onde o script será executado.
3. **Execute o Script**:

    ```bash
    python rename.py
    ```

4. **Personalize a Lista de Caracteres e Strings a Remover**: Na variável `caracteres_indesejados`, adicione as strings ou caracteres que deseja remover. Exemplo:

    ```python
    caracteres_indesejados = ['@', '=', '%', '#', '1900x800', '?', '^', '{', '}', '[', ']', 'exemplo123']
    ```

5. **Renomeação Completa**: O script renomeia todos os arquivos, exibindo os nomes antigos e novos.

## Personalização

- **Adicionar ou Remover Strings**: Altere a lista `caracteres_indesejados` para remover quaisquer caracteres ou strings que desejar, como `1900x800`, `exemplo123`, etc.
- **Alterar Diretório de Execução**: Para renomear arquivos de um diretório específico, altere a variável `pasta_atual` para o caminho desejado.

## Considerações Finais

Este script é uma solução prática para organizar arquivos, removendo caracteres indesejados e garantindo uma nomenclatura padronizada.
