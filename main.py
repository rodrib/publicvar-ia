import streamlit as st
import pandas as pd
import plotly.express as px 

# Page title
st.set_page_config(page_title='Publicvar-IA', page_icon='📊',
                   layout="wide", # Forma de layout ancho o compacto
                    initial_sidebar_state="expanded" # Definimos si el sidebar aparece expandido o colapsado
                   )
st.title('📊 Analisis de datos del IGeHM')

with st.expander('Sobre esta app'):
  st.markdown('**¿Qué puede hacer esta aplicación??**')
  st.info('Esta aplicación muestra la distribucion de genes y variantes en Cancer')
  st.markdown('**How to use the app?**')
  st.warning('Para interactuar con la aplicación, 1. Haga click en play')

gsheetid='1jAdbksm3fu5uVE7NOGe7LtSSJBjQGEPzc0c44f9Ud4s'
sheetid='0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}&format'
#st.write(url)


df = pd.read_csv(url)
#https://docs.google.com/spreadsheets/d/1jAdbksm3fu5uVE7NOGe7LtSSJBjQGEPzc0c44f9Ud4s/edit?usp=sharing

# Mostrar el DataFrame usando st.dataframe()
#st.dataframe(df)  # Esta función permite desplazarse por la tabla si es necesario


# Opción para mostrar todos los valores # comento por ahora //
#mostrar_todos = st.checkbox("Mostrar todos los valores")



#if mostrar_todos:
#    st.dataframe(df) 


# Mostrar las columnas del DataFrame en Streamlit
# st.write("Columnas disponibles en el DataFrame:")
# st.write(df.columns)

# # Seleccionar columnas usando Streamlit
# columnas_seleccionadas = st.multiselect(
#     'Selecciona las columnas que deseas ver:',
#     df.columns
# )

# # Mostrar el nuevo DataFrame con las columnas seleccionadas
# if columnas_seleccionadas:
#     nuevo_df = df[columnas_seleccionadas]
#     st.write("Nuevo DataFrame con las columnas seleccionadas:")
#     st.dataframe(nuevo_df)
# else:
#     st.write("Por favor, selecciona al menos una columna.")

# ####
# # Subtítulo "Genes vs Impacto"
# st.subheader("Genes vs Impacto")

# # Filtro por la columna "Tiene resultado"
# tiene_resultado = st.selectbox('Filtrar por "Tiene resultado":', options=['SI', 'NO'])

# # Filtrar el DataFrame si el usuario selecciona "SI"
# if tiene_resultado == 'SI':
#     df_filtrado = df[df['Tiene resultado'] == 'SI'][['Gen', 'tipo', 'EXON', 'var-gen', 'var-prot', 'Impacto', 'Tiene otra?']]
# else:
#     df_filtrado = df[df['Tiene resultado'] == 'NO'][['Gen', 'tipo', 'EXON', 'var-gen', 'var-prot', 'Impacto', 'Tiene otra?']]

# # Mostrar el nuevo DataFrame
# st.write("Nuevo DataFrame filtrado:")
# st.dataframe(df_filtrado)


# ### Valores numericos de los indicadores de los estudios realizados
#num_filas_pac = len(df_filtrado)

#cant_genes_unicos = len(df_filtrado['Gen'].unique())
#//

##### interactivo

# Subtítulo "Genes vs Impacto"
#st.subheader("Graficos animados")



import pandas as pd
from ipyvizzu import Config, Data, Style
from ipyvizzustory import Story, Slide, Step

d_types = {
    "Unnamed: 0": float,
    "Gen": str,
    "tipo": str,
    "EXON": str,
    "var-gen": str,
    "var-prot": str,
    "Impacto": str,
    "Tiene otra?": str,
}


#df1 = pd.read_csv("pages\igehm_m1.csv", dtype=d_types)
import os
df1 = pd.read_csv(os.path.join("pages", "igehm_m1.csv"), dtype=d_types)

#st.dataframe(df1)


data = Data()
data.add_df(df1)

story = Story(data)
story.set_size(640, 480)
story.set_feature("tooltip", True)

story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": ["Gen", "count()"],
                    "y": {"set": None, "range": {"min": "-200%", "max": "100%"}},
                    "color": "Gen",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "Gen",
                    "lightness": None,
                    "size": ["Gen", "count()"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "Impacto",
                    "lightness": None,
                    "size": ["Gen", "count()"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#eb0000 #fd7c4b #cc9577 #fda276 #d5895b #dc9376 #a46850 #fd723c #e97c5e #b3654e #b75121 #966443 #d15948 #fd6a4a #fe9f8a #bb5b58 #fb786c #fc5a54 #fd8047 #fe4e49 #ff8d69 #dab18f #e9908f #9e8171 #99746b",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "tipo",
                    "lightness": None,
                    "size": ["Gen", "count()"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#3394b6 #5ab4cb #4199b9 #599f9c #bf7caf #b6918b #8785a9 #76b4ce #8f8dba #6b789e #6b5c78 #757284 #8ea5be #8498aa #778393 #b897a4 #64ad9f #977675 #65dbd5",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter("(record['Gen'].includes('BRCA1'))"),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "Gen",
                    "lightness": None,
                    "size": ["var-gen", "count()"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter("(record['Gen'].includes('BRCA1'))"),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": "count()",
                    "y": {
                        "set": ["Gen", "var-gen"],
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "Gen",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter("(record['Gen'].includes('BRCA2'))"),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "Gen",
                    "lightness": None,
                    "size": ["var-gen", "count()"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)
story.add_slide(
    Slide(
        Step(
            Data.filter("(record['Gen'].includes('BRCA2'))"),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": "count()",
                    "y": {
                        "set": ["Gen", "var-gen"],
                        "range": {"min": "auto", "max": "auto"},
                    },
                    "color": "Gen",
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                    "label": None,
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#694db1 #029a67 #fa7f16 #f1c226 #d06c29 #d19565 #f1474d #b6a720 #807126 #f4714d #b55ca9 #f58ffc #bc458e #9c7cee #9c4fb4 #6f9ffc #5e6cbc #79858d #a99789 #4c7350 #ae7a43 #7bb057 #497655 #9d1069 #ae3894 #b20000",
                        },
                    }
                }
            ),
        )
    )
)

#story.play()


# Encabezado
st.header("Estadisticas de NGS en Cancer")
cantidad_pacientes = 247 #num_filas_pac
cantidad_genes = 34 #cant_genes_unicos
disciplines = 12 # df['discipline'].nunique()
ages = 20 #df[df['age'].astype(int)>0]['age'].nunique()
agesMin = 1 #df[df['age'].astype(int)>0]['age'].min()
agesMax = 11 #df[df['age'].astype(int)>0]['age'].max()
cols = st.columns([2,10,2])
with cols[0]:
    st.image("https://gremialweb.com/wp-content/uploads/2024/02/Genetica-501x445.png")
    st.info("Created with ❤️ by [Rodrigo Bogado]")    
with cols[1]:
    story.play()
    st.info("Click on the play button to see every slide...enjoy 😁")
with cols[2]:
    st.metric("Total de Pacientes:",f"{cantidad_pacientes:,.0f}")
    st.metric("Cantidad de Genes:", f"{cantidad_genes:,.0f}")
    #st.metric("Positivos:",f"{disciplines:,.0f}")
    #st.metric("Negativos:",f"{ages:,.0f}")
    #st.metric("Mas Joven:",f"{agesMin} years old")
    #st.metric("Mas Viejo:",f"{agesMax} years old")