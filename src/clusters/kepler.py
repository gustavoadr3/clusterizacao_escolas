def pontuar_kepler(row):
    pontos = 0

    pontos += int(row.get('IN_BIBLIOTECA', 0) == 1)
    pontos += int(row.get('IN_BIBLIOTECA_SALA_LEITURA', 0) == 1)
    pontos += int(row.get('IN_LABORATORIO_CIENCIAS', 0) == 1)
    pontos += int(row.get('IN_LABORATORIO_INFORMATICA', 0) == 1)
    pontos += int(row.get('IN_INTERNET', 0) == 1)
    pontos += int(row.get('IN_INTERNET_ALUNOS', 0) == 1)
    pontos += int(row.get('IN_INTERNET_ADMINISTRATIVO', 0) == 1)
    pontos += int(row.get('IN_INTERNET_APRENDIZAGEM', 0) == 1)
    pontos += int(row.get('IN_INTERNET_COMUNIDADE', 0) == 1)
    pontos += int(row.get('IN_ACESSO_INTERNET_COMPUTADOR', 0) == 1)
    pontos += int(row.get('IN_ACES_INTERNET_DISP_PESSOAIS', 0) == 1)
    pontos += int(row.get('IN_BANDA_LARGA', 0) == 1)
    pontos += int(row.get('IN_PROF_BIBLIOTECARIO', 0) == 1)
    pontos += int(row.get('QT_PROF_BIBLIOTECARIO', 0) < 100)
    pontos += int(row.get('IN_PROF_COORDENADOR', 0) == 1)
    pontos += int(row.get('QT_PROF_COORDENADOR', 0) < 100)
    pontos += int(row.get('IN_PROF_PEDAGOGIA', 0) == 1)
    pontos += int(row.get('QT_PROF_PEDAGOGIA', 0) < 100)
    pontos += int(row.get('IN_PROF_MONITORES', 0) == 1)
    pontos += int(row.get('QT_PROF_MONITORES', 0) < 100)


    return pontos