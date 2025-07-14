def pontuar_farias(row):
    pontos = 0
    pontos += int(row.get('IN_INTERNET', 0) == 1)
    pontos += int(row.get('IN_INTERNET_ALUNOS', 0) == 1)
    pontos += int(row.get('IN_BANDA_LARGA', 0) == 1)
    pontos += int(row.get('IN_DIURNO', 0) == 1)
    pontos += int(row.get('IN_MED', 0) == 1)
    pontos += int(row.get('QT_MAT_MED', 0) > 100)
    pontos += int(row.get('QT_MAT_MED_INT', 0) > 20)
    pontos += int(row.get('QT_DOC_MED', 0) > 10)
    pontos += int(row.get('QT_TUR_MED', 0) > 3)
    pontos += int(row.get('QT_TUR_MED_INT', 0) > 1)
    return pontos