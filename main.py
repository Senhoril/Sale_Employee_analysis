import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

# Configurar estilo do seaborn
sns.set_style("whitegrid")
sns.set_palette("husl")

def gerar_salarios_aleatorios():
    salarios_aleatorios = np.append(np.random.randint(low=3000, high=6000, size=7), 9000)
    return salarios_aleatorios


def criar_dataframe_vendas(df_funcionarios):
    """Cria um DataFrame de vendas baseado nos vendedores"""
    # Filtra apenas os vendedores
    vendedores = df_funcionarios[df_funcionarios['cargo'] == 'vendedor']['nome'].tolist()

    # Define os meses
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    # Lista para armazenar os dados de vendas
    dados_vendas = []

    # Gera dados de vendas para cada vendedor em cada mês
    np.random.seed(42)  # Para resultados reproduzíveis
    for vendedor in vendedores:
        for i, mes in enumerate(meses):
            # Vendas base entre 2000 e 8000
            vendas = np.random.normal(5000, 1500)

            # Ajustes sazonais
            if mes in ['Nov', 'Dez']:  # Black Friday e Natal
                vendas += 2000
            elif mes in ['Jan', 'Fev']:  # Início do ano mais fraco
                vendas -= 1000

            # Alguns vendedores são melhores
            if vendedor == 'Ana':
                vendas += 1000
            elif vendedor == 'Elena':
                vendas += 800

            # Garantir que não seja negativo
            vendas = max(vendas, 1000)

            dados_vendas.append({
                'vendedor': vendedor,
                'mes': mes,
                'mes_num': i + 1,
                'vendas': round(vendas, 2),
                'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste']),
                'produto': np.random.choice(['Produto A', 'Produto B', 'Produto C', 'Produto D']),
                'comissao': round(vendas * 0.05, 2)  # 5% de comissão
            })

    return pd.DataFrame(dados_vendas)


# Criar dados
funcionarios = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fernando', 'Gabi', 'Hugo'],
    'data_nascimento': ['1987-03-15', '1982-11-22', '1990-07-08', '1985-01-30', '1992-09-12', '1988-05-17',
                        '1991-12-03', '1983-08-25'],
    'data_criacao': ['2021-06-10', '2020-03-15', '2023-11-08', '2022-09-20', '2024-01-12', '2021-10-05', '2022-07-18',
                     '2020-12-30'],
    'salario': gerar_salarios_aleatorios(),
    'cargo': ['vendedor', 'vendedor', 'vendedor', 'rh', 'vendedor', 'vendedor', 'ti', 'gerente']
}

df_funcionarios = pd.DataFrame(funcionarios)
df_funcionarios['data_nascimento'] = pd.to_datetime(df_funcionarios['data_nascimento'])
df_funcionarios['data_criacao'] = pd.to_datetime(df_funcionarios['data_criacao'])
df_funcionarios['idade'] = ((pd.to_datetime('today') - df_funcionarios['data_nascimento']).dt.days / 365.25).astype(int)

# Criar DataFrame de vendas
df_vendas = criar_dataframe_vendas(df_funcionarios)

print("DataFrame Funcionários:")
print(df_funcionarios)
print("\nDataFrame Vendas:")
print(df_vendas.head(10))

# Criar os 4 subplots usando seaborn
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análises de Funcionários e Vendas', fontsize=16, fontweight='bold')

# Subplot 1: Distribuição de Salários por Cargo
ax1 = axes[0, 0]
sns.barplot(data=df_funcionarios, x='cargo', y='salario', hue='cargo', ax=ax1, 
            estimator=np.mean, palette='Set2', legend=False)
ax1.set_title('Salário Médio por Cargo')
ax1.set_xlabel('Cargo')
ax1.set_ylabel('Salário Médio (R$)')
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: Vendas Totais por Vendedor
ax2 = axes[0, 1]
vendas_por_vendedor = df_vendas.groupby('vendedor')['vendas'].sum().reset_index()
vendas_por_vendedor = vendas_por_vendedor.sort_values('vendas', ascending=False)
sns.barplot(data=vendas_por_vendedor, x='vendedor', y='vendas', hue='vendedor', 
            ax=ax2, palette='viridis', legend=False)
ax2.set_title('Vendas Totais por Vendedor (Ano)')
ax2.set_xlabel('Vendedor')
ax2.set_ylabel('Vendas Totais (R$)')
ax2.tick_params(axis='x', rotation=45)

# Subplot 3: Evolução das Vendas por Mês
ax3 = axes[1, 0]
vendas_mensais = df_vendas.groupby(['mes_num', 'mes'])['vendas'].sum().reset_index()
sns.lineplot(data=vendas_mensais, x='mes_num', y='vendas', ax=ax3, 
             marker='o', linewidth=2, color='green')
ax3.set_title('Evolução das Vendas por Mês')
ax3.set_xlabel('Mês')
ax3.set_ylabel('Vendas Totais (R$)')
meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(meses_nomes, rotation=45)

# Subplot 4: Idade vs Salário dos Funcionários
ax4 = axes[1, 1]
sns.scatterplot(data=df_funcionarios, x='idade', y='salario', hue='cargo',
                ax=ax4, s=100, alpha=0.8, palette='Set1')
ax4.set_title('Relação Idade vs Salário por Cargo')
ax4.set_xlabel('Idade')
ax4.set_ylabel('Salário (R$)')
ax4.legend(title='Cargo')

plt.tight_layout()
plt.show()

# Estatísticas adicionais
print(f"\n--- ESTATÍSTICAS ---")
print(f"Total de vendedores: {len(df_vendas['vendedor'].unique())}")
print(f"Vendas totais do ano: R$ {df_vendas['vendas'].sum():,.2f}")
print(f"Média de vendas por mês: R$ {df_vendas.groupby('mes')['vendas'].sum().mean():,.2f}")
vendas_por_vendedor_stats = df_vendas.groupby('vendedor')['vendas'].sum().sort_values(ascending=False)
print(f"Melhor vendedor: {vendas_por_vendedor_stats.index[0]} (R$ {vendas_por_vendedor_stats.iloc[0]:,.2f})")
print(f"Salário médio da empresa: R$ {df_funcionarios['salario'].mean():,.2f}")