etcdctl snapshot save snapshot.db       # Cria snapshot nomeando como snapshot.db
etcdctl snapshot status snapshot.db     # Exibe o status e informações sobre o arquivo
etcdctl snapshot restore snapshot.db    # Restaura o snapshot