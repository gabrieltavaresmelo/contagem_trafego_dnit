# CONTAGEM DE TRÁFEGO

O tráfego gerado é o efeito verificado quando melhorias em uma rodovia promovem o aumento do número de viagens, aumentando sua demanda. Deve-se, por isso, calcular a elasticidade da demanda da rodovia para estimar-se a parcela de tráfego gerado nos estudos de viabilidade técnica de rodovias federais brasileiras.

Este projeto realiza o scraping no site do DNIT, obtem os dados e estrutura no pandas.

---

## COLETA DOS DADOS

[VÍDEO EXPLICATIVO](https://youtu.be/2LRK0XQHB2M)
[LINK DE ACESSO AO VMD](https://servicos.dnit.gov.br/dadospnct/ContagemContinua)

## COMANDOS PARA CRIAR O AMBIENTE

```bash
$ conda info --envs
$ conda env remove --name icd01

$ conda create --name icd01 pip python=3.10.12
$ conda activate icd01
$ conda deactivate

```

---

## COMANDOS PARA EXECUTAR O PROJETO

```bash
$ pip install -r requirements.txt
$ conda install -c conda-forge jupyter
$ conda install -c conda-forge ipykernel nb_conda_kernels

# Rodando o script PYTHON
$ python contagem_trafego_dnit.py

# Rodando via Jupyter
$ jupyter notebook

```


# REFERÊNCIAS
https://servicos.dnit.gov.br/dadospnct/ContagemContinua
https://codeigo.com/python/convert-beautifulsoup-object-to-string/
http://www.anpet.org.br/anais32/documentos/2018/Trafego%20Urbano%20e%20Rodoviario/Trafego%20em%20Rodovias%20I/1_219_AC.pdf