# Atividade 01 - APIs e Web Services

**Disciplina:** APIs e Web Services (AWS)
**Atividade:** 01 – Protocolo HTTP
**Link para acesso**: <https://github.com/ferreirawill/soap-client>

**Integrantes**:

* Jéssica Souza Pivoto
* William Carlos Moreira Ferreira

___

### Questões

**1) Crie uma aplicação simples, utilizando a linguagem/plataforma que você preferir, que consuma um Web Service SOAP. Implemente pelo menos três operações Web Service de exemplo: <https://www.crcind.com/csp/samples/SOAP.Demo.cls>**

Foi desenvolvida uma aplicação que consome informações do serviço: [DataFlex WebService for Country information](!http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso). Essa aplicação tem como objetivo apresentar informações de um determinado país para o usuário após ele digitar o nome, em inglês, deste no console. As informações que são apresentadas são:

* ISO Code do país
* A capital do país
* A moeda utilizada no país
* O DDI do país

O código fonte foi escrito em Python, utilizando a biblioteca [Zeep](!https://docs.python-zeep.org/en/master/) para efetuar as requisições. As operações implementadas desse serviço foram:


| Objetivo | Operação |
| ------------- | ------------- |
| Buscar ISO Code do país  | CountryISOCode  |
| Buscar capital do país  | CapitalCity  |
| Buscar moeda utilizada no país  | CountryCurrency  |
| Buscar DDI do país  | CountryIntPhoneCode  |

O código que executa essas operações está disponível em: [SoapClient.py no GITHUB](https://github.com/ferreirawill/soap-client/blob/master/SoapClient.py)


**2) Instale um proxy HTTP na sua máquina e verifique as mensagens enviadas/recebidas quando a sua aplicação acessa algum dos recursos implementados no Web Service.**

O analisador de protocolo utilizado para capturar as requisições da aplicação foi o [Wireshark](https://www.wireshark.org/). Os resultados da captura foram:

**1- Captura das requisiões após a execução do projeto:**
![Execução no terminal do VS Code e pacotes HTTP no Wireshark](Imagens/execucao-e-trafego.png)

**2- Requisição e resposta da busca pelo ISO Code do país:**
* *Requisição:*
![Requisição do ISO Code no Wireshark](Imagens/requisicao-iso-code.png)
* *Resposta:*
![Resposta do ISO Code no Wireshark](Imagens/resposta-iso-code.png)

**3- Requisição e resposta da busca pela Capital do país:**
* *Requisição:*
![Requisição da Capital do país no Wireshark](Imagens/requisicao-capital.png)
* *Resposta:*
![Resposta da Capital do país no Wireshark](Imagens/resposta-capital.png)

**4- Requisição e resposta da busca pela Moeda do país:**
* *Requisição:*
![Requisição da Moeda do país no Wireshark](Imagens/requisicao-moeda.png)
* *Resposta:*
![Resposta da Moeda do país no Wireshark](Imagens/resposta-moeda.png)

**2- Requisição e resposta da busca pela Capital do país:**
* *Requisição:*
![Requisição do DDI do país no Wireshark](Imagens/requisicao-ddi.png)
* *Resposta:*
![Resposta do DDI do país no Wireshark](Imagens/resposta-ddi.png)