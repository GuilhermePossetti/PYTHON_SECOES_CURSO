# raise - lançados exceções (erros)
## https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):      
    if d == 0: #Verifica se d é zero
        raise ZeroDivisionError('Você está tentando dividir por zero')#Se for, lança manualmente (raise) um ZeroDivisionError
    return True    #Se não for, retorna True (só pra indicar que passou na validação)


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))