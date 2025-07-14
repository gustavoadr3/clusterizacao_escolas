def pontuar_compartilha(row):
    pontos = 0
    pontos += int(row.get("IN_PROF_COORDENADOR", 0) == 1)
    pontos += int(row.get("QT_PROF_COORDENADOR", 0) >= 5)
    pontos += int(row.get("IN_PROF_PEDAGOGIA", 0) == 1)
    pontos += int(row.get("QT_PROF_PEDAGOGIA", 0) >= 10)
    pontos += int(row.get("QT_DOC_BAS", 0) >= 10)
    pontos += int(row.get("QT_DOC_INF", 0) >= 10)
    pontos += int(row.get("QT_DOC_INF_CRE", 0) >= 10)
    pontos += int(row.get("QT_DOC_INF_PRE", 0) >= 10)
    pontos += int(row.get("QT_DOC_FUND", 0) >= 10)
    pontos += int(row.get("QT_DOC_FUND_AI", 0) >= 10)
    pontos += int(row.get("QT_DOC_FUND_AF", 0) >= 10)
    pontos += int(row.get("QT_DOC_MED", 0) >= 10)
    pontos += int(row.get("QT_DOC_PROF", 0) >= 10)
    pontos += int(row.get("QT_DOC_PROF_TEC", 0) >= 10)
    return pontos
