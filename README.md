# Lista de Compras em Python 🛒  
![Status](https://img.shields.io/badge/status-finalizado-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Lógica](https://img.shields.io/badge/conceito-de-listas-purple)
![Feito por](https://img.shields.io/badge/feito%20por-Israel%20Brito-orange)

## 📌 Sobre o Projeto  
Este programa simula uma **lista de compras** onde o usuário pode inserir itens um por vez.  
A coleta continua até que seja digitado **"fim"**, independentemente de maiúsculas ou minúsculas.  
Ao final, todos os itens são exibidos em **ordem alfabética crescente**, um por linha.

## 🧠 Como o Código Funciona  
1. Uma lista vazia é criada para armazenar os itens:  
   ```python
   lista_de_compras = []
   ```
2. O programa solicita que o usuário digite um item.  
3. O processo se repete até o usuário escrever **"fim"**.  
4. Todos os itens armazenados são ordenados com `.sort()`  
5. A lista organizada é exibida linha por linha.

## ▶️ Como Executar  
1. Execute o arquivo Python no terminal.  
2. Digite os itens da lista conforme desejar.  
3. Quando quiser encerrar, digite:  
   ```
   fim
   ```
4. A saída será semelhante a:  
   ```
   abacaxi
   arroz
   leite
   pão
   ```

## 📝 Exemplo de Uso  
Entrada:  
```
leite
arroz
leite
pão
fim
```  
Saída:  
```
arroz
leite
leite
pão
```

## 🎯 Objetivo  
- Praticar o uso de **listas**  
- Aplicar loops com condição de parada  
- Reforçar manipulação de strings  
- Exercício simples e direto de lógica de programação

## 📈 Possíveis Melhorias  
- Impedir duplicações automaticamente  
- Permitir remover itens da lista  
- Salvar a lista em arquivo `.txt`  
- Criar um menu interativo no terminal

## 👨‍💻 Autor  
**Israel Brito**  
Projeto desenvolvido para estudo de lógica e manipulação de listas em Python.
