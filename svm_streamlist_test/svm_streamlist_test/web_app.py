import numpy as np
import pickle
import streamlit as st

from predict_venta_service import predict_single

# Nombre de la web app
st.set_page_config( page_title="Pinsapos IA Málaga")

# loading the saved model

with open('notebooks/models/se_vende.pck', 'rb') as f:
    dv, loaded_model = pickle.load(f)

# loaded_model = pickle.load(open('notebooks/models/se_vende.pck', 'rb'))

# creating a function for Prediction

def venta_prediction(input_data):
    

    vendido, prediction = predict_single(input_data, dv, loaded_model)

    result = {
            'Vendido': bool(vendido),
            'Vendido_probability': float(prediction),
        }

    return (result)  

    # print(input_data)
    # prediction = loaded_model.predict_proba(input_data)
    # print(prediction)

    # if (prediction[0] == 0):
    #     return 'No se vende'
    # else:
    #     return 'Se vende'

def recoger_atributos_categoricos():
    """Recoge los atributos categóricos del usuario."""
    atributos_categoricos = {}

    for atributo in [
    'aseos','baños','comunidad_incluida','estado_propiedad','garaje','muebles','parking',
    'balcon','cocina','agua','aire_acondicionado','aire_acond._central','alarma',
    'ascensor','autobuses','calefacción','calefacción_central','céntrico',
    'centros_comerciales','centros_médicos','cerca_de_universidad','colegios',
    'jardín','patio','terraza']:
        
        valor = st.checkbox(atributo)
        atributos_categoricos[atributo] = 1 if valor else 0
    return atributos_categoricos

def recoger_atributos_numericos():
    """Recoge los atributos numéricos del usuario."""
    atributos_numericos = {}

    for atributo in [
        'habitaciones_total','mt_construidos','mt_parcela','mt_utiles','precio_a_consultar',
        'precio_alquiler','precio_anterior','precio_inmobiliaria','precio_iva','precio_propietario','precio_traspaso']:

        valor = st.number_input(atributo, step=1)
        atributos_numericos[atributo] = int(valor)
    return atributos_numericos

def main():

    # giving a title
    st.title('Predicción de ventas inmuebles Malaga')

    # getting the input data from the user
    atributos_categoricos = recoger_atributos_categoricos()
    atributos_numericos = recoger_atributos_numericos()

    # Mostrar los atributos recopilados
    st.write("Atributos categóricos:")

    for atributo, valor in atributos_categoricos.items():
        st.write(f"{atributo}: {valor}")

    st.write("Atributos numéricos:")
    for atributo, valor in atributos_numericos.items():
        st.write(f"{atributo}: {valor}")
    
    
    # code for Prediction
    result = ''
    
    # creating a button for Prediction
    
    if st.button('Venta Test Result'):
        atrib_total = dict(atributos_categoricos.items() | atributos_numericos.items())
        result = venta_prediction(atrib_total)
        
        
    st.success(result)
    
    
    
    
    
if __name__ == '__main__':
    main()