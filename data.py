import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos desde archivo Excel en tu repositorio de GitHub
file_path = 'https://github.com/cjoya26/Data_Ventas/raw/main/DATA_VENTAS.xlsx'  # Enlace al archivo Excel
data = pd.read_excel(file_path, sheet_name='VENTAS')

# Título del dashboard
st.title("Dashboard de Ventas")

# Visualización de datos
st.subheader("Vista de los Datos")
st.dataframe(data)

# Análisis 1: Ventas Totales por Cliente
st.subheader("Ventas Totales por Cliente")
ventas_cliente = data.groupby("CLIENTE")["TOTAL FACTURA"].sum().reset_index()
fig_ventas_cliente = px.bar(ventas_cliente, x="CLIENTE", y="TOTAL FACTURA", title="Total de Ventas por Cliente")
st.plotly_chart(fig_ventas_cliente)

# Análisis 2: Estado de las Facturas
st.subheader("Estado de las Facturas")
estado_facturas = data["ESTADO"].value_counts().reset_index()
fig_estado_facturas = px.pie(estado_facturas, names="index", values="ESTADO", title="Distribución de Estados de Factura")
st.plotly_chart(fig_estado_facturas)

# Análisis 3: Comparación Total Facturado vs. Saldo por Cobrar
st.subheader("Comparación Total Facturado vs. Saldo por Cobrar")
totales = data[["TOTAL FACTURA", "SALDO POR COBRAR"]].sum()
st.metric("Total Facturado", f"S/ {totales['TOTAL FACTURA']:,.2f}")
st.metric("Saldo por Cobrar", f"S/ {totales['SALDO POR COBRAR']:,.2f}")

