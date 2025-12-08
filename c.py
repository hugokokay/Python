"""Pequeno script que pergunta ao usuário se ele(a) está bem.

Melhorias:
- Normaliza a entrada (strip + lower)
- Trata respostas afirmativas e negativas comuns
- Fornece mensagem clara em caso de resposta não reconhecida
- Coloca lógica em funções e `main()` para facilitar testes
"""

def is_affirmative(answer: str) -> bool:
    if answer is None:
        return False
    a = answer.strip().lower()
    return a in ("s", "sim", "y", "yes", "1")


def is_negative(answer: str) -> bool:
    if answer is None:
        return False
    a = answer.strip().lower()
    return a in ("n", "nao", "não", "no", "0")


def main() -> None:
    print("Digite 'x' a qualquer momento para sair.")
    while True:
        try:
            resp = input("Você está bem? [sim/não] ")
        except EOFError:
            print('\nEntrada finalizada. Saindo.')
            break

        if resp is None:
            print('Resposta vazia. Digite "sim", "não" ou "x" para sair.')
            continue

        if resp.strip().lower() == 'x':
            print('Saindo...')
            break

        if is_affirmative(resp):
            print('Que bom!')
        elif is_negative(resp):
            print('Espero que melhore logo!')
        else:
            print("Não entendi sua resposta. Por favor responda 'sim' ou 'não' (ou digite 'x' para sair).")


if __name__ == '__main__':
    main()
