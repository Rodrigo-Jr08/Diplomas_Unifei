from generated import *


def coleta_dados_diplomado(cpf_busca:str):

    print(f"\n--- Coletando dados do diplomado (CPF: {cpf_busca}) ---")

    endereco = obter_endereco()
    naturalidade = Tnaturalidade()

    #insira função para obter 
    
def obter_campo(campo:str,prompt:str,obrigatorio:bool=False):

    sufixo = "(Campo obrigatório)" if obrigatorio else "(Campo opcional)"
    
    while 1:
        val = input("{prompt}{sufixo}").strip()

        if val!="":
            return val

        if not obrigatorio:
            return None

        print("Esse campo é obrigatório, você precisa inserir alguma informação")
    
    
def validar_Tuf(valor: str) -> bool:
    try:
        Tuf(valor)
        return True
    except ValueError:
        return False

def busca_banco(campo:str):
    valor = None
    return valor

def obter_endereco()->Tendereco:
    print("--- Buscando as informações referentes ao endereço ---")
    #Pega os campos simples
    logradouro=obter_campo(campo="Logradouro",prompt="Insira o logradouro: ",obrigatorio=True)
    bairro=obter_campo(campo="Bairro",prompt="Insira o bairro: ",obrigatorio=True)
    cep=obter_campo(campo="cep",prompt="Insira o CEP: ",obrigatorio=True)
    numero=obter_campo(campo="Numero",prompt="Insira o numero: ")
    complemento=obter_campo(campo="Complemento",prompt="Insira o complemento: ")

    #Pega o municipio nacional (do banco)
    codigo_municipio=busca_banco(campo="Codigo Municipio")
    nome_municipio=busca_banco(campo="Nome municipio")
    uf = busca_banco(campo="UF")

    #Pega o nome estrangeiro (do banco, tenta)
    nome_municipio_estrangeiro = busca_banco(campo="Nome municipio estrangeiro")

    #Se tiver alguma coisa do municipio nacional, pede pra completar o restante
    if codigo_municipio or nome_municipio or uf:
        codigo_municipio=obter_campo(campo="Codigo Municipio",prompt="Insira o código do Municipio",obrigatorio=True)
        nome_municipio=obter_campo(campo="Nome municipio",prompt="Insira o nome do municipio",obrigatorio=True)
        while 1:
            uf = obter_campo(campo="UF",prompt="Insira a Unidade Federal",obrigatorio=True)
            if validar_Tuf(uf): break
    #senao pede o estrangeiro 
    else:
        nome_municipio = obter_campo(campo="Nome Municipio",prompt="Insira o nome do municipio estrangeiro",obrigatorio=True)
    

    endereco = Tendereco(
        logradouro=logradouro,
        bairro=bairro,
        cep=cep,
        numero=numero,
        complemento=complemento,
        codigo_municipio=codigo_municipio,
        nome_municipio=nome_municipio,
        uf=uf,
        nome_municipio_estrangeiro=nome_municipio_estrangeiro
    )
    return endereco
        