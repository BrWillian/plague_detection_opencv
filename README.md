# Detecção de pragas

Bem-vindo/a ao repositório contendo esse projeto.  

## :scroll: Sobre o projeto
O teste consiste em detectar, enumerar e recriar máscara para as pragas nas plantações.

## :clipboard: Requisitos

### Requisitos obrigatórios
Este repositório contêm requisitos necessários para estruturação do projeto.

* Documentação
  * Instruções de instalação, inicialização.
  * Descrição sobre as tecnologias utilizadas no projeto
* Características do detector.
  * Testes

## :computer: Utilização

### Modo de utilização
* Realizar instalação das depêndencias \
`$ pip3 install -r requeriments.txt`
* Após instalação das depêndencias podemos consultar a mini documentação guia \
`python3 main.py --help`

<pre>
usage: main.py [-h] [--sensitivity SENSITIVITY] [--circles] [--no-circles]
               --image IMAGE

optional arguments:
  -h, --help            show this help message and exit
  --sensitivity SENSITIVITY
                        Sensibilidade do detector (default: 30)
  --circles             Desenhar circulo nas detecções (default: False)
  --no-circles          Não desenhar circulo nas detecções (default: False)
  --image IMAGE         Caminho da imagem (default: None)
</pre>
### Exemplos de uso
* Para uma detecção simples segue abaixo código exemplo.\
`$ python3 main.py --image="caminho da imagem aqui"`
* O código acima realiza uma detectção básica, porém podem ser alteradas todas caracteriscas conforme o --help mostra.
* Para realizar uma detecção com desenho de circulos (para melhor visualização das detecções) segue abaixo código exemplo.\
`$ python3 main.py --image="caminho da imagem aqui" --circles`
* ou \
`$ python3 main.py --image="caminho da imagem aqui" --no-circles`
* O modelo também dispôe de um parametro para aumentar ou diminuir a sensibilidade da detecção segue abaixo código exemplo.\
* `$ python3 main.py --image="caminho da imagem aqui" --circles --sensibility=30`

## :bulb: Exemplos

### Exemplos de imagens
* As imagens utilizadas neste projeto foram imagens disponibilizadas pela empresa [Solinftec](https://www.solinftec.com/pt-br/), portanto todos direitos reservados a eles.

> <img src="https://github.com/BrWillian/plague_detection_opencv/blob/master/data/mato-grosso.jpeg?raw=true" width="250" hspace="50" >
> <img src="https://github.com/BrWillian/plague_detection_opencv/blob/master/data/aracatuba.jpg?raw=true" width="330">
> <p align="center">Exemplos de entrada.</p>


> <img src="https://github.com/BrWillian/plague_detection_opencv/blob/master/output/mato-grosso_filled.jpg?raw=true" hspace="50" width="250">
> <img src="https://github.com/BrWillian/plague_detection_opencv/blob/master/output/aracatuba_circle.jpg?raw=true" width="330"><p>
> <p align="center">Exemplo de saída sem círculos e com círculos</p>

* Na pasta data/ segue os exemplos utilizados no teste.

### Referências
* Todo a codificação está presente na documentação do opencv disponivel em:
[Link](https://docs.opencv.org/4.x/)


Boa sorte! :boom:

---
