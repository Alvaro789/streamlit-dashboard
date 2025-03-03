import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
# Configuración del título del Dashboard
st.title("Dashboard Interactivo de DataTech Solutions")
st.markdown("## Análisis de ventas, rendimiento de empleados y clientes")
# Sidebar - Configuración de filtros
st.sidebar.header("Configuración")
nombre_usuario = st.sidebar.text_input("Ingresa tu nombre", "Usuario")
year = st.sidebar.selectbox("Selecciona el año", [2021, 2022, 2023])
mes = st.sidebar.selectbox("Selecciona el mes", list(range(1, 13)))
color_grafico = st.sidebar.color_picker("Selecciona el color del gráfico",
"#3498db")
# Generación de datos ficticios
np.random.seed(42)
# Ventas mensuales por producto
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
"Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = np.random.randint(1000, 5000, size=12)
df_ventas = pd.DataFrame({"Mes": meses, "Ventas": ventas})
# Gráfico de Ventas Mensuales
st.subheader("Ventas Mensuales")
fig, ax = plt.subplots()
ax.plot(df_ventas["Mes"], df_ventas["Ventas"], marker="o", color=color_grafico)
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas")
ax.set_title("Tendencia de Ventas Mensuales")
plt.xticks(rotation=45)
st.pyplot(fig)
# Rendimiento de empleados por departamento
departamentos = ["Ventas", "Soporte", "Desarrollo", "Marketing"]
rendimiento = np.random.randint(50, 100, size=len(departamentos))
df_rendimiento = pd.DataFrame({"Departamento": departamentos, "Rendimiento":
rendimiento})
# Gráfico de Barras de Rendimiento de Empleados
st.subheader("Rendimiento de Empleados")
fig, ax = plt.subplots()
ax.bar(df_rendimiento["Departamento"], df_rendimiento["Rendimiento"],
color=color_grafico)
ax.set_xlabel("Departamento")
ax.set_ylabel("Rendimiento (%)")
ax.set_title("Rendimiento por Departamento")
st.pyplot(fig)
# Distribución geográfica de clientes
latitudes = np.random.uniform(-10, 50, 10)
longitudes = np.random.uniform(-80, 20, 10)
df_clientes = pd.DataFrame({"Latitud": latitudes, "Longitud": longitudes})
# Mapa de Clientes
st.subheader("Distribución Geográfica de Clientes")
m = folium.Map(location=[20, -40], zoom_start=2)
for _, row in df_clientes.iterrows():
 folium.Marker([row["Latitud"], row["Longitud"]], popup="Cliente").add_to(m)
folium_static(m)
# Mensaje de despedida
st.sidebar.markdown(f"Usuario activo: **{nombre_usuario}**")
st.success(f"¡Bienvenido, {nombre_usuario}! Esperamos que disfrutes del análisis.")
