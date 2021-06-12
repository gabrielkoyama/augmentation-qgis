![title_pluginqgis.jpg](https://www.dropbox.com/s/asiq8e3suw3gpyb/title_pluginqgis.jpg?dl=0&raw=1)

[![Software License](https://img.shields.io/badge/license-MIT-green)](https://github.com/gabrielkoyama/augmentation_qgis/blob/main/LICENSE)
----

# Sumário
 - [Sobre o plugin](#1-Sobre)
 - [Instalação](#2-instalação)
    - [QGIS](#21-qgis)
	- [ZIP](#22-zip)
	- [Erros de instalação](#23-Erros-de-instalação)
 - [Execução](#3-execução)
 - [Manual das funções implementadas](#4-manual-das-funções-implementadas)
    - [Rotate](#Rotate) 
    - [Flip](#Flip) 
    - [Reshape](#Reshape) 
    - [Color](#Color) 
    - [Remote Sensing](#Remote-Sensing) 
    - [Augmentate](#Augmentate)
 - [Pacote](#5-pacote)
 - [License](#License)
## 1 Sobre
Esse plugin tem como objetivo fornecer _data augmentation_ dado uma imagem e pontos de interesse fornecidos.

---
## 2 Instalação
### 2.1 QGIS
Para instalar este plugin é necessário habilitar a opção para mostrar os complementos experimentais em **Complementos > Gerenciar e Instalar Complementos > Opções** e checar a opção  **Mostrar também os complementos experiementais**, como indicado na Figura 1.

![habilitar_opcoes.jpg](https://www.dropbox.com/s/1fk64xkba4n8oke/habilitar_opcoes.jpg?dl=0&raw=1)
**Figura 1:** Demonstrativo da tela de Complementos do _QGIS_ na seção Opções.

Feito isto, basta procurar por **Data Augmentation** no filtro de busca e clicar em **Instalar Complemento Experimental**.
![instalar_qgis.jpg](https://www.dropbox.com/s/ec9jxhgszqqyi8t/instalar_qgis.jpg?dl=0&raw=1)
**Figura 2:** Demonstrativo da tela de Complementos do _QGIS_ com a busca por _data augmentation_.

### 2.2 ZIP
Também é possível fazer a instalação manualmente com o projeto no formato _.zip_. Para isto basta fazer o _download_ dos códigos neste repostório e selecionar a opção **Instalar a partir do ZIP** na janela de plugins do QGIS e depois clicar em **Instalar Complemento**.
![zip_opcoes.jpg](https://www.dropbox.com/s/0ji0jxijrwdce9v/zip_opcoes.jpg?dl=0&raw=1) 
**Figura 3:** Demonstrativo da tela de Complementos do _QGIS_ com a instalação a partir do ZIP.

### 2.3 Erros de instalação
Caso ocorra algum erro na instalação do _plugin_ relacionado as dependências, recomendamos que tente primeiro instalar os pacotes **_scikit-image_** e **_opencv_** manualmente pelo **_Terminal Python_** do QGIS (Ctrl + Alt + P) usando os comandos:
```
import os
os.system("pip install scikit-image")
os.system("pip install opencv-python")
```
Após isso encerre o _QGIS_, abra novamente e tente reinstalar _plugin_.
![errocv2.jpg](https://www.dropbox.com/s/vchmvwepc4auism/errocv2.jpg?dl=0&raw=1)
**Figura 4:** Exemplo de erro na instalação do plugin.

## 3 Execução

O plugin apresenta uma interface contendo duas abas: **_Parameters_** para a definição dos parâmetros de execução e **_Results_** exibindo os resultados gerados pelo programa.

![Imgur](https://i.imgur.com/4nhqTzH.jpg)
**Figura 5:** Exemplo Interface do Plugin.

De acordo com a **Figura 5**, é possível dividir o processo em 5 passos: **(1)** seleção do layer no formato .tif ou .jp2; **(2)** seleção dos vetores com formato geométrico do tipo POINT e projeção geográfica EPSG:4326. Para a definição dos dados de entrada é possível escolher pelo layer ativo no QGIS ou realizando o upload no plugin;**(3)** é responsável pela definição dos métodos que serão aplicados no raster. Podendo ser métodos de rotação, cor, remodelar, giro ou sensoriamento remoto;**(4)** se trata de um método randômico, que aplica todos os outros métodos combinados, gerando uma grande quantidade de dados;**(5)**  área de exibição dos resultados gerados pelo algoritmo contendo uma TreeView separados por métodos e um canvas para a visualização da imagem.


## 4 Manual das funções implementadas
Nesta seção se encontra uma breve descrição das funções de _data augmentation_ implementadas no _plugin_ e alguns exemplos.

#### Rotate

<img src="https://i.imgur.com/jqJrjd9.png" width="150" height="150" /> <img src="https://i.imgur.com/hQfN0Is.png" width="150" height="150" /> <img src="https://i.imgur.com/WAChozl.png" width="150" height="150" />

**Figura 6:** Exemplo Rotate

| Método | Descrição |
| ------ | ------ |
| **90°** | Rotaciona a amostra em 90° no sentido anti-horário;
| **180°** | Rotaciona a amostra em 180° no sentido anti-horário;
| **270°** | Rotaciona a amostra em 270° no sentido anti-horário;


#### Flip

<img src="https://i.imgur.com/DnWzo1V.png" width="150" height="150" /> <img src="https://i.imgur.com/X8SB63p.png" width="150" height="150" />

**Figura 7:** Exemplo Flip

| Método | Descrição |
| ------ | ------ |
| **Horizontal** | Espelha a imagem horizontalmente
| **Vertical** | Espelha a imagem verticalmente

#### Reshape

<img src="https://i.imgur.com/muPXfOZ.png" width="150" height="150" /> <img src="https://i.imgur.com/eBh9Ero.png" width="150" height="150" /> <img src="https://i.imgur.com/K8ODGfm.png" width="150" height="150" /> <img src="https://i.imgur.com/NOVbaCL.png" width="150" height="150" />

**Figura 8:** Exemplo Reshape

| Método | Descrição |
| ------ | ------ |
| **Crop** | O comando _crop_ faz um recorte da amostra removendo, por padrão, 100 _pixels_ acima e à direta da amostra e 200 _pixels_ abaixo e à esquerda da amostra.
| **Rescale** | A função _rescale_ redimensiona a amostra a partir de uma razão. Por padrão o valor usado é 0.5.
| **Trim** | O comando _trim_ faz uma  aparagem da amostra a partir das bordas. Por padrão os valores são 50 (acima, à diretia) e 20 (abaixo, à esquerda).
| **Truncate** | Faz a truncagem de frequências da imagem, a partir de um limite máximo de frequência definido. Por padrão o _limiar de truncagem_ é dado por 100, enquanto que o valor de transformação dos pixels truncados é de 200.


#### Color

<img src="https://i.imgur.com/kBQLG7G.png" width="150" height="150" />

**Figura 9:** Exemplo Color

| Método | Descrição |
| ------ | ------ |
| **Binary** |  A função _binary_ faz uma binarização das frequências da imagem a partir de um limiar que, por padrão, é dado por 50. As frequências abaixo do limiar são atribuídas à cor branca e as que estiverem acima são atribuídas à cor preta.

#### Remote Sensing

<img src="https://i.imgur.com/XzUttTk.png" width="150" height="150" /> <img src="https://i.imgur.com/N3E3TSw.png" width="150" height="150" /> <img src="https://i.imgur.com/ziHHJ1i.png" width="150" height="150" /> <img src="https://i.imgur.com/v9ruGGT.png" width="150" height="150" />

**Figura 10:** Exemplo Remote Sensing

| Método | Descrição |
| ------ | ------ |
| **Cloud** | Simula a presença de nuvens na amostra a partir da aplicação de uma máscara de nuvem sobre a amostra a partir de template.
| **Degradation** | Faz a degradação diminuindo a resolução da imagem, ao somar uma constante as resoluções _x, y_. É usado para simular as diferentes resoluções das imagens de satéli tes.
| **Haze** | Essa função simula a presença de neblina na amostra. Para isso é realizado um desfoque na amostra aplicada a partir de uma função _Gaussiana_  (_Gaussian Blur_) com parâmetro _sigma_ = 2.
| **Sharpen Edges** | A função _sharpen edges_ aprimora o contraste da borda de uma imagem na tentativa de melhorar sua acutância (nitidez aparente). Por padrão, a frequência máxima do realce é dada por 120, o valor de transformação dos _pixels_ da borda é 255 e o valor de zona de abertura para definição de bordas.


#### Augmentate
A função _augmentate_ produz um grande conjunto de dados de _data augmentation_ a partir da aplicação de todas as técnicas descritas nessa seção nas amostras fornecidas usando parâmetros aleatórios.


## 5 Pacote
Data Augmentation também se encontra na versão de pacote com _Graphical User Interface_ (GUI) e _command-line interface_ (CLI) em linguagem _python_.
As instruções sobre como usá-lo em sua máquina estão no link seguir.

| Pacote | README |
| ------ | ------ |
| Python | [https://github.com/prog-geo/augmentation/blob/main/README.md][PlDb] |

## License

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
