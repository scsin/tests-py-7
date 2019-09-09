# Desafio de programação orientada a testes

Dark sky é um serviço de previsão do tempo por API. Temos uma função que faz uma requisição para a API
do Dark sky passando a latitude e a longitude de algum lugar no planeta e a API retorna a temperatura. Nossa função
converte para °Celsius e retorna o valor da temperatura.


Escreva um teste que seja possível testar off-line a chamada para API do Dark sky e a conversão para °Celsius.
Use a bibliteca Pytest e os seguintes dados para testar a função **get_temperature**.

    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16


