# 5) Escreva um programa que permita ao usuário digitar a nota do aluno na prova, a
#   nota do aluno nos trabalhos e a freqüência do mesmo. O calculo da nota do aluno
#   é calculada sabendo que a prova tem peso de 70% e o trabalho de 30%. A partir
#   dos dados abaixo indique se o aluno está aprovado, reprovado ou em recuperação.
# - Aprovado: média >= 6.0 e freqüência >=75%
# - Recuperação: média >=4.0 e média <6.0 e freqüência>=75%
# - Reprovado: média<4.0 ou freqüência <75%

nota = float(input('Digite a nota do aluno na Prova: '))
trabalho = float(input('Digite a nota do Trabalho do aluno: '))
freq = float(input('Digite a taxa de frequência do aluno: '))

mediap = nota * 0.7
mediat = trabalho * 0.3
mediafinal = mediap + mediat

if mediafinal >= 6 and freq >= 75:
    print('Parabéns o aluno foi aprovado em ambos os requisitos.')

elif mediafinal >= 4 and freq >= 75:
    print('Que pena, o aluno não foi aprovado pela nota, mas terá a oportunidade de fazer a recuperação.')

else:
    print('Infelizmente o aluno não obteve a média de nota ou '
          'frequencia necessária para ser aprovado ou fazer recuperação.')

print(f'A nota obtida pelo aluno na prova com base no peso estabelecido é: ', mediap)
print(f'A nota obtida pelo aluno no trabalho com base no peso estabelecido é :', mediat)
print(f'Frequência: ', freq, '%')