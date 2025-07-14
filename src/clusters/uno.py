def pontuar_uno(row):
    pontos = 0
    pontos += int(row.get('IN_LABORATORIO_INFORMATICA', 0) == 1)
    pontos += int(row.get('IN_COMPUTADOR', 0) == 1)
    pontos += int(row.get('IN_DESKTOP_ALUNO', 0) == 1)
    pontos += int(row.get('IN_COMP_PORTATIL_ALUNO', 0) == 1)
    pontos += int(row.get('QT_COMP_PORTATIL_ALUNO', 0) > 0)
    pontos += int(row.get('IN_INTERNET', 0) == 1)
    pontos += int(row.get('IN_INTERNET_ALUNOS', 0) == 1)
    pontos += int(row.get('IN_INTERNET_APRENDIZAGEM', 0) == 1)
    pontos += int(row.get('TP_REDE_LOCAL', 0) in [1, 2, 3])
    return pontos
