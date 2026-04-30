CREATE TABLE categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    tipo TEXT
);

CREATE TABLE transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    descricao TEXT,
    valor REAL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);