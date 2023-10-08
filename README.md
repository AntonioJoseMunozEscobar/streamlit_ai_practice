<h1> IA con Scikit-Learn en Python</h1>
Este proyecto está enfocado en gestionar una base de datos de una inmobiliaria. El objetivo es determinar la probabilidad de venta potencial de una vivienda en base
a sus características como su precio, dormitorios, aseos, metros de vivienda, y otras características...


<h2> Qué tecnologías se han utilizado a lo largo del proyecto:</h2>
- Python (Librerías [NumPy, Pandas, Scikit-Learn, Streamlit, Matplotlib, Ipykernel, Pickle]). </br>
- Poetry para crear una virtualización de dependencias. </br>
- Streamlit cloud para lanzar la webapp. </br>
</br>
El proyecto consta de la búsqueda de una base de datos, la cual se ha recogido de un CRM de una inmobiliaria
local de Málaga. Después el modelado de una máquina de soporte vectorial (SVM) para poder clasificar en "Vendido" o "No vendido"
una propiedad. </br>
Y por último aplicamos esa SVM a una serie de datos que nosotros le introduciremos desde la webapp. Originalmente
este proyecto estaba hecho mediante un endpoint y una petición POST con la librería Flask, sin embargo he decidido probar nuevas
librerías para desarrollar aplicaciones web.

<h2>Aquí el enlace a la <a href="https://inmobiliaria-malaga-ai.streamlit.app" rel="nofollow">aplicación</a> para poder probarla</h2>
