# As estruturas de controle nos permitem controlar o fluxo de execução de nossos programas. 
# Em Python, as estruturas de controle mais comuns são as estruturas condicionais e os loops. 
# Essas estruturas nos permitem tomar decisões e repetir blocos de código segundo certas condições.

# Estruturas condicionais
# As estruturas condicionais nos permitem executar diferentes blocos de código segundo se cumpra ou não uma determinada condição.
# Em Python, as estruturas condicionais mais utilizadas são if, if-else e if-elif-else.

# Profit diário esperado
profit_esperado = 10 # representando 10kk

# Profit feito hoje
profit_hoje = 11 # representando 11kk

# Verifica diferença e imprime a mensagem correspondente

if profit_hoje >= 10:
    print ("Excelente! Batemos a meta!")

elif profit_hoje >= 9:
    print ("Profit aceitável, mas falta 1kk para bater a meta.")

elif profit_hoje >= 8:
    print ("Ok, faltam 2kk para bater a meta.")

elif profit_hoje >= 7:
    print ("Aconteceu alguma coisa? Faltam 3kk para bater a meta, precisamos melhorar!")

else:
    print ("Talvez seja melhor procurar outro método para melhorar o profit e atingir a meta.")