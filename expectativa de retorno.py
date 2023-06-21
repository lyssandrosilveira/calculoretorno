import random
import streamlit as st
import matplotlib.pyplot as plt

def simulate_value_betting(win_rate, odds, bet_amount, num_simulations):
    total_bet = 0
    total_return = 0
    total_wins = 0
    returns = []
    profits = []
    expected_value = []

    for _ in range(num_simulations):
        bet = random.random() < win_rate
        total_bet += bet_amount

        if bet:
            total_return += bet_amount * odds
            total_wins += 1

        returns.append(total_return)
        profit = total_return - total_bet
        profits.append(profit)
        expected_val = (win_rate * (bet_amount * odds)) - ((1 - win_rate) * bet_amount)
        expected_value.append(expected_val)

    return total_bet, total_return, total_wins, returns, profits, expected_value

# Interface do Streamlit
st.title("Simulação de Apostas")

# Entrada dos parâmetros
win_rate = st.slider("Probabilidade de vitória", 0.0, 1.0, 0.92, 0.01)
odd_atual = st.number_input("Odd", min_value=1.0)
bet_amount = st.number_input("Valor da aposta", min_value=0.0)
num_simulations = st.number_input("Número de simulações", min_value=1, step=1, value=500)

# Rodar simulação
total_bet, total_return, total_wins, returns, profits, expected_value = simulate_value_betting(win_rate, odd_atual, bet_amount, num_simulations)

# Calcular o lucro/prejuízo
profit = total_return - total_bet

# Mostrar os resultados
st.write(f"Total apostado: {total_bet}")
st.write(f"Total retorno: {total_return}")
st.write(f"Total vitórias: {total_wins}")
st.write(f"Lucro/prejuízo: {profit}")

# Plotar o gráfico
x = range(num_simulations)
y_profits = profits
y_expected_value = expected_value

fig, ax = plt.subplots()
ax.plot(x, y_profits, label='Profit')
ax.set_xlabel('Simulação')
ax.set_ylabel('Valor')
ax.set_title(f'Expectativa de Lucro/Prejuízo - ({num_simulations} jogos simulados)')
ax.legend()

st.pyplot(fig)




