

def valida_cpf(cpf):
    cpf = cpf.strip().replace('.', '').replace('-', '')
    if len(cpf) == 11:
        return True
    else: return False


def listar_usuarios(lista, nome):
    for user in lista:
        if user['nome'] == nome:
            return user
        